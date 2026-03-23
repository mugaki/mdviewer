#!/usr/bin/env python3
"""
Lightweight Markdown Viewer
Usage: python viewer.py
"""

import os
import sys
import socketserver
import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path

import pystray
from PIL import Image

HOST = "127.0.0.1"
PORT = 8765
URL  = f"http://{HOST}:{PORT}"

# PyInstaller で --onefile ビルドした場合は sys._MEIPASS に展開される
if getattr(sys, "frozen", False):
    STATIC_DIR = Path(getattr(sys, "_MEIPASS"))
else:
    STATIC_DIR = Path(__file__).parent


# ---- Tray icon image ----
def _make_tray_image():
    ico_path = STATIC_DIR / "icon.ico"
    img = Image.open(ico_path)
    img = img.convert("RGBA")
    return img


# ---- HTTP Server ----
class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    daemon_threads = True


class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parsed = urlparse(self.path)
        path   = parsed.path

        if path in ("/", "/index.html"):
            self._serve(STATIC_DIR / "index.html", "text/html; charset=utf-8")

        elif path.startswith("/vendor/"):
            rel   = path.lstrip("/")
            fpath = STATIC_DIR / rel
            try:
                fpath.resolve().relative_to((STATIC_DIR / "vendor").resolve())
            except ValueError:
                self._error(403)
                return
            ext  = fpath.suffix.lower()
            mime = {".js":  "application/javascript; charset=utf-8",
                    ".css": "text/css; charset=utf-8"}.get(ext, "application/octet-stream")
            self._serve(fpath, mime)

        elif path == "/icon.ico":
            self._serve(STATIC_DIR / "icon.ico", "image/x-icon")

        elif path == "/quit":
            msg = b"Goodbye"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)
            threading.Timer(0.3, _shutdown).start()

        else:
            self._error(404)

    def _serve(self, fpath: Path, mime: str):
        if not fpath.is_file():
            self._error(404)
            return
        body = fpath.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        try:
            self.wfile.write(body)
        except BrokenPipeError:
            pass

    def _error(self, code: int):
        msg = b"Not Found" if code == 404 else b"Forbidden"
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(msg)))
        self.end_headers()
        try:
            self.wfile.write(msg)
        except BrokenPipeError:
            pass


# ---- Shutdown ----
_tray   = None
_server = None

def _shutdown():
    if _tray:
        _tray.stop()
    if _server:
        threading.Thread(target=_server.shutdown, daemon=True).start()


# ---- Main ----
def main():
    global _tray, _server

    server = ThreadingHTTPServer((HOST, PORT), Handler)
    _server = server
    threading.Thread(target=server.serve_forever, daemon=True).start()

    webbrowser.open(URL)

    icon_img = _make_tray_image()
    menu = pystray.Menu(
        pystray.MenuItem("ブラウザで開く", lambda icon, item: webbrowser.open(URL), default=True),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("終了", lambda icon, item: _shutdown()),
    )
    tray = pystray.Icon("mdviewer", icon_img, "mdviewer", menu)
    _tray = tray
    tray.run()          # blocks until tray.stop()
    server.shutdown()


if __name__ == "__main__":
    main()
