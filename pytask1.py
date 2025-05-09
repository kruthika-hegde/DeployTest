users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_user(user):   #add function
    users.append(user)
    add_user({"id": 3, "name": "Johnny", "email": "johnny@example.com"})

def get_user_by_id(user_id):    #get function
    for user in users:
        if user["id"] == user_id:
            return user
    return None
print(get_user_by_id(2))

def update_user(user_id, new_data): #update function
    for user in users:
        if user["id"] == user_id:
            user.update(new_data)
            return True
    return False
update_user(1, {"email": "alice0127@example.com"})


def delete_user(user_id):   #delete function
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return True
    return False
delete_user(2)
print(users)




