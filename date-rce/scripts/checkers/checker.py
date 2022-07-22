import sys
import requests

host = sys.argv[1]
port = sys.argv[2]

def ping():
    r = requests.get(f"http://{host}:{port}/ping", timeout=2)
    if r.status_code == 200:
        if r.text == "pong":
            return 1
    return 0

def get():
    r = requests.post(f"http://{host}:{port}", data={"date": "date"})
    if r.status_code == 200:
        return 1
    return 0

if __name__ == '__main__':
    if (ping() and get()):
        print(1)