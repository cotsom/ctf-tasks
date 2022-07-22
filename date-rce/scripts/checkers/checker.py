import sys
import requests

host = sys.argv[1]
port = sys.argv[2]

def ping():
    r = requests.get(f"http://{host}:{port}/ping", timeout=2)
    if r.status_code == 200:
        if r.text == "pong":
            print(1)
            return 1
    return 0

if __name__ == '__main__':
    ping()
