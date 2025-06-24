# main.py
import argparse
import os
from connection import init_connection
from logger import configure_logger
from users import add_user
from groups import add_group
from summary import write_summary

def main():
    parser = argparse.ArgumentParser(description="On-/offboarding in AD automatiseren")
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
    sub = parser.add_subparsers(dest="cmd", required=True)

    # add-user
    p = sub.add_parser("add-user")
    p.add_argument("username")
    p.add_argument("firstname")
    p.add_argument("lastname")
    p.add_argument("group")
    p.add_argument(
        "--user-ou",
        default="OU=pythonusers,DC=poliforma,DC=local",
        help="Container DN for new users",
    )
    # add others like --base-home, --servicedesk-tel als defaults

    # add-group
    r = sub.add_parser("add-group")
    r.add_argument("group_name")
    r.add_argument(
        "--group-ou",
        default="OU=Groups,DC=poliforma,DC=local",
        help="Container DN for new groups",
    )

    # ... migratie en search-user voeg je op dezelfde wijze toe

    args = parser.parse_args()

    if not (args.server and args.username and args.password):
        parser.error(
            "Server, username and password must be provided via options or environment variables"
        )

    # Init
    init_connection(args.server, args.username, args.password)
    logger = configure_logger("ad_script.log")

    if args.cmd == "add-user":
        user, home = add_user(
            args.username,
            args.firstname,
            args.lastname,
            args.group,
            "/srv/homes",
            logger,
            container_dn=args.user_ou,
        )
        write_summary(home, args.username, args.group, "+31 20 123 4567")
    elif args.cmd == "add-group":
        add_group(args.group_name, "/srv/groups", logger, container_dn=args.group_ou)
    # ...

if __name__ == "__main__":
    main()
