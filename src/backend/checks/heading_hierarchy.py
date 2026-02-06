from bs4 import BeautifulSoup
from typing import List, Dict
from .alt_text import BaseCheck


class HeadingHierarchyCheck(BaseCheck):
    def run(self, soup: BeautifulSoup) -> List[Dict]:
        issues = []
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        if not headings:
            issues.append(
                {
                    "type": "heading_hierarchy",
                    "severity": "WARNING",
                    "element": "body",
                    "message_key": "issue_headings_none",
                }
            )
            return issues

        last_level = 0
        for h in headings:
            current_level = int(h.name[1])
            if current_level > last_level + 1 and last_level != 0:
                issues.append(
                    {
                        "type": "heading_hierarchy",
                        "severity": "WARNING",
                        "element": str(h)[:100],
                        "message_key": "issue_headings_broken",
                        "params": {"last": last_level, "current": current_level},
                    }
                )
            last_level = current_level

        return issues
