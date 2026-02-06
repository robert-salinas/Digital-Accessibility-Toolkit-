from bs4 import BeautifulSoup
from typing import List, Dict
from .alt_text import BaseCheck

class KeyboardNavCheck(BaseCheck):
    BAD_PHRASES = ["click aquí", "haz click", "leer más", "ver más", "click here", "read more"]

    def run(self, soup: BeautifulSoup) -> List[Dict]:
        issues = []
        
        # Check generic links
        links = soup.find_all("a")
        for link in links:
            text = link.get_text().strip().lower()
            if text in self.BAD_PHRASES:
                issues.append({
                    "type": "link_context",
                    "severity": "WARNING",
                    "element": str(link)[:100],
                    "message_key": "issue_link_generic",
                    "params": {"text": text}
                })

        # Check positive tabindex
        tabindexed = soup.find_all(attrs={"tabindex": True})
        for el in tabindexed:
            try:
                val = int(el["tabindex"])
                if val > 0:
                    issues.append({
                        "type": "keyboard_nav",
                        "severity": "CRITICAL",
                        "element": str(el)[:100],
                        "message_key": "issue_tabindex_positive"
                    })
            except ValueError:
                pass
                
        return issues
