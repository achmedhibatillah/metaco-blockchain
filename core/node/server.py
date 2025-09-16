import threading
import requests
from flask import Flask, request, jsonify  # type: ignore

from core.node.controllers.peers import PeersManagement
from core.node.controllers.block_management import BlockManagement
from core.node.controllers.mining_difficulty import MiningDifficulty

class Server:
    def __init__(self, port=8050):
        self.port = port
        self.obj_block_management = BlockManagement()
        self.obj_mining_difficulty = MiningDifficulty()

    def start(self):
        app = Flask(__name__)

        @app.route("/nodestatus", methods=["GET"])
        def get_nodestatus():
            return jsonify({
                "status": "hi, i'am a metaco node!"
            })
        
        @app.route("/nb", methods=["POST"])
        def nb():
            block = requests.get_json()

            block_hash = self.obj_block_management.block_hash({k:v for k,v in block.items() if k!="hs"})
            target = self.obj_mining_difficulty.get_difficulty()

            if block.get("hs") != block_hash or block_hash >= target:
                return jsonify({"status": "ivhs"}), 400

        if not self.port:
            raise RuntimeError("[!] No available ports.")
        
        peersmanagement = PeersManagement(self.port)
        threading.Thread(target=peersmanagement.loop_peers, daemon=True).start()
        
        print(f"Node is running on http://127.0.0.1:{self.port}")
        app.run(port=self.port)