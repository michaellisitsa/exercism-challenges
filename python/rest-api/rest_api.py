import json


class RestAPI:
    # TODO: how to type a dict with specific key "users" and list of dict
    def __init__(self, database: dict | None = None):
        """
        Ingest database with users like below
        "users": [
            {"name": "Adam", "owes": { "Bob": 12.0, "Chuck": 4.0 }, "owed_by": { "Bob": 6.5, "Dan": 2.75 }, "balance": 0.0},
        ]
        """
        # TODO: Do I need to normalize the data, or just have getters for different things like amount
        if database is None:
            self._data = {"users": []}
        else:
            self._data = database

        # TODO: Rename to better method

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
        """
        payload = {"users":["Adam","Bob"]}
        """
        if payload is None:
            return json.dumps(self._data)
        # TODO: Add a decorator to decode and encode. This is is getting old
        payload_decoded = json.loads(payload)
        if url.endswith("users"):
            filtered_users = map(self.fetchData, payload_decoded["users"])
            return json.dumps({"users": list(filtered_users)})

    def post(self, url, payload=None):
        if url.endswith("add"):
            if payload is None:
                return
            payload_decoded = json.loads(payload)
            # TODO: We need to make it easier to do a set, rather than every time grabbing the user id
            # and filtering over the list
            new_user = self.setData(payload_decoded["user"])
        return json.dumps(new_user)
