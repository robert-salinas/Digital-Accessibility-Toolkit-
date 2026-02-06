from bs4 import BeautifulSoup
from typing import List, Dict
from .alt_text import BaseCheck


class FormLabelsCheck(BaseCheck):
    def run(self, soup: BeautifulSoup) -> List[Dict]:
        issues = []
        inputs = soup.find_all("input")
        for inp in inputs:
            # Skip hidden inputs and submit/button
            if inp.get("type") in ["hidden", "submit", "button", "reset"]:
                continue

            input_id = inp.get("id")
            has_label = False

            if input_id:
                label = soup.find("label", attrs={"for": input_id})
                if label:
                    has_label = True

            # Check if wrapped in label
            if not has_label:
                parent = inp.parent
                while parent:
                    if parent.name == "label":
                        has_label = True
                        break
                    parent = parent.parent

            if not has_label:
                issues.append(
                    {
                        "type": "form_labels",
                        "severity": "CRITICAL",
                        "element": str(inp)[:100],
                        "message_key": "issue_form_label_missing",
                    }
                )
        return issues
