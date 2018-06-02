users = [
    {
        "firstname": "wairimu",
        "lastname": "wairimu",
        "email": "wairimu@wairimu.com",
        "username": "wairimu",
        "password": "wairimu"
    }
]


def add_user(data):
    users.append(data)


def view_users():
    return users


def view_username():
    for i in users:
        return i['username']


def view_password():
    for i in users:
        return i['password']


def login(username, password):
    for i in users:
        if i['username'] == username and i['password'] == password:
            return True
    else:
        return False
