#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """
     Fabric script that generates a .tgz archive
    """
    local("mkdir -p versions")

    now = datetime.now()
    fm_date = now.strftime("%Y%m%d%H%M%S")
    result = local("tar -czvf versions/web_static_{}.tgz web_static".
                   format(fm_date))
    if result.succeeded:
        return "versions/web_static_{}.tgz".format(fm_date)
    else:
        return None


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
        run("sudo ln -s /data/web_static/releases/{}/ \
/data/web_static/current".format(filename))
        return True


def deploy():
    """deploy fiunction"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
