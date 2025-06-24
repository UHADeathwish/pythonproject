# group_ops.py
import os
from pyad import adgroup

def add_group(group_name: str, base_dir: str, logger):
    """
    Maakt een nieuwe AD-groep én een directory met groepseigenaar.
    """
    # AD-groep
    group = adgroup.ADGroup.create(group_name,
                                   container_dn="OU=Groups,DC=poliforma,DC=local")
    logger.info(f"Nieuwe AD-groep {group_name} aangemaakt")

    # Directory
    dir_path = os.path.join(base_dir, group_name)
    os.makedirs(dir_path, exist_ok=True)
    # Stel eigenaar/rechten in (bijv. via os.chown of icacls op Windows)
    # ...
    logger.info(f"Directory {dir_path} aangemaakt voor groep {group_name}")

    return group, dir_path
