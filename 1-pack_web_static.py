#!/usr/bin/python3
"""Fabric script to generate .tgz archive"""

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once


@runs_once
def do_pack():
        """
        Creates a .tgz archive from all files in web_static folder
        Archive name:
          web_static_<year><month><day><hour><minute><second>.tgz
        Returns:
            archive path if successful else None
    """
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    return None
