# summary.py
import os

def write_summary(home_path: str, username: str, group: str, servicedesk_tel: str):
    """
    Schrijft een tekstbestand in de home dir met alle gevraagde info.
    """
    summary_file = os.path.join(home_path, "user_summary.txt")
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"Gebruiker: {username}\n")
        f.write(f"Groep: {group}\n")
        f.write(f"Home Path: {home_path}\n")
        f.write(f"Servicedesk: {servicedesk_tel}\n")
