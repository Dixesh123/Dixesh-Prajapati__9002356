def create_user(first_name, last_name, age):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }

def get_full_name(user):
    return f"{user['first_name']} {user['last_name']}"
