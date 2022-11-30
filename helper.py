
def user_helper(user) -> dict:
    return {
        "name": user["name"],
        "password": user["password"],
        "email": user["email"],
        "is_active": user["is_active"]
    }

def userDetails_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "age": user["age"],
        "phone_number": user["phone_number"],
        "password": user["name"],
        "otp": user["otp"],
        "path": user["path"]
    }