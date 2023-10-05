#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """
     Fabric script that generates a .tgz archive
    """
    local("mkdir -p version")

    now = datetime.now()
    arch = "web_static_{}{}{}{}{}{}.tgz".\
        format(now.year,
               now.month,
               now.day, now.hour, now.minute, now.second)
    result = local("tar -cvzf version/{} web_static".format(arch))
    if result.succeeded:
        return "version/{}".format(arch)
    else:
        return None
