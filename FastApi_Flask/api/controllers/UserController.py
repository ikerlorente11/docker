from database import db, User

def getUsers():
    """
    Retrieve all users from the database.
    
    Returns:
        list: A list of User objects.
    """
    users = User.query.all()
    return users


def newUser(firstName: str, lastName: str):
    """
    Create a new user in the database.
    
    Args:
        firstName (str): First name of the user.
        lastName (str): Last name of the user.
    
    Returns:
        tuple: A dictionary with a success message and user ID, and the HTTP status code.
    """
    # Validate parameters
    if not firstName or not lastName:
        return {"message": "First name and last name are required"}, 400

    # Create new user
    new_user = User(firstName=firstName, lastName=lastName)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created successfully", "id": new_user.id}, 201


def updateUser(id: int, user_data):
    """
    Update an existing user in the database.
    
    Args:
        id (int): ID of the user to be updated.
        user_data (dict): Dictionary containing updated user information.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search user in database
    user = User.query.get(id)
    if not user:
        return {"message": "User not found"}, 404
    
    # Extract new values
    firstName = user_data.firstName
    lastName = user_data.lastName
    
    # Update user values
    user.firstName = firstName
    user.lastName = lastName
    
    db.session.commit()

    return {"message": "User updated successfully"}, 200


def removeUser(id: int):
    """
    Remove a user from the database.
    
    Args:
        id (int): ID of the user to be deleted.
    
    Returns:
        tuple: A dictionary with a success or error message and the HTTP status code.
    """
    # Search user in database
    user = User.query.get(id)
    if not user:
        return {"message": "User not found"}, 404
    
    # Remove user
    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted successfully"}, 200
