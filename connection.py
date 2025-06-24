# connection.py
from pyad import pyad
from pyad import aduser
import argparse
import os

def init_connection(ldap_server: str, username: str, password: str):
    """
    Stel de AD-connectie in met pyad.
    """
    pyad.set_defaults(ldap_server=ldap_server,
                      username=username,
                      password=password)
    try:
        # Try to fetch the current user to test the connection
        user = aduser.ADUser.from_cn(username)
        print(f"Connected to AD server {ldap_server} as {username}. Connection works. User: {user}")
    except Exception as e:
        print(f"Connected to AD server {ldap_server} as {username}, but connection test failed: {e}")

# Verbinding test uitvoeren indien dit script direct wordt uitgevoerd
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test AD connection")
    parser.add_argument(
        "--server",
        default=os.environ.get("AD_SERVER"),
        help="LDAP server address",
    )
    parser.add_argument(
        "--username",
        default=os.environ.get("AD_USERNAME"),
        help="Bind account username",
    )
    parser.add_argument(
        "--password",
        default=os.environ.get("AD_PASSWORD"),
        help="Bind account password",
    )
    args = parser.parse_args()
    if not (args.server and args.username and args.password):
        parser.error(
            "Server, username and password must be provided via options or environment variables"
        )

    init_connection(
        ldap_server=args.server,
        username=args.username,
        password=args.password,
    )
