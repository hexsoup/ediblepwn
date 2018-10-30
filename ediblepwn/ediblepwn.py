import requests
import json

BASE_URL = "https://haveibeenpwned.com/api/v2"
HEADERS = {
    "User-Agent": "EdiblePwn"
}

class EdiblePwn():
    def __init__(self):
        pass

    def get_breaches(self):
        try:
            response = requests.get("{}/breaches".format(BASE_URL), headers=HEADERS)
            if response.text:
                return response.json()
            else:
                return "No results found."
        except requests.exceptions.HTTPError as e:
            return e
        except ConnectionError as e:
            return e

    def get_breaches_by_account(self, account):
        try:
            response = requests.get("{}/breachedaccount/{}".format(BASE_URL,account),headers=HEADERS)
            if response.text:
                return response.json()
            else:
                return "No results found for specified account."
        except requests.exceptions.HTTPError as e:
            return e
        except ConnectionError as e:
            return e

    def get_breaches_by_site(self, site):
        try:
            response = requests.get("{}/breach/{}".format(BASE_URL, site), headers=HEADERS)
            if response.text:
                return response.json()
            else:
                return "No results found for specified site."
        except requests.exceptions.HTTPError as e:
            return e
        except ConnectionError as e:
            return e

    def get_pastes_by_account(self, account):
        try:
            response = requests.get("{}/pasteaccount/{}".format(BASE_URL,account),headers=HEADERS)
            if response.text:
                return response.json()
            else:
                return "No results found for specified account."
        except requests.exceptions.HTTPError as e:
            return e
        except requests.exceptions.ConnectionError as e:
            return e

    def get_passwords_by_partial_hash(self, hash):
        try:
            response = requests.get("https://api.pwnedpasswords.com/range/{}".format(hash),headers=HEADERS)
            if response.text:
                return response.text
            else:
                return "No results found for specified partial hash."
        except requests.exceptions.HTTPError as e:
            return e
        except ConnectionError as e:
            return e
