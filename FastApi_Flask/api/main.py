from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import flask_app, db
from database import User
from models.User import User as BaseUser
from controllers.UserController import getUsers, newUser, updateUser, removeUser

# Init app
app = FastAPI()

# Permitted origins
origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Working
@app.get("/")
def root():
    return {"message": "OK"}

# ENDPOINTS
# List users
@app.get("/users", tags=["User"])
def listUsers():
    with flask_app.app_context():
        return getUsers()

# Create user
@app.post("/users", tags=["User"])
def createUser(user: BaseUser):
    with flask_app.app_context():
        return newUser(user.firstName, user.lastName)

# Update user
@app.put("/users", tags=["User"])
def modifyUser(id: int, user: BaseUser):
    with flask_app.app_context():
        return updateUser(id, user)

# Delete user
@app.delete("/users", tags=["User"])
def deleteUser(id: int):
    with flask_app.app_context():
        return removeUser(id)