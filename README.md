# Active Directory Automation Scripts

This project provides Python utilities to automate creation of users and groups in Active Directory. The scripts rely on the `pyad` package to communicate with the domain controller and expect that they are run by an account with permission to manage users and groups.

## Prerequisites

- **Python version**: Python 3.10 or newer.
- **Active Directory permissions**: The executing account must have rights to create users, groups and modify home folder permissions.
- **Operating system**: Windows with access to the domain where `pyad` is able to connect (uses `pywin32`).

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Edit `main.py` with the correct domain name and credentials for your environment.

## Usage

Example to create a user:

```bash
python main.py add-user jdoe John Doe "CN=Domain Users,CN=Users,DC=poliforma,DC=local"
```

Example to create a group:

```bash
python main.py add-group "HR Users"
```

The scripts log their actions to `ad_script.log` and create a small summary file in the user's home directory.

