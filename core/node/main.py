import os
import socket
from flask import Flask, request, jsonify  # type: ignore
from dotenv import load_dotenv  # type: ignore

from core.node.server import Server
from core.node.mining import Mining

class Main:

    def __init__(self):
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

        ports = os.getenv("NODE_PORTS", "")
        self.ports = [int(p.strip()) for p in ports.split(",") if p.strip()]

    def start(self):
        server = Server(self.get_port())
        server.start()

    def mining(self):
        mining = Mining()
        mining.index()

    def get_port(self):
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(("127.0.0.1", port))
            sock.close()
            if result != 0:
                return port
        return None
