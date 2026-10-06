#!/usr/bin/env python3
import imaplib, ssl

ctx = ssl.create_default_context()
host = open('/home/hermes/.hermes/secrets/IMAP_HOST').read().strip()
port = int(open('/home/hermes/.hermes/secrets/IMAP_PORT').read().strip())
user = open('/home/hermes/.hermes/secrets/IMAP_USER').read().strip()
pwd = open('/home/hermes/.hermes/secrets/IMAP_PASS').read().strip()

print(f"connecting to {host}:{port}...", flush=True)
mail = imaplib.IMAP4_SSL(host, port, timeout=10, ssl_context=ctx)
print("connected, logging in...", flush=True)
mail.login(user, pwd)
print("logged in", flush=True)
mail.select('INBOX')
print("inbox selected", flush=True)
status, data = mail.search(None, 'UNSEEN')
print(f"unseen count: {len(data[0].split()) if data[0] else 0}", flush=True)
mail.logout()
