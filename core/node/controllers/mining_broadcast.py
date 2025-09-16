import os
import requests

from core.node.controllers.peers import PeersManagement

class MiningBroadcast:
    def __init__(self):
        self.obj_peers_management = PeersManagement()
        self.NODES = self.obj_peers_management.get_peers()

    def broadcasting_node(self, block):
        for node in self.NODES:
            try:
                requests.post(f"http://127.0.0.1:{node}/nb", json=block, timeout=2)
            except:
                pass