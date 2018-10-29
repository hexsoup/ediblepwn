import requests

BASE_URL = "https://haveibeenpwned.com/api/v2"
HEADERS = {
    "User-Agent": "EdiblePwn"
}

class EdiblePwn():
    def __init__(self):
        pass

    def get_breaches(self):
        response = requests.get("{}/breaches".format(BASE_URL), headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def get_breaches_by_account(self, account):
        response = requests.get("{}/breachedaccount/{}".format(BASE_URL,account),headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def get_breaches_by_site(self, site):
        response = requests.get("{}/breach/{}".format(BASE_URL, site), headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def get_pastes_by_account(self, account):
        response = requests.get("{}/pasteaccount/{}".format(BASE_URL,account),headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()

    def get_passwords_by_partial_hash(self, hash):
        response = requests.get("https://api.pwnedpasswords.com/range/{}".format(hash),headers=HEADERS)
        if response.status_code == 200:
            return response.text
        response.raise_for_status()
