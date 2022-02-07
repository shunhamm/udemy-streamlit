import requests
import json

def main():
    url = 'https://hdjbdy.deta.dev/'
    data = {
        'x': 1.2,
        'y': 3.0
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())
if __name__=='__main__':
    main()


