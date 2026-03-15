from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import os
import threading
import uvicorn
import webview
from .analyzer import AccessibilityAnalyzer
from .report_generator import generate_report
from .database import init_db, save_audit, get_history

app = FastAPI(title="Digital Accessibility Toolkit API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Request/Response Models
class AuditRequest(BaseModel):
    url: str
    lang: str = "es"

class AuditResponse(BaseModel):
    url: str
    score: float
    issues: List[dict]
    summary: str
    report_url: Optional[str] = None

# API Endpoints
@app.post("/audit", response_model=AuditResponse)
async def run_audit(request: AuditRequest):
    try:
        analyzer = AccessibilityAnalyzer(request.url)
        results = await analyzer.analyze()
        report = generate_report(results, lang=request.lang)
        
        save_audit(
            url=request.url,
            score=results["score"],
            issues=results["issues"],  # Save raw issues with keys for future flexibility
            summary=report["summary"],
        )

        return {
            "url": request.url,
            "score": report["score"],
            "issues": report["issues"],  # Return TRANSLATED issues to frontend
            "summary": report["summary"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history")
async def audit_history(limit: int = 10, lang: str = "es"):
    try:
        raw_history = get_history(limit=limit)
        translated_history = []
        
        for item in raw_history:
            # We treat each history item as a result set to translate it
            report = generate_report(item, lang=lang)
            translated_history.append({
                "url": item["url"],
                "score": report["score"],
                "issues": report["issues"],
                "summary": report["summary"],
                "created_at": item["created_at"]
            })
            
        return translated_history
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Static Files & Frontend (Practical MVP approach)
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

app.mount("/", StaticFiles(directory=FRONTEND_DIR), name="static")

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

if __name__ == "__main__":
    # Start FastAPI in a background thread
    t = threading.Thread(target=run_server, daemon=True)
    t.start()

    # Create the native GUI window
    print("[INFO] Lanzando interfaz de escritorio...")
    webview.create_window(
        'Digital Accessibility Toolkit - DAT', 
        'http://127.0.0.1:8000',
        width=1200,
        height=800,
        background_color='#1A1F2E'
    )
    webview.start()
