#!/usr/bin/python3
"""to deplaoy"""
from fabric.api import *
import os
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['52.87.222.165', '54.237.12.4']
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        filename = os.path.basename(archive_path.split('.')[0])
        folder = run("sudo mkdir -p /data/web_static/releases/{}/".
                     format(filename))
        run('sudo tar -xzvf /tmp/{} -C /data/web_static/releases/{}/'.
            format(os.path.basename(archive_path), filename))
        run("sudo rm  /tmp/{}".format(os.path.basename(archive_path)))
        run("sudo rm -f /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /\
                data/web_static/current".format(filename))
        return True
    except Exception as e:
        return False
