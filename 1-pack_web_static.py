#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """
     Fabric script that generates a .tgz archive
    """
    try:
        local("mkdir -p versions")

        now = datetime.now()
        fm_date = now.strftime("%Y%m%d%H%M%S")
        result = local("tar -czvf versions/web_static_{}.tgz web_static".
                       format(fm_date))
        return "versions/web_static_{}.tgz".format(fm_date)
    except Exception as e:
        return None
