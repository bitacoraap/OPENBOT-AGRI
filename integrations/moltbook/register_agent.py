#!/usr/bin/env python3
"""Register OPENBOT-AGRI on Moltbook. Run LOCALLY. Never commit credentials."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API = "https://www.moltbook.com/api/v1/agents/register"
NAME = "OpenbotAgri"
DESCRIPTION = (
    "Open-source human-and-AI collaboration experiment: design, source and test "
    "an agricultural inspection robot. Public engineering challenges: "
    "https://github.com/bitacoraap/OPENBOT-AGRI"
)

def main():
    payload = json.dumps({"name": NAME, "description": DESCRIPTION}).encode()
    req = Request(API, data=payload, headers={"Content-Type":"application/json"}, method="POST")
    try:
        with urlopen(req, timeout=20) as res:
            result = json.load(res)
    except HTTPError as exc:
        print("Registration failed:", exc.code, exc.read().decode(errors="replace")[:800])
        return
    agent = result.get("agent", result)
    key = agent.get("api_key")
    if not key:
        print("Registration response had no API key. Check Moltbook documentation.")
        return
    dest = Path.home() / ".config" / "openbot-agri" / "moltbook.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(dest, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump({"api_key":key, "agent_name":NAME}, f)
    print("Saved credentials privately in:", dest)
    print("Claim URL:", agent.get("claim_url"))
    print("Verification code:", agent.get("verification_code"))
    print("Never upload credentials or paste them into a public issue.")

if __name__ == "__main__":
    main()
