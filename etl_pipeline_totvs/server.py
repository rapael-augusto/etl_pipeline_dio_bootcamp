from fastapi import FastAPI

app = FastAPI()

users = [
        {
            "id": 1,
            "name": "Devweekerson",
            "account": {
                "id": 1,
                "number": "01.097954-4",
                "agency": "2030",
                "balance": 624.12,
                "limit": 1000
            },
            "card": {
                "id": 1,
                "number": "xxxx xxxx xxxx 1111",
                "limit": 2000
            },
            "features": [],
            "news": []
        },
        {
            "id": 2,
            "name": "ImagineSomethingReallyCreativeHere",
            "account": {
                "id": 2,
                "number": "01.023954-4",
                "agency": "2023",
                "balance": 2624.12,
                "limit": 10000
            },
            "card": {
                "id": 2,
                "number": "xxxx xxxx xxxx 2111",
                "limit": 3000
            },
            "features": [],
            "news": []
        },
        {
            "id": 3,
            "name": "ThirdTimeIsTheCharm",
            "account": {
                "id": 3,
                "number": "01.023934-4",
                "agency": "2023",
                "balance": 2694.12,
                "limit": 10000
            },
            "card": {
                "id": 3,
                "number": "xxxx xxxx xxxx 2131",
                "limit": 3000
            },
            "features": [],
            "news": []
        },
        {
            "id": 4,
            "name": "MyNameIsPink",
            "account": {
                "id": 4,
                "number": "01.023934-4",
                "agency": "2024",
                "balance": 23694.12,
                "limit": 10000
            },
            "card": {
                "id": 4,
                "number": "xxxx xxxx xxxx 2031",
                "limit": 3000
            },
            "features": [],
            "news": []
        },
        {
            "id": 5,
            "name": "AndI'mReallyGladToMeetYou",
            "account": {
                "id": 5,
                "number": "01.053934-4",
                "agency": "2024",
                "balance": 294.12,
                "limit": 1000
            },
            "card": {
                "id": 5,
                "number": "xxxx xxxx xxxx 2931",
                "limit": 2200
            },
            "features": [],
            "news": []
        }
]

@app.get("/users")
def get_all():
    return users

@app.get("/users/{id}")
def get_by_id(id: int):
    return next((u for u in users if u["id"] == id), None)

@app.put("/users/{id}")
def put_by_id(id: int, user_data: dict):
    for i, u in enumerate(users):
        if u["id"] == id:
            user_data["id"] = id
            users[i] = user_data
            return users[i]
