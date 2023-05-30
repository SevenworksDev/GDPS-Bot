import requests, random

class dlprox:
    def __init__(self, url):
        self.url = url

    def get(self, filename='.proxpy-proxies'):
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(filename, 'w') as file:
                file.write(response.text)
        else:
            print("[ProxPy]: Failed to download proxies, Either the URL provided failed to load or your Internet Connection is off.")

class request:
    def __init__(self, proxy_file='.proxpy-proxies'):
        self.proxy_file = proxy_file
        self.proxies = []

    def load(self):
        with open(self.proxy_file, 'r') as file:
            self.proxies = file.read().splitlines()

    def request_proxy(self):
        random.shuffle(self.proxies)
        return self.proxies.pop(0)

    def get(self, url, headers=None, proxyInfo=None):
        proxy = self.request_proxy()
        if proxyInfo == True: print("[ProxPy]: Using proxy "+proxy)
        proxies = {'http': proxy, 'https': proxy}
        try:
            response = requests.get(url, proxies=proxies, headers=None)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"[ProxPy]: GET request failed with error: {e}")
            return None

    def post(self, url, data=None, headers=None, proxyInfo=None):
        proxy = self.request_proxy()
        if proxyInfo == True: print("[ProxPy]: Using proxy "+proxy)
        proxies = {'http': proxy, 'https': proxy}
        try:
            response = requests.post(url, proxies=proxies, data=data, headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"[ProxPy]: POST request failed with error: {e}")
            return None

