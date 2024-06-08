from mathematical_operations import add
from string_operations import concatenate
from user_operation import create_user, get_full_name

def combined_user_operation(d, h, first_name, last_name, age):
    addition_result = add(d, h)
    user = create_user(first_name, last_name, age)
    full_name = get_full_name(user)
    return addition_result, full_name
