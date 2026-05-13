def is_strong_password(password):
    if len(password) < 8:
        return False
    return True

print(is_strong_password('1,2,3,4,5,6,7,8'))