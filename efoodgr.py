import json
import os
import requests
import urllib3

config = {
    "register": {
        "method": "post",
        "url": "https://api.e-food.gr/api/v1/user/register",
        "data": {
            "email": None,
            "password": None
        },
        "aftermethod": "json"
    },
    "login": {
        "method": "post",
        "url": "https://api.e-food.gr/api/v1/user/login",
        "data": {
            "email": None,
            "password": None
        },
        "aftermethod": "json"
    },
    "reset_password": {
        "method": "post",
        "url": "https://api.e-food.gr/api/v1/user/reset_password",
        "data": {
            "email": None
        },
        "aftermethod": "json"
    },
    "account": {
        "method": "get",
        "url": "https://api.e-food.gr/api/v1/user/account",
        "aftermethod": "json"
    },
    "address": {
        "method": "get",
        "url": "https://api.e-food.gr/api/v1/user/clients/address",
        "aftermethod": "json"
    },
    "shops": {
        "method": "get",
        "url": "https://api.e-food.gr/api/v1/restaurants",
        "params": {
            "latitude": None,
            "longitude": None,
            "filters": {},
            "mode": "filter",
            "version": "3"
        },
        "aftermethod": "json"
    }
}

def req(js0n: dict=None, r=None):
    if js0n != None and isinstance(js0n, dict) and len(js0n) > 0:
        if "r" in js0n and js0n["r"] != None:
            r_ = js0n["r"]
        else:
            if r != None:
                r_ = r
            else:
                r_ = None
        if "method" in js0n and js0n["method"] != None:
            method_ = js0n["method"]
        else:
            method_ = None
        if "url" in js0n and js0n["url"] != None:
            url_ = js0n["url"]
        else:
            url_ = None
        if "params" in js0n and js0n["params"] != None:
            params_ = js0n["params"]
        else:
            params_ = None
        if "data" in js0n and js0n["data"] != None:
            data_ = js0n["data"]
        else:
            data_ = None
        if "headers" in js0n and js0n["headers"] != None:
            headers_ = js0n["headers"]
        else:
            headers_ = None
        if "aftermethod" in js0n and js0n["aftermethod"] != None:
            aftermethod_ = str(js0n["aftermethod"]).lower()
        else:
            aftermethod_ = None
        if r_ != None:
            try:
                re = r_.request(
                    method=method_,
                    url=url_,
                    params=params_,
                    data=data_,
                    headers=headers_
                )
            except Exception:
                re = None
            if re != None:
                out = None
                if aftermethod_ == "text":
                    try:
                        out = re.text
                    except Exception:
                        pass
                if aftermethod_ == "json":
                    try:
                        out = re.json()
                    except Exception:
                        pass
                if aftermethod_ == "content":
                    try:
                        out = re.content
                    except Exception:
                        pass
                return out

class Efood:
    def __init__(self):
        with requests.Session() as ss:
            self.session = ss
            headers_config = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42",
                "X-core-platform": "web",
                "X-core-version": "2.31.2",
                "Accept-Language": "el"
            }
            for header in headers_config:
                self.session.headers[header] = headers_config[header]
    def login(self, email :str=None, password :str=None):
        if email != None and isinstance(email, str) and password != None and isinstance(password, str):
            config["login"]["data"]["email"] = email
            config["login"]["data"]["password"] = password
            data0 = req(config["login"], self.session)
            print(data0["status"])
            if data0 != None and isinstance(data0, dict):
                if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                    data1 = data0["data"]
                    if "session_id" in data1 and data1["session_id"] != None and isinstance(data1["session_id"], str):
                        self.session.headers["x-core-session-id"] = data0["data"]["session_id"]
                    if "user" in data1 and data1["user"] != None and isinstance(data1["user"], dict):
                        return data1["user"]
    def register(self, email :str=None, password :str=None):
        if email != None and isinstance(email, str) and password != None and isinstance(password, str):
            config["register"]["data"]["email"] = email
            config["register"]["data"]["password"] = password
            data0 =  req(config["register"], self.session)
            if data0 != None and isinstance(data0, dict):
                if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                    data1 = data0["data"]
                    if "session_id" in data1 and data1["session_id"] != None and isinstance(data1["session_id"], str):
                        self.session.headers["x-core-session-id"] = data0["data"]["session_id"]
                    if "user" in data1 and data1["user"] != None and isinstance(data1["user"], dict):
                        return data1["user"]
    def reset_password(self, email :str=None):
        if email != None and isinstance(email, str) and email != "" and email != " ":
            config["reset_password"]["data"]["email"] = email
            data0 = req(config["reset_password"], self.session)
            if data0 != None and isinstance(data0, dict):
                if "status" in data0 and data0["status"] != None and isinstance(data0["status"], str):
                    return data0["status"] == "ok"
    def account(self):
        data0 = req(config["account"], self.session)
        if data0 != None and isinstance(data0, dict):
            if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                return data0["data"]
    def address(self):
        data0 = req(config["address"], self.session)
        if data0 != None and isinstance(data0, dict):
            if "data" in data0 and data0["data"] != None and isinstance(data0["data"], list) and len(data0["data"]) > 0:
                return data0["data"]
    def shops(self, latitude :float=None, longitude: float=None):
        if latitude != None and isinstance(latitude, float) and longitude != None and isinstance(longitude, float):
            config["shops"]["params"]["latitude"] = latitude
            config["shops"]["params"]["longitude"] = longitude
            data0 = req(config["shops"], self.session)
            if data0 != None and isinstance(data0, dict):
                if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                    data1 = data0["data"]
                    if "restaurants" in data1 and data1["restaurants"] != None and isinstance(data1["restaurants"], list) and len(data1["restaurants"]) > 0:
                        return data0["data"]["restaurants"]
    def menu(self, shop_id :int=None):
        if shop_id != None and isinstance(shop_id, int):
            config["shops"]["url"] = f'{config["shops"]["url"]}/{shop_id}'
            data0 = req(config["shops"], self.session)
            if data0 != None and isinstance(data0, dict):
                if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                    data1 = data0["data"]
                    if "menu" in data1 and data1["menu"] != None and isinstance(data1["menu"], dict):
                        menu = data1["menu"]
                        if "categories" in menu and menu["categories"] != None and isinstance(menu["categories"], list) and len(menu["categories"]) > 0:
                            return menu["categories"]
