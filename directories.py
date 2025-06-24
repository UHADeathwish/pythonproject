# directory_ops.py
import os
import shutil
import subprocess

def create_home_directory(path: str, group: str, logger):
    os.makedirs(path, exist_ok=True)
    # Windows: gebruik icacls of PowerShell om rechten in te stellen
    subprocess.run(["icacls", path, "/grant", f"{group}:(OI)(CI)M"], check=True)
    logger.debug(f"Rechten ingesteld op {path} voor groep {group}")

def move_to_backup(path: str, backup_root: str, logger):
    os.makedirs(backup_root, exist_ok=True)
    dst = os.path.join(backup_root, os.path.basename(path))
    shutil.move(path, dst)
    logger.debug(f"{path} -> {dst}")
