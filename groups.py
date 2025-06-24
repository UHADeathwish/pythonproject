# group_ops.py
import os
from pyad import adgroup

def add_group(
    group_name: str,
    base_dir: str,
    logger,
    container_dn: str = "OU=Groups,DC=poliforma,DC=local",
):
    """Create a new AD group and corresponding directory.

    Parameters
    ----------
    group_name: str
        Name of the group to create.
    base_dir: str
        Directory path where the group's folder will be created.
    logger
        Logger instance for logging actions.
    container_dn: str, optional
        Distinguished name of the container where the group will be created.
    """
    # AD-groep
    group = adgroup.ADGroup.create(group_name, container_dn=container_dn)
    logger.info(f"Nieuwe AD-groep {group_name} aangemaakt")

    # Directory
    dir_path = os.path.join(base_dir, group_name)
    os.makedirs(dir_path, exist_ok=True)
    # Stel eigenaar/rechten in (bijv. via os.chown of icacls op Windows)
    # ...
    logger.info(f"Directory {dir_path} aangemaakt voor groep {group_name}")

    return group, dir_path
