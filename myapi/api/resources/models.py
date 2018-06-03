"""
The users Database
"""
users = [
    {
        "firstname": "wairimu",
        "lastname": "wairimu",
        "email": "wairimu@wairimu.com",
        "username": "wairimu",
        "password": "wairimu"
    }
]
requests =[]

def add_user(data):
    users.append(data)

def add_request(data):
    requests.append(data)

def view_users():
    return users


def login(username, password):
    for i in users:
        if i['username'] == username and i['password'] == password:
            return True
    else:
        return False
