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
requests = []


def add_user(data):
    users.append(data)


def add_request(data):
    data['id'] = len(requests) + 1
    requests.append(data)


def view_user_requests(username):
    request = [
        request for request in requests if request["username"] == username]
    return request
    


def get_request_id(username, id):
    dicts = view_user_requests(username)
    result = next(
        (item for item in dicts if item["id"] == id), False)
    return result


def edit_request(username, id, title, request):
    result = get_request_id(username, id)
    result['title'] = title
    result['request'] = request


def view_users():
    return users

def login(username, password):
    for i in users:
        if i['username'] == username and i['password'] == password:
            return True
    else:
        return False
