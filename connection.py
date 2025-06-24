# connection.py
from pyad import pyad
from pyad import aduser

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
    init_connection(
        ldap_server="192.168.1.130",      # Server IP / Hostname
        username="Administrator",        # Username
        password="Welkom01"      # Wachtwoord
    )