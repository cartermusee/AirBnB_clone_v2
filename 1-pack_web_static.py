#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """
     Fabric script that generates a .tgz archive
    """
    local("mkdir -p version")

    now = datetime.now()
    fm_date = now.strftime("%Y%m%d%H%M%S")
    result = local("tar -czvf version/web_static_{}.tgz web_static".\
            format(fm_date))
    if result.succeeded:
        return "version/web_static_{}.tgz".format(fm_date)
    else:
        return None
