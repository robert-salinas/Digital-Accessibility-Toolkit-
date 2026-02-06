from bs4 import BeautifulSoup
from typing import List, Dict


class BaseCheck:
    def run(self, soup: BeautifulSoup) -> List[Dict]:
        raise NotImplementedError("Subclasses must implement run()")


class AltTextCheck(BaseCheck):
    def run(self, soup: BeautifulSoup) -> List[Dict]:
        issues = []
        images = soup.find_all("img")
        for img in images:
            if not img.has_attr("alt"):
                issues.append(
                    {
                        "type": "alt_text",
                        "severity": "CRITICAL",
                        "element": str(img)[:100],
                        "message_key": "issue_alt_text",
                    }
                )
            elif not img["alt"].strip():
                issues.append(
                    {
                        "type": "alt_text",
                        "severity": "WARNING",
                        "element": str(img)[:100],
                        "message_key": "issue_alt_empty",
                    }
                )
        return issues
