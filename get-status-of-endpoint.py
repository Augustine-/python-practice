import requests

endpoint = "http://example.com/api/ep"

resp = requests.get(endpoint)
resp.raise_for_status()

data  = resp.json()

urls = data.get('urls', [])

def check_url_status(url):
    try:
        res = requests.get(url)
        return res.status_code
    except requests.RequestException as e:
        return f"Error: {e}"

for url in urls:
    status = check_url_status(url)
    print(f"URL: {url}, Status: {status}")
