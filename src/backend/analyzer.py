import httpx
from bs4 import BeautifulSoup
from typing import Dict, List, Any, Optional
from .checks.alt_text import AltTextCheck
from .checks.language_declared import LanguageDeclaredCheck
from .checks.heading_hierarchy import HeadingHierarchyCheck
from .checks.form_labels import FormLabelsCheck
from .checks.keyboard_nav import KeyboardNavCheck


class AccessibilityAnalyzer:
    """
    Clase principal para coordinar el análisis de accesibilidad de un sitio web.
    """

    def __init__(self, url: str):
        self.url: str = url
        self.soup: Optional[BeautifulSoup] = None
        self.html_content: str = ""

    async def fetch_content(self) -> None:
        """
        Descarga el contenido HTML de la URL proporcionada.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url)
            response.raise_for_status()
            self.html_content = response.text
            self.soup = BeautifulSoup(self.html_content, "html.parser")

    async def analyze(self) -> Dict[str, Any]:
        """
        Ejecuta todos los chequeos de accesibilidad y devuelve los resultados.
        """
        if not self.soup:
            await self.fetch_content()

        issues: List[Dict[str, Any]] = []

        # Run various checks
        checks = [
            AltTextCheck(),
            LanguageDeclaredCheck(),
            HeadingHierarchyCheck(),
            FormLabelsCheck(),
            KeyboardNavCheck(),
        ]

        for check in checks:
            check_results = check.run(self.soup)
            issues.extend(check_results)

        # Simple score calculation (to be improved)
        failed_checks = len(set(issue["type"] for issue in issues))
        score: float = max(0, 100 - (failed_checks * 10))

        return {
            "url": self.url,
            "score": score,
            "issues": issues,
            "raw_html": self.html_content,
        }
