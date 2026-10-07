import requests

def req(url,params,timeout):
    try:
        resp = requests.get(url,params=params,timeout=timeout)
    except requests.exceptions.RequestException:
        return False
    return resp