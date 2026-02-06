from bs4 import BeautifulSoup
from typing import List, Dict
from .alt_text import BaseCheck


class LanguageDeclaredCheck(BaseCheck):
    def run(self, soup: BeautifulSoup) -> List[Dict]:
        issues = []
        html_tag = soup.find("html")
        if not html_tag or not html_tag.has_attr("lang"):
            issues.append(
                {
                    "type": "language_declared",
                    "severity": "CRITICAL",
                    "element": "<html>",
                    "message_key": "issue_lang_missing",
                }
            )
        return issues
