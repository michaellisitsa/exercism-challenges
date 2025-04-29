from __future__ import annotations  # must be at top of file

from functools import wraps
import json
from dataclasses import dataclass, field, asdict
from typing import TypeGuard, TypedDict, assert_type, cast


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


class Database(dict[str, User]):
    def __missing__(self, name) -> User:
        self[name] = User(name)
        return self[name]


class IOUPayloadT(TypedDict):
    lender: str
    borrower: str
    amount: float


class AddPayloadT(TypedDict):
    user: str


def is_add_payload(x: object) -> TypeGuard[AddPayloadT]:
    return (
        isinstance(x, dict)
        and all(isinstance(key, str) for key in x)
        and "user" in x
        and isinstance(x["user"], str)
    )


def is_iou_payload(x: object) -> TypeGuard[IOUPayloadT]:
    return (
        isinstance(x, dict)
        and all(isinstance(key, str) for key in x)
        and "lender" in x
        and isinstance(x["lender"], str)
    )


def json_serializer(func):
    @wraps(func)
    def wrapper(self, url, payload=None):
        serialized_payload = None
        if payload is not None:
            serialized_payload = json.loads(payload)
        return json.dumps(func(self, url, serialized_payload))

    return wrapper


class RestAPI:
    _data: Database

    def __init__(self, database: DatabaseDict | None = None):
        self._data = Database()
        if database:
            for user in database["users"]:
                self.set_user(user)

    def set_user(self, data: UserDict) -> User:
        # Only name is requred by the User class
        user = User(
            data["name"],
            data["owes"],
            data["owed_by"],
            data["balance"],
        )
        self._data[user.name] = user
        return user

    def get_user(self, name: str) -> User:
        return self._data[name]

    def get_users(self) -> list[dict[str, User]]:
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

    @json_serializer
    def get(self, url, payload=None):
        if url.endswith("users"):
            if payload is None:
                return {"users": self.get_users()}
            else:
                users = [asdict(self.get_user(user)) for user in payload["users"]]
                return {"users": users}

    @json_serializer
    def post(self, url: str, payload: IOUPayloadT | AddPayloadT):
        if url.endswith("add") and is_add_payload(payload):
            return asdict(
                self.set_user(
                    {
                        "name": payload["user"],
                        "owes": {},
                        "owed_by": {},
                        "balance": 0,
                    }
                )
            )
        elif url.endswith("iou") and is_iou_payload(payload):
            amount = payload["amount"]
            borrower = self.get_user(payload["borrower"])
            lender = self.get_user(payload["lender"])
            # Decrement the balance of the lender, increment of the lender
            borrower.balance -= amount
            lender.balance += amount
            # TODO: Append to existing balance
            borrower.owes[lender.name] = amount
            lender.owed_by[borrower.name] = amount
            return {"users": [asdict(lender), asdict(borrower)]}
