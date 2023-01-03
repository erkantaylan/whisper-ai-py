import json
import socketserver
from http.server import BaseHTTPRequestHandler

from typing import Tuple

from whisper_helper import WhisperHelper

whisper = WhisperHelper()


class WhisperServer(BaseHTTPRequestHandler):
    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer) -> None:
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.succes_response()
        self.wfile.write(bytes('POST audio path', "utf-8"))

    def do_POST(self):
        self.succes_response()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post = post_data.decode('utf-8')
        result = whisper.get_text(post)
        self.wfile.write(bytes(json.dumps(result), "utf-8"))

    def succes_response(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
