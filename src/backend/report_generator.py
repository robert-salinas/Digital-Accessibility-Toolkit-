from typing import Dict, Any, List
from .utils import translate


def generate_report(results: Dict[str, Any], lang: str = "es") -> Dict[str, Any]:
    issues = results.get("issues", [])
    score = results.get("score", 0)

    # Translate summary
    if score >= 90:
        summary_key = "summary_excellent"
    elif score >= 70:
        summary_key = "summary_good"
    else:
        summary_key = "summary_bad"

    summary = translate(summary_key, lang)

    # Translate each issue
    translated_issues = []
    for issue in issues:
        msg_key = issue.get("message_key")
        params = issue.get("params", {})

        # Translate severity and message
        severity_key = f"severity_{issue['severity'].lower()}"
        translated_issue = {
            "type": issue["type"],
            "severity": translate(severity_key, lang),
            "element": issue["element"],
            "message": translate(msg_key, lang, **params),
        }
        translated_issues.append(translated_issue)

    return {"summary": summary, "score": score, "issues": translated_issues}
