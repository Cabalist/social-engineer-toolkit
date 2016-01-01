# coding=utf-8

from src.core_utils import check_config, cleanup_routine
from src.interface.main import SETToolkit


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


if __name__ == "__main__":

    check_config()

    try:
        SETToolkit().cmdloop()
    except KeyboardInterrupt:
        print(("\n\nThank you for {red}shopping{end} with the Social-Engineer Toolkit."
               "\n\nHack the Gibson...and remember...hugs are worth more "
               "than handshakes.\n".format(red=bcolors.RED, end=bcolors.ENDC)))
    finally:
        cleanup_routine()
