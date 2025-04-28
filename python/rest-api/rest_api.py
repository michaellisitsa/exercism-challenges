from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import TypedDict


@dataclass
class User:
    name: str
    owes: dict[str, float] = field(default_factory=dict)
    owed_by: dict[str, float] = field(default_factory=dict)
    balance: float = 0

    def to_string(self) -> str:
        return f"{self.name}- owes: {self.owes} and is owed by {self.owed_by} with balance {self.balance}"


class UserDict(TypedDict):
    name: str
    owes: dict[str, float]
    owed_by: dict[str, float]
    balance: float


class DatabaseDict(TypedDict):
    users: list[UserDict]


class Database(dict):
    def __missing__(self, name) -> User:
        self[name] = User(name)
        return self[name]


class RestAPI:
    _data: Database

    # TODO: how to type a dict with specific key "users" and list of dict
    def __init__(self, database: DatabaseDict | None = None):
        self._data = Database()
        if database:
            for user in database["users"]:
                self.set_user(user)

    def set_user(self, data):
        # Only name is requred by the User class
        user = User(
            data["name"],
            data["owes"],
            data["owed_by"],
            data["balance"],
        )
        self._data[user.name] = user

    def get_user(self, name):
        return self._data[name]

    def get_users(self):
        return [asdict(user) for user in self._data.values()]

    def fetchData(self, userId) -> dict | None:
        # TODO: Get a better find function
        user = None
        if self._data is None:
            return None
        users = self._data["users"]
        # Find a neater way to destructure all the keys in each iteration
        for current_user in users:
            name = current_user["name"]
            if name == userId:
                user = current_user
                break
        return user

    def setData(self, userId) -> None:
        user = self.fetchData(userId)
        if not user:
            user = {"name": userId, "owes": {}, "owed_by": {}, "balance": 0}
            self._data["users"].append(user)
            return user

    def get(self, url, payload=None):
        if url.endswith("users"):
            if payload is None:
                return json.dumps({"users": self.get_users()})
            else:
                users = [
                    asdict(self.get_user(user)) for user in json.loads(payload)["users"]
                ]
                return json.dumps({"users": users})

    def post(self, url, payload=None):
        if payload is None:
            return
        payload_decoded = json.loads(payload)
        if url.endswith("add"):
            # TODO: We need to make it easier to do a set, rather than every time grabbing the user id
            # and filtering over the list
            new_user = self.setData(payload_decoded["user"])
        elif url.endswith("iou"):
            # expected data shape =  {"lender":<name of lender>,"borrower":<name of borrower>,"amount":5.25}
            borrower = self.fetchData(payload_decoded["borrower"])
            lender = self.fetchData(payload_decoded["lender"])
            # Decrement the balance of the lender, increment of the lender
            borrower["balance"] -= payload_decoded["amount"]
            lender["balance"] += payload_decoded["amount"]
            # Find the lender in the list of in the borrower's owed list
            borrower_currently_owes_lender_amt = borrower["owes"][lender["name"]]
            borrower_currently_owes_lender_amt += payload_decoded["amount"]
        return json.dumps(new_user)
