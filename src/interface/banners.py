# coding=utf-8

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


def intro_banner():
    return ("{blue}[---]        The Social-Engineer Toolkit ({yellow}SET{blue})         [---]{end}"
            "{blue}[---]        Created by:{red} David Kennedy {blue}({yellow}ReL1K{blue})         [---]{end}"
            "{blue}                Version: {red}Version INFO goes here{end}"
            "{blue}                  Codename: '{yellow}Underground'{end}"
            "{blue}[---]        Follow us on Twitter: {purple}@TrustedSec{blue}         [---]{end}"
            "{blue}[---]        Follow me on Twitter: {purple}@HackingDave{blue}        [---]{end}"
            "{blue}[---]       Homepage: {yellow}https://www.trustedsec.com{blue}       [---]{end}"
            "{green}        Welcome to the Social-Engineer Toolkit (SET).{end}"
            "{green}         The one stop shop for all of your SE needs.{end}"
            "{blue}     Join us on irc.freenode.net in channel #setoolkit{end}"
            "{bold}   The Social-Engineer Toolkit is a product of TrustedSec.){end}"
            "{end}"
            "{end}"
            "{blue}           Visit: {green}https://www.trustedsec.com{end}"
            "{blue}   It's easy to update using the PenTesters Framework! (PTF){end}"
            "{blue}Visit {yellow}https://github.com/trustedsec/ptf{blue} to update all your tools!{end}"
            .format(blue=bcolors.BLUE, red=bcolors.RED, green=bcolors.GREEN, yellow=bcolors.YELLOW,
                    purple=bcolors.PURPLE, bold=bcolors.BOLD, end=bcolors.ENDC + "\n"))


def license_text():
    with open("readme/LICENSE") as fileopen:
        return fileopen.read()


def disclaimer():
    return ("{0}The Social-Engineer Toolkit is designed purely"
            " for good and not evil. If you are planning on "
            "using this tool for malicious purposes that are "
            "not authorized by the company you are performing "
            "assessments for, you are violating the terms of "
            "service and license of this toolset. By hitting "
            "yes (only one time), you agree to the terms of "
            "service and that you will only use this tool for "
            "lawful purposes only.{1}".format(bcolors.RED, bcolors.ENDC))
