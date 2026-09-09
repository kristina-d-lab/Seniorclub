#!/usr/bin/env python3
"""Local preview with the same URL rules as vercel.json.

    python3 preview.py            -> http://localhost:8000/

/fi/            -> fi/index.html
/fi/mumili/     -> fi/mumili.html
/fi/mumili      -> redirect to /fi/mumili/
missing page    -> 404.html
"""
import os, sys, http.server, socketserver, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_GET(self):
        path = urllib.parse.urlsplit(self.path).path
        fs = os.path.join(ROOT, path.lstrip("/"))
        if os.path.isfile(fs):
            return super().do_GET()
        parts = path.strip("/").split("/")
        if parts and parts[0] in ("fi", "en", "ru"):
            if not path.endswith("/"):
                self.send_response(308); self.send_header("Location", path + "/"); self.end_headers(); return
            slug = parts[1] if len(parts) > 1 and parts[1] else "index"
            cand = os.path.join(ROOT, parts[0], slug + ".html")
            if os.path.isfile(cand):
                self.path = f"/{parts[0]}/{slug}.html"
                return super().do_GET()
        if os.path.isdir(fs) and os.path.isfile(os.path.join(fs, "index.html")):
            return super().do_GET()
        self.path = "/404.html"
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(open(os.path.join(ROOT, "404.html"), "rb").read())

    def log_message(self, *a):
        pass


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), H) as httpd:
    print(f"Preview: http://localhost:{PORT}/  (Ctrl+C to stop)")
    httpd.serve_forever()
