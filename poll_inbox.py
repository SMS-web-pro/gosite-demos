#!/usr/bin/env python3
"""Poll inbox for prospect responses."""
import imaplib, email, json, os, sys
from datetime import datetime, timezone, timedelta

TARGET_SENDERS = ["info@denvertotalpt.com", "info@tagcommercialbroker.com", "mch@mchdumbo.com", "info@whitecoatbeauty.com"]
IMAP_HOST = os.environ.get("IMAP_HOST", "imap.gmail.com")
IMAP_USER = os.environ.get("IMAP_USER", "siteup.services@gmail.com")
IMAP_PASS = os.environ.get("IMAP_PASS", "")
STATE_FILE = "/home/hermes/.hermes/cron/poll_state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"last_uid": 0, "processed": []}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def main():
    if not IMAP_PASS:
        print(json.dumps({"error": "IMAP_PASS not set"}))
        sys.exit(1)

    try:
        mail = imaplib.IMAP4_SSL(IMAP_HOST)
        mail.login(IMAP_USER, IMAP_PASS)
        mail.select("INBOX")

        state = load_state()
        since = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%d-%b-%Y")
        typ, data = mail.search(None, f'(UNSEEN SINCE {since})')

        new_responses = []
        for num in data[0].split():
            typ, msg_data = mail.fetch(num, "(RFC822)")
            raw = msg_data[0][1]
            msg = email.message_from_bytes(raw)
            sender = msg.get("From", "")
            subject = msg.get("Subject", "")
            uid = num.decode()

            if uid in state["processed"]:
                continue

            for target in TARGET_SENDERS:
                if target in sender.lower():
                    new_responses.append({
                        "from": sender,
                        "subject": subject,
                        "uid": uid,
                        "date": msg.get("Date", "")
                    })
                    break

            state["processed"].append(uid)

        state["last_uid"] = max(state["processed"]) if state["processed"] else 0
        save_state(state)
        mail.logout()

        if new_responses:
            print(json.dumps({"responses": new_responses, "count": len(new_responses)}))
        else:
            print(json.dumps({"responses": [], "count": 0}))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
