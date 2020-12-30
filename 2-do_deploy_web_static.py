#!/usr/bin/python3
""" Fabric module """
from fabric.api import env, put, run, local
from os.path import exists
from re import search
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ['35.237.13.104', '35.231.190.248']


def do_deploy(archive_path):
        """ Deploy archive! """
        if exists(archive_path):
                try:
                        tmp_path = archive_path.replace("versions", "/tmp")
                        put(archive_path, "/tmp")
                        file_name = search(r"/(\w+).tgz", tmp_path).group(1)
                        path = "/data/web_static/releases/" + file_name + '/'
                        run("mkdir -p {}".format(path))
                        run("tar -xzf {} -C {}".format(tmp_path, path))
                        run("rm {}".format(tmp_path))
                        run("rsync -r {}web_static/* {}".format(path, path))
                        run("rm -rf {}web_static".format(path))
                        run("rm -rf {}".format("/data/web_static/current"))
                        run("ln -s {} /data/web_static/current".format(path))
                        return True
                except:
                        return False
        return False


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
