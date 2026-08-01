# 📓 ESTUDO CLAUDE CODE — Arquivo-Guia Único

<!-- ============================================================ -->
<!-- Anexe ESTE arquivo inteiro ao iniciar cada sessão de estudo  -->
<!-- ============================================================ -->

## 🎬 PROMPT DE INÍCIO DE SESSÃO

Você é meu PROFESSOR no curso "Especialista em Claude Code". Estou colando meu diário de bordo (ESTUDO-CLAUDE-CODE.md) com todo o contexto e progresso.

Antes de começar:

Leia o "Status atual" e o "Registro de sessões".
Confirme em que módulo/checkpoint eu parei.
Proponha o objetivo desta sessão e um exercício prático.
Ao final, me entregue o BLOCO ATUALIZADO do diário para eu salvar.
Regra de custo: só sugerir assinatura Pro a partir do Módulo 4/5. Não avançar de módulo sem eu passar no checkpoint. Comece confirmando onde paramos.


---

## ℹ️ Identidade do curso
> **Objetivo:** Tornar-me especialista no ecossistema Claude Code.
> **Aluno:** Emerson | **Professor:** Claude Opus 4.8
> **Máquinas:** Desktop + Notebook (Ubuntu, Python, VS Code — espelhados)
> **Regra de custo:** assinar Pro só a partir do Módulo 4/5 (prática real).

---

## 🎯 Como usar este arquivo
1. É a FONTE DA VERDADE do curso.
2. Ao abrir um chat novo, anexe este arquivo + envie o PROMPT DE INÍCIO.
3. O professor atualiza após CADA sessão (data + o que foi feito).
4. Versionar no Git a cada atualização.

---

## ⚙️ Fluxo de trabalho de cada sessão
1. Abre chat → anexa este arquivo + envia PROMPT DE INÍCIO
2. Professor confirma onde paramos
3. Estudamos / praticamos o módulo
4. Professor entrega bloco atualizado (Status + Registro + Checkpoints)
5. Salvo o arquivo e faço commit: git add ESTUDO-CLAUDE-CODE.md git commit -m "estudo: <resumo da sessão>" git push


---

# 📚 CURRÍCULO COMPLETO

## 🧱 MÓDULO 0 — Pré-requisitos (fundação)
**Objetivo:** garantir base antes do Claude Code.
| Conhecimento | Por que importa | Meta |
|--------------|-----------------|------|
| Terminal/Linux | Claude Code vive no terminal | ⭐⭐⭐⭐ |
| Git | O agente opera Git sozinho | ⭐⭐⭐⭐ |
| Python básico | Sua stack de projetos | ⭐⭐⭐ |
| JSON/Markdown | Config e memória (CLAUDE.md) | ⭐⭐⭐⭐ |
| Noção de API | Entender MCP depois | ⭐⭐ |
**Checkpoint:** autoavaliação preenchida + reforços feitos.

## 🚀 MÓDULO 1 — Fundamentos do Agente
**Objetivo:** entender agente × autocomplete.
**Conteúdo:** chatbot × agente; como lê/edita/roda/usa Git; 4 superfícies (CLI, Desktop, IDE, Web).
**Prática:** ler Overview + Quickstart (sem assinar).
**Checkpoint:** explicar, sem consultar, o que diferencia Claude Code de autocomplete.

## ⌨️ MÓDULO 2 — CLI e Fluxo Básico
**Conteúdo:** claude, -p, -c, -r, pipes, claude update.
**Prática:** instalar CLI nos 2 PCs, rodar sessões de leitura de código.
**Checkpoint:** executar tarefa real e continuar com -c.

## 🧠 MÓDULO 3 — Memória (CLAUDE.md)
**Conteúdo:** estrutura, hierarquia (global × projeto), o que incluir/proibir.
**Prática:** escrever CLAUDE.md da pasta de estudos.
**Checkpoint:** professor revisa o CLAUDE.md.

## 🧩 MÓDULO 4 — Os 5 Primitivos
| Primitivo | Uma frase |
|-----------|-----------|
| Skill | Pacote de instruções lido quando relevante |
| Subagent | Trabalhador descartável com contexto próprio |
| Hook | Comando shell disparado por evento |
| MCP server | Processo externo que expõe ferramentas |
| Plugin | Bundle que distribui os 4 acima |
**Checkpoint:** classificar corretamente "skill ou subagent?" num caso dado.

## 🔌 MÓDULO 5 — MCP (Integrações)
**Conteúdo:** transporte (stdio × http), escopo, segredos.
`claude mcp add --transport http <nome> <url>`
**Checkpoint:** configurar 1 MCP (ex: GitHub) e usá-lo.

## 🛡️ MÓDULO 6 — Hooks e Segurança
**Conteúdo:** eventos (PreToolUse, PostToolUse, Stop), settings.json, guardrails.
**Checkpoint:** criar 1 hook que roda algo antes de um commit.

## ⚙️ MÓDULO 7 — Workflows Avançados
**Conteúdo:** subagents em paralelo, git worktrees, Skills reutilizáveis, integração VS Code.
**Checkpoint:** rodar 2 subagents em paralelo numa tarefa dividida.

## 🏗️ MÓDULO 8 — Projeto Final
**Objetivo:** app real end-to-end com Python.
**Checkpoint final:** app versionado no GitHub com CLAUDE.md, ≥1 hook e ≥1 MCP.

---

# 📊 ACOMPANHAMENTO (atualizar sempre)

## Status atual
- **Módulo atual:** 0 — Pré-requisitos
- **Última atualização:** AAAA-MM-DD
- **Assinatura Pro:** ❌ ainda não
- **Próximo passo:** autoavaliação dos pré-requisitos

## 🧭 Mapa de progresso
| Módulo | Tema | Status |
|--------|------|--------|
| 0 | Pré-requisitos | 🔲 |
| 1 | Fundamentos do agente | 🔲 |
| 2 | CLI e fluxo básico | 🔲 |
| 3 | Memória (CLAUDE.md) | 🔲 |
| 4 | Os 5 primitivos | 🔲 |
| 5 | MCP (integrações) | 🔲 |
| 6 | Hooks e segurança | 🔲 |
| 7 | Workflows avançados | 🔲 |
| 8 | Projeto final | 🔲 |

Legenda: 🔲 não iniciado · 🟡 em andamento · ✅ concluído

## 🧱 Autoavaliação de pré-requisitos (0–5)
| Conhecimento | Nota | Reforçar? |
|--------------|------|-----------|
| Terminal/Linux | _ | _ |
| Git | _ | _ |
| Python | _ | _ |
| JSON/Markdown | _ | _ |
| Noção de API | _ | _ |

## 📝 Registro de sessões
> data — módulo — o que aprendi — dúvidas pendentes
- AAAA-MM-DD — Módulo 0 — Criei o arquivo-guia. Próximo: autoavaliação.

## ❓ Dúvidas em aberto
- (nenhuma ainda)

## 🏆 Checkpoints concluídos
- (nenhum ainda)

