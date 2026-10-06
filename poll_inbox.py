#!/usr/bin/env python3
"""Poll inbox for new emails from target campaign senders."""
import imaplib, email, json, argparse, os, sys
from datetime import datetime, timezone

STATE_FILE = "/home/hermes/.hermes/state/inbox_seen.json"
TARGET_SENDERS = {
    "denver-total-pt": "info@denvertotalpt.com",
    "tagg": "info@tagcommercialbroker.com",
    "mcollection-home": "mch@mchdumbo.com",
    "white-coat-beauty": "info@whitecoatbeauty.com",
}
SECRETS = "/home/hermes/.hermes/secrets"

def load_seen():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"seen": [], "last_run": None}

def save_seen(data):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def read_secret(name):
    p = os.path.join(SECRETS, name)
    if os.path.exists(p):
        with open(p) as f:
            return f.read().strip()
    return ""

def connect_imap():
    host = read_secret("IMAP_HOST") or "imap.gmail.com"
    port = int(read_secret("IMAP_PORT") or "993")
    user = read_secret("IMAP_USER")
    pwd = read_secret("IMAP_PASS")  # Keep spaces as-is
    mail = imaplib.IMAP4_SSL(host, port, timeout=15)
    mail.login(user, pwd)
    mail.select("INBOX")
    return mail

def fetch_new(mail, seen_ids):
    status, data = mail.search(None, "UNSEEN")
    if status != "OK":
        return []
    new = []
    for num in data[0].split():
        msg_id = f"INBOX:{num.decode()}"
        if msg_id in seen_ids:
            continue
        status2, msg_data = mail.fetch(num, "(RFC822)")
        if status2 != "OK":
            continue
        raw = msg_data[0][1]
        msg = email.message_from_bytes(raw)
        sender = msg.get("From", "")
        subject = msg.get("Subject", "")
        addr = sender
        if "<" in sender:
            addr = sender.split("<")[1].split(">")[0].strip().lower()
        else:
            addr = sender.strip().lower()
        new.append({"id": msg_id, "num": num.decode(), "from": sender, "address": addr, "subject": subject})
    return new

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--peek", action="store_true")
    parser.add_argument("--mark", action="store_true")
    args = parser.parse_args()

    try:
        mail = connect_imap()
    except Exception as e:
        print(f"IMAP connection failed: {e}", file=sys.stderr)
        sys.exit(1)

    seen = load_seen()
    seen_ids = set(seen.get("seen", []))
    messages = fetch_new(mail, seen_ids)

    target_msgs = []
    for m in messages:
        for slug, addr in TARGET_SENDERS.items():
            if m["address"] == addr.lower():
                m["slug"] = slug
                target_msgs.append(m)
                break

    if args.peek:
        if not target_msgs:
            print("aucune nouvelle réponse")
        else:
            for m in target_msgs:
                print(f"[{m['slug']}] {m['from']} — {m['subject']}")

    if args.mark:
        for m in messages:
            seen_ids.add(m["id"])
        seen["seen"] = sorted(seen_ids)
        seen["last_run"] = datetime.now(timezone.utc).isoformat()
        save_seen(seen)
        print(f"marked {len(messages)} messages as seen")

    mail.logout()

if __name__ == "__main__":
    main()
