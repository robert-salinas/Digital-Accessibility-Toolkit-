import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any

DB_PATH = "accessibility_toolkit.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            score REAL NOT NULL,
            issues TEXT NOT NULL,
            summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_audit(url: str, score: float, issues: List[Dict], summary: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO audits (url, score, issues, summary)
        VALUES (?, ?, ?, ?)
    ''', (url, score, json.dumps(issues), summary))
    conn.commit()
    conn.close()

def get_history(limit: int = 10) -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM audits ORDER BY created_at DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    
    history = []
    for row in rows:
        history.append({
            "id": row["id"],
            "url": row["url"],
            "score": row["score"],
            "issues": json.loads(row["issues"]),
            "summary": row["summary"],
            "created_at": row["created_at"]
        })
    
    conn.close()
    return history
