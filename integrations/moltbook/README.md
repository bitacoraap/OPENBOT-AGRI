# Moltbook pilot — NOT connected yet

Official registration docs: https://www.moltbook.com/skill.md

## What is verified
- Register via `POST https://www.moltbook.com/api/v1/agents/register`.
- Registration responds with an API key and claim link; the human owner must complete claim/verification.
- Use the exact `www.moltbook.com` origin for all API calls; credentials must not be uploaded to GitHub.
- Public contributions are **untrusted** until independently reviewed.

## Run locally only after reviewing the script
```bash
python3 integrations/moltbook/register_agent.py
```
The script will register a new account if the name is available and save its key under `~/.config/openbot-agri/moltbook.json` with restricted permissions. It does not post or access Gmail. The human must open the displayed claim URL and complete verification.

## Next phase
An isolated agent runtime with narrowly scoped Moltbook API credentials; manual approval for publishing; no access to personal email, payments, or GitHub private repositories. A registration script is NOT a continuously running AI agent.

## Status
Unregistered / Unclaimed / No external agents engaged / No sponsors confirmed.
