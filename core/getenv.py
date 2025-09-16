import os
from dotenv import load_dotenv  # type: ignore

def get_env():
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

    ports = os.getenv("NODE_PORTS", "")
    PORTS = [int(p.strip()) for p in ports.split(",") if p.strip()]

    env = {
        "nodes": PORTS
    }

    return env
