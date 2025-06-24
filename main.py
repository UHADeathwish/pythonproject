# main.py
import argparse
from connection import init_connection
from logger import configure_logger
from users import add_user
from groups import add_group
from summary import write_summary

def main():
    parser = argparse.ArgumentParser(description="On-/offboarding in AD automatiseren")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # add-user
    p = sub.add_parser("add-user")
    p.add_argument("username")
    p.add_argument("firstname")
    p.add_argument("lastname")
    p.add_argument("group")
    # add others like --base-home, --servicedesk-tel als defaults

    # add-group
    r = sub.add_parser("add-group")
    r.add_argument("group_name")

    # ... migratie en search-user voeg je op dezelfde wijze toe

    args = parser.parse_args()

    # Init
    init_connection("poliforma.local", "administrator", "Welkom01")
    logger = configure_logger("ad_script.log")

    if args.cmd == "add-user":
        user, home = add_user(args.username, args.firstname, args.lastname,
                              args.group, "/srv/homes", logger)
        write_summary(home, args.username, args.group, "+31 20 123 4567")
    elif args.cmd == "add-group":
        add_group(args.group_name, "/srv/groups", logger)
    # ...

if __name__ == "__main__":
    main()
