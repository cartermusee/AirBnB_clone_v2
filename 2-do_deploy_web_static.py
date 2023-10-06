#!/usr/bin/python3

from fabric.api import *
import os
from datetime import datetime


env.hosts = ['52.87.222.165', '54.237.12.4']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"
def do_deploy(archive_path):
    """
     Fabric script that generates a .tgz archive
    """

    try:
        if not os.path.exists(archive_path):
            return False

        put(archive_path, "/tmp/")

        arch_file = os.path.basename(archive_path)
        folder = "/data/web_static/releases/.{}".\
                 format(arch_file.split('.')[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(arch_file, folder))
        run("rm -r /tmp/{}".format(arch_file))

        run("rm -f /data/web_static/current")
        run('ln -s {} /data/web_static/current'.format(folder))
        return True
    except Exception as e:
        return False
    return True
