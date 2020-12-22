#!/usr/bin/python3
""" Fabric module """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ function do_pack """
    time = datetime.now()
    path = "versions/web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))
    if not os.path.exists("versions/"):
        os.mkdir("versions")
    result = local("tar -cvzf {} web_static".format(path), capture=True)
    if result.succeeded:
        return path
    return None
