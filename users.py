# users.py
from pyad import aduser, adcontainer
import os
from directories import create_home_directory

def add_user(username: str, firstname: str, lastname: str, group_dn: str, base_home: str, logger):
    container = adcontainer.ADContainer.from_dn("OU=pythonusers,DC=poliforma,DC=local")

    # Try removing an existing user to avoid naming conflicts
    try:
        existing_user = aduser.ADUser.from_cn(username)
        existing_user.delete()
        logger.info(f"Removed existing user {username} before creating new one.")
    except:
        pass

    # Create a disabled user with minimal attributes
    user = aduser.ADUser.create(
        username,
        container,
        optional_attributes={
            "givenName": firstname,
            "sn": lastname,
            "sAMAccountName": username,
            "userPrincipalName": f"{username}@poliforma.local",
            "userAccountControl": 514  # disabled
        }
    )
    logger.info(f"User {username} created (disabled).")

    # Try a more complex password
    user.set_password("WelK0m!2025")  # Change to a strong password not reused

    # Enable account
    user.update_attribute("userAccountControl", 512)
    logger.info(f"Password set and account enabled for {username}")

    # Create home directory
    home_path = os.path.join(base_home, username)
    create_home_directory(home_path, group_dn, logger)
    logger.info(f"Home directory {home_path} created")

    return user, home_path
