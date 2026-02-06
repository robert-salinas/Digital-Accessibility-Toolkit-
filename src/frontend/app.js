document.addEventListener('DOMContentLoaded', () => {
    const urlForm = document.getElementById('url-form');
    const urlInput = document.getElementById('url-input');
    const resultsSection = document.getElementById('results');
    const loadingSection = document.getElementById('loading');
    const summaryText = document.getElementById('summary-text');
    const scoreValue = document.getElementById('score-value');
    const issuesList = document.getElementById('issues-list');

    urlForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const url = urlInput.value;
        if (!url) return;

        // Show loading
        loadingSection.hidden = false;
        resultsSection.hidden = true;
        issuesList.innerHTML = '';

        try {
            const response = await fetch('/audit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: url, lang: 'es' }),
            });

            if (!response.ok) {
                throw new Error('Error en el servidor');
            }

            const data = await response.json();
            displayResults(data);
        } catch (error) {
            alert('Error al conectar con el servidor: ' + error.message);
        } finally {
            loadingSection.hidden = true;
        }
    });

    function displayResults(data) {
        resultsSection.hidden = false;
        scoreValue.textContent = data.score;
        summaryText.textContent = data.summary;

        if (data.issues.length === 0) {
            issuesList.innerHTML = '<p class="success">No se encontraron problemas automáticos. ¡Excelente!</p>';
            return;
        }

        data.issues.forEach(issue => {
            const issueEl = document.createElement('div');
            issueEl.className = `issue issue-${issue.severity}`;
            issueEl.innerHTML = `
                <strong>${issue.severity}: ${issue.type}</strong>
                <p>${issue.message}</p>
                <code>Elemento: ${escapeHtml(issue.element)}</code>
            `;
            issuesList.appendChild(issueEl);
        });
        
        // Move focus to results for screen readers
        resultsSection.querySelector('h2').focus();
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
});
