import requests

def req(url,params,timeout):
    try:
        resp = requests.get(url,params=params,timeout=timeout)
        resp.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    return resp