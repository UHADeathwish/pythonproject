# Python Project AD Automation

This project automates user and group management tasks in Active Directory using Python.

## Connection options

The scripts no longer use hard-coded connection details. Provide the LDAP server address, username and password through command-line options or environment variables.

### Environment variables

- `AD_SERVER` – server address
- `AD_USERNAME` – bind username
- `AD_PASSWORD` – bind password

### Command-line options

```
--server   LDAP server address
--username Bind account username
--password Bind account password
```

Values specified on the command line override the environment variables.

Example usage:

```bash
export AD_SERVER=poliforma.local
export AD_USERNAME=Administrator
export AD_PASSWORD=Welkom01
python main.py --server poliforma.local add-user jdoe John Doe ExampleGroup
```

