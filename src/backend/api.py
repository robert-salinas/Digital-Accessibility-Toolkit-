from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from .analyzer import AccessibilityAnalyzer
from .report_generator import generate_report
from .database import init_db, save_audit, get_history

app = FastAPI(title="Digital Accessibility Toolkit API")


# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()


class AuditRequest(BaseModel):
    url: str
    lang: str = "es"


class AuditResponse(BaseModel):
    url: str
    score: float
    issues: List[dict]
    summary: str
    report_url: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Digital Accessibility Toolkit API is running"}


@app.post("/audit", response_model=AuditResponse)
async def run_audit(request: AuditRequest):
    try:
        analyzer = AccessibilityAnalyzer(request.url)
        results = await analyzer.analyze()

        report = generate_report(results, lang=request.lang)

        # Save to database
        save_audit(
            url=request.url,
            score=results["score"],
            issues=results["issues"],
            summary=report["summary"],
        )

        return {
            "url": request.url,
            "score": results["score"],
            "issues": results["issues"],
            "summary": report["summary"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history")
async def audit_history(limit: int = 10):
    try:
        return get_history(limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
