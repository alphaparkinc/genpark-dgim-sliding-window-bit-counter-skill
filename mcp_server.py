import sys
import json
from client import DGIMCounter

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "estimate":
        dgim = DGIMCounter(params.get("window", 100))
        for b in params.get("bits", []):
            dgim.update(b)
        return {"estimated_count": dgim.estimate_count(params.get("k", 50))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
