document.addEventListener('DOMContentLoaded', () => {
    const urlForm = document.getElementById('url-form');
    const urlInput = document.getElementById('url-input');
    const urlError = document.getElementById('url-error');
    const resultsSection = document.getElementById('results');
    const loadingSection = document.getElementById('loading');
    const summaryText = document.getElementById('summary-text');
    const scoreValue = document.getElementById('score-value');
    const issuesList = document.getElementById('issues-list');
    const targetUrlDisplay = document.getElementById('target-url');
    const historyList = document.getElementById('history-list');

    // Cargar historial al inicio
    loadHistory();

    urlForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const url = urlInput.value.trim();
        if (!url) return;

        // Reset UI
        urlError.classList.add('hidden');
        loadingSection.classList.remove('hidden');
        resultsSection.classList.add('hidden');
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
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error en la auditoría');
            }

            const data = await response.json();
            displayResults(data, url);
            loadHistory(); // Recargar historial tras nueva auditoría
        } catch (error) {
            urlError.textContent = `Error técnico: ${error.message}`;
            urlError.classList.remove('hidden');
            console.error('Audit Error:', error);
        } finally {
            loadingSection.classList.add('hidden');
        }
    });

    function displayResults(data, url) {
        resultsSection.classList.remove('hidden');
        targetUrlDisplay.textContent = url;
        scoreValue.textContent = data.score;
        summaryText.textContent = data.summary;

        if (data.issues.length === 0) {
            issuesList.innerHTML = `
                <div class="col-span-full bg-green-900/20 border border-green-800 p-8 rounded-xl text-center">
                    <p class="text-green-400 font-bold text-lg">✓ No se encontraron barreras críticas automáticas.</p>
                    <p class="text-green-600 text-sm mt-2 font-mono uppercase tracking-widest">Estado: Accesibilidad Optimizada</p>
                </div>
            `;
        } else {
            data.issues.forEach(issue => {
                const card = createIssueCard(issue);
                issuesList.appendChild(card);
            });
        }
        
        // Accesibilidad: Mover foco al inicio de los resultados
        resultsSection.scrollIntoView({ behavior: 'smooth' });
        setTimeout(() => {
            document.getElementById('results-heading').focus();
        }, 500);
    }

    function createIssueCard(issue) {
        const div = document.createElement('div');
        const severityColors = {
            'CRITICAL': 'border-red-600 bg-red-900/10 text-red-400',
            'WARNING': 'border-yellow-600 bg-yellow-900/10 text-yellow-400',
            'INFO': 'border-blue-600 bg-blue-900/10 text-blue-400'
        };
        const colorClass = severityColors[issue.severity] || severityColors.INFO;

        div.className = `p-6 rounded-xl border-l-4 ${colorClass} bg-[#0F172A] border-y border-r border-gray-800 flex flex-col gap-3 transition-transform hover:scale-[1.02]`;
        div.setAttribute('role', 'listitem');
        
        div.innerHTML = `
            <div class="flex justify-between items-start">
                <span class="text-[10px] font-black uppercase tracking-[0.2em] px-2 py-1 rounded bg-current/10 border border-current/20">
                    ${issue.severity}
                </span>
                <span class="font-mono text-[10px] text-gray-500 uppercase">${issue.type}</span>
            </div>
            <h3 class="font-bold text-rs-text leading-tight">${issue.message}</h3>
            <div class="mt-auto">
                <p class="text-xs text-gray-500 mb-1 font-mono">Elemento afectado:</p>
                <code class="block text-[10px] bg-black/40 p-2 rounded border border-gray-800 overflow-x-auto whitespace-pre font-mono text-rs-orange">
                    ${escapeHtml(issue.element)}
                </code>
            </div>
        `;
        return div;
    }

    async function loadHistory() {
        try {
            const response = await fetch('/api/history?limit=10');
            if (!response.ok) return;
            
            const history = await response.json();
            if (history.length === 0) {
                historyList.innerHTML = '<p class="text-gray-600 italic">No hay registros de auditoría.</p>';
                return;
            }

            historyList.innerHTML = '';
            history.forEach(item => {
                const div = document.createElement('div');
                div.className = 'flex items-center justify-between p-4 bg-[#0F172A] border border-gray-800 rounded-lg hover:border-gray-600 transition-colors group';
                div.setAttribute('role', 'listitem');
                
                const date = new Date(item.created_at).toLocaleDateString('es-PY', {
                    day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit'
                });

                div.innerHTML = `
                    <div class="flex items-center gap-4 truncate">
                        <div class="w-10 h-10 rounded bg-gray-800 flex items-center justify-center font-black text-rs-orange text-xs">
                            ${item.score}
                        </div>
                        <div class="truncate">
                            <p class="text-sm font-bold truncate group-hover:text-rs-orange transition-colors">${item.url}</p>
                            <p class="text-[10px] text-gray-500 font-mono uppercase tracking-widest">${date}</p>
                        </div>
                    </div>
                    <button 
                        onclick="document.getElementById('url-input').value='${item.url}'; document.getElementById('audit-btn').click();"
                        class="text-[10px] font-black uppercase tracking-tighter text-gray-400 hover:text-white"
                        aria-label="Re-auditar ${item.url}"
                    >
                        Re-auditar
                    </button>
                `;
                historyList.appendChild(div);
            });
        } catch (error) {
            console.error('History Load Error:', error);
            historyList.innerHTML = '<p class="text-red-900/50 text-xs">Error al cargar historial.</p>';
        }
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
});
