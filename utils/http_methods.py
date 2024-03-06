import requests
import os
import sys
sys.path.append(os.getcwd())

class Http_methods:
    headers = {'Content-type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        res = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
        return res

    @staticmethod
    def post(url, body):
        res = requests.post(url, headers=Http_methods.headers, cookies=Http_methods.cookie, json=body)
        return res

    @staticmethod
    def put(url, body):
        res = requests.put(url, headers=Http_methods.headers, cookies=Http_methods.cookie, json=body)
        return res

    @staticmethod
    def delete(url, body):
        res = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookie, json=body)
        return res