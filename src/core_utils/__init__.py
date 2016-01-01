# coding=utf-8
import os
import shutil

import sys

from src.config import CONFIG, create_config


# kill certain processes
def kill_proc(port, flag):
    return
    # proc = subprocess.Popen("netstat -antp | grep '{0}'".format(port), shell=True, stdout=subprocess.PIPE)
    # stdout_value = proc.communicate()[0]
    # a = re.search("\d+/{0}".format(flag), stdout_value)
    # if a:
    #     b = a.group()
    #     b = b.replace("/{0}".format(flag), "")
    #     subprocess.Popen("kill -9 {0}".format(b), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()


def cleanup_routine():
    """
    Cleanup old or stale files
    :return:
    :rtype:
    """
    # restore original Java Applet
    shutil.copyfile("src/html/Signed_Update.jar.orig", os.path.join(CONFIG["SET_dir"], "Signed_Update.jar"))
    if os.path.isfile("newcert.pem"):
        os.remove("newcert.pem")
    if os.path.isfile(os.path.join(CONFIG["SET_dir"], "/interfaces")):
        os.remove(os.path.join(CONFIG["SET_dir"], "/interfaces"))
    if os.path.isfile("src/html/1msf.raw"):
        os.remove("src/html/1msf.raw")
    if os.path.isfile("src/html/2msf.raw"):
        os.remove("src/html/2msf.raw")
    if os.path.isfile("msf.exe"):
        os.remove("msf.exe")
    if os.path.isfile("src/html/index.html"):
        os.remove("src/html/index.html")
    if os.path.isfile(os.path.join(CONFIG["SET_dir"], "/Signed_Update.jar")):
        os.remove(os.path.join(CONFIG["SET_dir"], "/Signed_Update.jar"))
    if os.path.isfile(os.path.join(CONFIG["SET_dir"], "/version.lock")):
        os.remove(os.path.join(CONFIG["SET_dir"], "/version.lock"))
    # kill anything python running on 80
    kill_proc("80", "python")
    # kill anything on 443 ruby which is generally a rogue listener
    kill_proc("443", "ruby")


def check_config():
    default_config_path = os.path.join(os.path.expanduser("~/.set/config.ini"))
    if not os.path.isfile(default_config_path):
        setdir = os.path.split(default_config_path)[0]
        if not os.path.exists(setdir):
            os.makedirs(setdir)
        create_config(default_config_path)


def check_environment():
    if os.geteuid() != 0:
        print("\n The Social-Engineer Toolkit (SET) - by David Kennedy (ReL1K)")
        print("\n Not running as root. \n\nExiting the Social-Engineer Toolkit (SET).\n")
        sys.exit(1)