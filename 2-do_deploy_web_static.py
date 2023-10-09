#!/usr/bin/python3
"""to deplaoy"""
from fabric.api import *
import os
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['52.87.222.165', '54.237.12.4']
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """finction deploy
    arg:
        archive_path:the path
    """
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path.split('.')[0])
        run("sudo mkdir -p /data/web_static/releases/{}/".
            format(filename))
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(os.path.basename(archive_path), filename))
        run("sudo rm  /tmp/{}".format(os.path.basename(archive_path)))
        run("sudo mv  /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(filename, filename))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(filename))
        run("sudo rm -rf data/web_static/current")
        if not exists("/data/web_static/current"):
            run("sudo ln -s /data/web_static/releases/{}/ \
/data/web_static/current".format(filename))
        return True
    except Exception as e:
        return False
