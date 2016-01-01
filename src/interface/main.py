# coding=utf-8
from __future__ import print_function

import cmd

from banners import intro_banner
from graphics_utils import random_graphic
from menus import AcceptLicense, FastTrack, SocialEngineeringAttacks, ThirdParyMods, UpdateConfig, UpdateSET


class bcolors(object):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'


# Py2/3 compatibility
# Python3 renamed raw_input to input
try:
    input = raw_input
except NameError:
    pass


class SETToolkit(cmd.Cmd, object):
    def __init__(self, *args, **kwargs):
        super(SETToolkit, self).__init__(*args, **kwargs)
        self.intro = ("Select from the following options:\n"
                      "1) Social-Engineering Attacks\n"
                      "2) Penetration Testing (Fast-Track)\n"
                      "3) Third Party Modules\n"
                      "4) Update the Social-Engineer Toolkit\n"
                      "5) Update SET configuration\n"
                      "6) Help, Credits, and About\n"
                      "99) Exit the Social-Engineer Toolkit\n")

        self.prompt = "SET>"

    def do_1(self, line):
        SocialEngineeringAttacks(self.prompt).cmdloop()

    def do_2(self, line):
        FastTrack(self.prompt).cmdloop()

    def do_3(self, line):
        ThirdParyMods(self.prompt).cmdloop()

    def do_4(self, line):
        UpdateSET(self.prompt).cmdloop()

    def do_5(self, line):
        UpdateConfig(self.prompt).cmdloop()

    def do_6(self, line):
        return self.do_help(line)

    def do_hugs(self, line):
        print("Have you given someone a hug today? Remember a hug can change the world.")
        input("Please give someone a hug then press return to continue.")

    def do_freehugs(self, line):
        print("HUGS ARE ALWAYS FREE! NEVER CHARGE! ALWAYS HUG.")
        input("Do not press return until giving someone a hug.")

    def do_derbycon(self, line):
        print("{bold}YAYYYYYYYYYYYYYYYYYYYYYY DerbyCon.\n"
              "DerbyCon 6.0 'Recharge' -- September 23th - 25th 2016{end}".format(bold=bcolors.BOLD, end=bcolors.ENDC))
        input("\n{bold}Don't miss it! Sep 23 - Sep 25th! Press return to continue.{end}".format(bold=bcolors.BOLD, end=bcolors.ENDC))

    def do_rance(self, line):

        print("{bold}We miss you buddy. David Jones (Rance) changed a lot of us and "
              "you'll always be apart of our lives (and SET). Fuck Cancer.{end}".format(bold=bcolors.BOLD, end=bcolors.ENDC))
        input("Press return to continue.")

    def do_cavs(self, line):

        print("{bold}2015-2016 CHAMPS BABY!!! "
              "C l e e e e e  e v  eeee l a a n n d d d d d d d d d d d {end}".format(bold=bcolors.BOLD, end=bcolors.ENDC))
        input("Press return to continue.")

    def preloop(self):
        # if not config['accepted_license']:
        if True:
            AcceptLicense(self.prompt).cmdloop()
        print(random_graphic())
        print(intro_banner())

    def do_exit(self, args):
        print("Exiting gracefully")
        return True

    do_EOF = do_exit
    do_99 = do_exit
