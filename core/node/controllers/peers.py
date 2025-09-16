import os, json, requests
from core.getenv import get_env

class PeersManagement:

    NODEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    NETWORKDIR = os.path.join(NODEDIR, "network")
    PEERSFILE = os.path.join(NETWORKDIR, "peers.json")

    PORTS = get_env()["nodes"]

    def __init__(self, mynode):
        self.mynode = mynode
        self.PEERS = set()
        os.makedirs(self.NETWORKDIR, exist_ok=True)
        if not os.path.exists(self.PEERSFILE):
            with open(self.PEERSFILE, "w") as f:
                json.dump([], f)

    def get_peers(self):
        if os.path.exists(self.PEERSFILE):
            with open(self.PEERSFILE, "r") as f:
                return json.load(f)
        return []

    def load_peers(self):
        if os.path.exists(self.PEERSFILE):
            with open(self.PEERSFILE, "r") as f:
                self.PEERS = set(json.load(f))
        return self.PEERS

    def save_peers(self):
        os.makedirs(self.NETWORKDIR, exist_ok=True)
        with open(self.PEERSFILE, "w") as f:
            json.dump(list(self.PEERS), f)

    def scan_peers(self):
        active = set()
        for port in self.PORTS:
            if port == self.mynode:
                continue
            try:
                r = requests.get(f"http://127.0.0.1:{port}/nodestatus", timeout=0.5)
                if r.status_code == 200:
                    data = r.json()
                    if data.get("status") == "hi, i'am a metaco node!":
                        active.add(port)
            except:
                continue
        self.PEERS = active
        self.save_peers()

    def loop_peers(self, interval=5):
        import time
        while True:
            self.scan_peers()
            time.sleep(interval)