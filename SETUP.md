# 🚀 Setup Ambiente Claude Code — Progresso

> Fonte da verdade para manter Desktop e Notebook idênticos.
> Colar este arquivo no início de cada sessão de estudo.

**Última atualização:** 2026-08-01
**Repositório:** github.com/myoyoda-dev/Projetos

---

## 📋 Checklist por máquina

| Etapa                     | Desktop (Yuki-PC) | Notebook (Yuki-Note) | Versão / Notas       |
|---------------------------|:-----------------:|:--------------------:|----------------------|
| Ubuntu                    |        [x]        |         [x]          | Note: 26.04 LTS      |
| Python                    |        [x]        |         [x]          | 3.14.4 (ambos)       |
| VS Code                   |        [x]        |         [x]          | Note: 1.131.0        |
| Git + GitHub              |        [x]        |         [x]          | 2.53.0 (ambos)       |
| VS Code Settings Sync     |        [x]        |         [x]          | login GitHub ✔       |
| Extensões VS Code         |        [x]        |         [x]          | 9 extensões (ambos)  |
| nvm                       |        [x]        |         [x]          | 0.40.1 (ambos)       |
| Node.js (via nvm)         |        [x]        |         [x]          | v24.18.1 (ambos)     |
| npm                       |        [x]        |         [x]          | 12.0.2 (ambos)       |
| Claude Code               |        [x]        |         [x]          | 2.1.220 (ambos)      |
| Autenticação Claude       |        [x]        |         [ ]          | Note: aguarda assin. |

---

## 🔧 Versões atuais

### Desktop (Yuki-PC)
node -v     -> v24.18.1
npm -v      -> 12.0.2
python3     -> Python 3.14.4
claude      -> 2.1.220 (Claude Code)
git         -> git version 2.53.0

### Notebook (Yuki-Note)
ubuntu      -> 26.04 LTS
python3     -> Python 3.14.4
git         -> git version 2.53.0
vscode      -> 1.131.0
nvm         -> 0.40.1
node -v     -> v24.18.1
npm -v      -> 12.0.2
claude      -> 2.1.220 (Claude Code) — login pendente

---

## 📝 Configurações aplicadas
- Git user.name: myoyoda-dev
- Git user.email: profemersonarashiro@gmail.com
- Método de auth GitHub: HTTPS (remote via https://github.com/myoyoda-dev/Projetos.git)
- Claude Code tema: Dark mode
- VS Code: idioma em Inglês (padronizado nos dois PCs)
- VS Code Settings Sync: conflitos resolvidos com "Accept Remote Settings"

---

## 🧩 Extensões VS Code (padronizadas nos 2 PCs)
- eamodio.gitlens — Git avançado
- ms-python.black-formatter — formatador Black
- ms-python.debugpy — debugger Python
- ms-python.isort — ordenar imports
- ms-python.python — suporte Python
- ms-python.vscode-pylance — language server
- ms-python.vscode-python-envs — gerenciador de ambientes
- oderwat.indent-rainbow — indentação colorida
- usernamehw.errorlens — erros inline

---

## 🐍 Dependências Python (requirements.txt)
- black==26.5.1 (formatador)
- click, mypy_extensions, packaging, pathspec, platformdirs, pytokens (deps do Black)
- certifi, charset-normalizer, idna, requests, urllib3

---

## ⏭️ Próximos passos
- [ ] Autenticar Claude no Notebook (após contratar assinatura — rodar `claude` no diretório do projeto)
- [ ] Investigar por que o Settings Sync não sincronizou extensões automaticamente

---

## 📓 Histórico de sessões
- **2026-08-01 (Desktop):** SETUP.md versionado (commit ea7a2ab). Desktop 100% pronto — Claude autenticado, tema Dark.
- **2026-08-01 (Notebook):** Repositório sincronizado via git pull. Diagnóstico: Ubuntu 26.04, Python 3.14.4, Git 2.53.0 e VS Code 1.131.0 já OK.
- **2026-08-01 (Notebook):** Instalados nvm 0.40.1, Node v24.18.1, npm 11.16.0 e Claude Code 2.1.220. Ambiente agora idêntico ao Desktop. Login do Claude adiado até contratar assinatura. Tema Dark selecionado.
- **2026-08-01 (Notebook):** VS Code Settings Sync ativado e sincronizado com o Desktop. Conflitos resolvidos com "Accept Remote Settings". Idioma mantido em Inglês.
- **2026-08-01 (Notebook):** Git confirmado (user.name/email/remote). Adicionado Black e deps ao requirements.txt (commit f3abc5a). npm atualizado 11.16.0 -> 12.0.2. Arquivo hello.py de teste descartado com git restore.
- **2026-08-01 (Desktop):** npm atualizado 11.16.0 -> 12.0.2. Ambientes agora 100% idênticos. Conflito no git pull resolvido com git checkout (descartada versão local antiga do SETUP.md).
- **2026-08-01 (Desktop):** Instaladas 5 extensões que faltavam (GitLens, Black, isort, indent-rainbow, ErrorLens) e removido language-pack-pt-br. Extensões agora idênticas ao Notebook (9 no total), idioma em inglês.
