def validate_email(email):
    if len(email) < 8:
        return False

    if '@' not in email:
        return False

    if email.startswith('@') or email.endswith('@'):
        return False
    return True

print(validate_email('@hannahajibs'))