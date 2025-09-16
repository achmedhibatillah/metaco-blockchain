import os
import json
from core.node.controllers.block_management import BlockManagement

class StateManagement:
    def __init__(self):
        self.STATE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "state")
        self.STATE_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "state", "state.json")
        self.GENESIS_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "genesis", "genesis.json")

        block_management = BlockManagement()
        self.BLOCKCHAIN = block_management.get_blockchain()
        self.STATE = self.state_load()
        if not self.STATE and self.BLOCKCHAIN:
            self.state_rebuild()

    @staticmethod
    def _normalize(addr):
        return str(addr).lower().strip() if addr else None
    
    def state_load(self):
        if os.path.exists(self.STATE_FILE):
            with open(self.STATE_FILE, "r") as f:
                raw = json.load(f)
            return [{"adr": self._normalize(x["adr"]), "stt": int(x["stt"])} for x in raw]
        elif os.path.exists(self.GENESIS_FILE):
            with open(self.GENESIS_FILE, "r") as f:
                genesis = json.load(f)
            norm = [{"adr": self._normalize(x["adr"]), "stt": int(x["stt"])} for x in genesis]
            os.makedirs(self.STATE_DIR, exist_ok=True)
            with open(self.STATE_FILE, "w") as f:
                json.dump(norm,f)
            return norm
        return []

    def state_rebuild(self):
        state_dict = {}

        block_management = BlockManagement()
        blockchain = block_management.get_blockchain()

        for block in blockchain:
            for tx in block.get("tx", []):
                i = self._normalize(tx.get("i"))
                o = self._normalize(tx.get("o"))
                amt = int(tx.get("a", 0))
                state_dict.setdefault(i,0)
                state_dict.setdefault(o,0)
                state_dict[i] -= amt
                state_dict[o] += amt
        self.STATE = [{"adr":a, "stt":b} for a,b in state_dict.items()]
        self.state_save()

    def state_save(self):
        os.makedirs(self.STATE_DIR, exist_ok=True)
        with open(self.STATE_FILE, "w") as f:
            json.dump(self.STATE, f)

    def state_update(self, block):
        state = self.get_state_disc()
        for tx in block.get("tx", []):
            i = self._normalize(tx.get("i"))
            o = self._normalize(tx.get("o"))
            amt = int(tx.get("a",0))
            state.setdefault(i,0)
            state.setdefault(o,0)
            if state[i] < amt:
                continue
            state[i] -= amt
            state[o] += amt
        self.STATE = [{"adr":a,"stt":b} for a,b in state.items()]
        self.state_save()

    def get_state_disc(self):
        return {self._normalize(x["adr"]): int(x["stt"]) for x in self.STATE}