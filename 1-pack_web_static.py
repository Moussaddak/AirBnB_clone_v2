#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """tgz archive all"""
    try:
        if not isdir("versions"):
            local("mkdir versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        fname = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(fname))
        return fname
    except:
        return None
