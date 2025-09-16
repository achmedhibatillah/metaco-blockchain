import threading
import requests
from flask import Flask, request, jsonify  # type: ignore

from core.node.controllers.peers import PeersManagement

class Server:
    def __init__(self, port=8050):
        self.port = port

    def start(self):
        app = Flask(__name__)

        @app.route("/nodestatus", methods=["GET"])
        def get_nodestatus():
            return jsonify({
                "status": "hi, i'am a metaco node!"
            })
        
        # @app.route("/receiveblock", methods=["POST"])
        # def receive_block():
        #     block = requests.get_json()

        if not self.port:
            raise RuntimeError("[!] No available ports.")
        
        peersmanagement = PeersManagement(self.port)
        threading.Thread(target=peersmanagement.loop_peers, daemon=True).start()
        
        print(f"Node is running on http://127.0.0.1:{self.port}")
        app.run(port=self.port)