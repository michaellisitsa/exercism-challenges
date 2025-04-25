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

    def get(self, url, payload=None):
        """
        payload = {"users":["Adam","Bob"]}
        """
        if payload is None:
            return json.dumps(self._data)
        payload_decoded = json.loads(payload)
        if url.endswith("users"):
            filtered_users = map(self.fetchData, payload_decoded["users"])
            return json.dumps({"users": list(filtered_users)})
