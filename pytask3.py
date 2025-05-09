import hashlib


users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        return "Username already exists"
    users[username] = hash_password(password)
    return "Created new user"

def login(username, password):
    if username not in users:
        return "User not found"
    if users[username] == hash_password(password):
        return "Login Successful"
    return "Incorrect password"


print(register("john", "mypassword"))  #Created new user
print(login("john", "mypassword"))    #Login Successful
print(login("john", "wrongpass"))     #Incorrect password
print(register("john", "newpass"))    #Username already exists