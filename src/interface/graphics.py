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


def set1():
    return bcolors.YELLOW + r"""
                 .--.  .--. .-----.
                : .--': .--'`-. .-'
                `. `. : `;    : :
                 _`, :: :__   : :
                `.__.'`.__.'  :_;   """ + bcolors.ENDC


def set2():
    return bcolors.GREEN + r"""
          _______________________________
         /   _____/\_   _____/\__    ___/
         \_____  \  |    __)_   |    |
         /        \ |        \  |    |
        /_______  //_______  /  |____|
                \/         \/            """ + bcolors.ENDC


def set3():
    return bcolors.BLUE + r"""
                :::===  :::===== :::====
                :::     :::      :::====
                 =====  ======     ===
                    === ===        ===
                ======  ========   ===
    """ + bcolors.ENDC


def set4():
    return bcolors.RED + r"""
               ..######..########.########
               .##....##.##..........##...
               .##.......##..........##...
               ..######..######......##...
               .......##.##..........##...
               .##....##.##..........##...
               ..######..########....##...  """ + bcolors.ENDC


def set5():
    return bcolors.PURPLE + r'''
             .M"""bgd `7MM"""YMM MMP""MM""YMM
            ,MI    "Y   MM    `7 P'   MM   `7
            `MMb.       MM   d        MM
              `YMMNq.   MMmmMM        MM
            .     `MM   MM   Y  ,     MM
            Mb     dM   MM     ,M     MM
            P"Ybmmd"  .JMMmmmmMMM   .JMML.''' + bcolors.ENDC


def set6():
    return bcolors.YELLOW + r"""
                  ________________________
                  __  ___/__  ____/__  __/
                  _____ \__  __/  __  /
                  ____/ /_  /___  _  /
                  /____/ /_____/  /_/     """ + bcolors.ENDC


def set7():
    return bcolors.RED + r'''
              !\_________________________/!\
              !!                         !! \
              !! Social-Engineer Toolkit !!  \
              !!                         !!  !
              !!          Free           !!  !
              !!                         !!  !
              !!          #hugs          !!  !
              !!                         !!  !
              !!      By: TrustedSec     !!  /
              !!_________________________!! /
              !/_________________________\!/
                 __\_________________/__/!_
                !_______________________!/
              ________________________
             /oooo  oooo  oooo  oooo /!
            /ooooooooooooooooooooooo/ /
           /ooooooooooooooooooooooo/ /
          /C=_____________________/_/''' + bcolors.ENDC


def binary():
    return bcolors.YELLOW + """
         01011001011011110111010100100000011100
         10011001010110000101101100011011000111
         10010010000001101000011000010111011001
         10010100100000011101000110111100100000
         01101101011101010110001101101000001000
         00011101000110100101101101011001010010
         00000110111101101110001000000111100101
         10111101110101011100100010000001101000
         01100001011011100110010001110011001000
         00001110100010110100101001001000000101
         01000110100001100001011011100110101101
         11001100100000011001100110111101110010
         00100000011101010111001101101001011011
         10011001110010000001110100011010000110
         01010010000001010011011011110110001101
         10100101100001011011000010110101000101
         01101110011001110110100101101110011001
         01011001010111001000100000010101000110
         11110110111101101100011010110110100101
         11010000100000001010100110100001110101
         011001110111001100101010""" + bcolors.ENDC


def trusted_sec_badge():
    return bcolors.GREEN + """
                          .  ..
                       MMMMMNMNMMMM=
                   .DMM.           .MM$
                 .MM.                 MM,.
                 MN.                    MM.
               .M.                       MM
              .M   .....................  NM
              MM   .8888888888888888888.   M7
             .M    88888888888888888888.   ,M
             MM       ..888.MMMMM    .     .M.
             MM         888.MMMMMMMMMMM     M
             MM         888.MMMMMMMMMMM.    M
             MM         888.      NMMMM.   .M
              M.        888.MMMMMMMMMMM.   ZM
              NM.       888.MMMMMMMMMMM    M:
              .M+      .....              MM.
               .MM.                     .MD
                 MM .                  .MM
                  $MM                .MM.
                    ,MM?          .MMM
                       ,MMMMMMMMMMM

                https://www.trustedsec.com""" + bcolors.ENDC


def tardis():
    return bcolors.backBlue + r"""
                              _                                           J
                             /-\                                          J
                        _____|#|_____                                     J
                       |_____________|                                    J
                      |_______________|                                   E
                     ||_POLICE_##_BOX_||                                  R
                     | |-|-|-|||-|-|-| |                                  O
                     | |-|-|-|||-|-|-| |                                  N
                     | |_|_|_|||_|_|_| |                                  I
                     | ||~~~| | |---|| |                                  M
                     | ||~~~|!|!| O || |                                  O
                     | ||~~~| |.|___|| |                                  O
                     | ||---| | |---|| |                                  O
                     | ||   | | |   || |                                  O
                     | ||___| | |___|| |                                  !
                     | ||---| | |---|| |                                  !
                     | ||   | | |   || |                                  !
                     | ||___| | |___|| |                                  !
                     |-----------------|                                  !
                     |   Timey Wimey   |                                  !
                     -------------------                                  !""" + bcolors.ENDC


def cavs():
    return bcolors.YELLOW + r'''
           ,..-,
         ,;;f^^"""-._
        ;;'          `-.
       ;/               `.
       ||  _______________\_______________________
       ||  |HHHHHHHHHHPo"~~\"o?HHHHHHHHHHHHHHHHHHH|
       ||  |HHHHHHHHHP-._   \,'?HHHHHHHHHHHHHHHHHH|
        |  |HP;""?HH|    """ |_.|HHP^^HHHHHHHHHHHH|
        |  |HHHb. ?H|___..--"|  |HP ,dHHHPo'|HHHHH|
        `| |HHHHHb.?Hb    .--J-dHP,dHHPo'_.rdHHHHH|
         \ |HHHi.`;;.H`-./__/-'H_,--'/;rdHHHHHHHHH|
           |HHHboo.\ `|"\"/"\" '/\ .'dHHHHHHHHHHHH|
           |HHHHHHb`-|.  \|  \ / \/ dHHHHHHHHHHHHH|
           |HHHHHHHHb| \ |\   |\ |`|HHHHHHHHHHHHHH|
           |HHHHHHHHHb  \| \  | \| |HHHHHHHHHHHHHH|
           |HHHHHHHHHHb |\  \|  |\|HHHHHHHHHHHHHHH|
           |HHHHHHHHHHHb| \  |  / dHHHHHHHHHHHHHHH|
           |HHHHHHHHHHHHb  \/ \/ .fHHHHHHHHHHHHHHH|
           |HHHHHHHHHHHHH| /\ /\ |HHHHHHHHHHHHHHHH|
           |""""""""""""""""""""""""""""""""""""""|
           |,;=====.     ,-.  =.       ,=,,=====. |
           |||     '    //"\\   \\   //  ||     ' |
           |||         ,/' `\.  `\. ,/'  ``=====. |
           |||     .   //"""\\   \\_//    .     |||
           |`;=====' =''     ``=  `-'     `=====''|
           |______________________________________|
''' + bcolors.ENDC


def skull():
    return bcolors.RED + r"""
                          ..:::::::::..
                      ..:::aad8888888baa:::..
                  .::::d:?88888888888?::8b::::.
                .:::d8888:?88888888??a888888b:::.
              .:::d8888888a8888888aa8888888888b:::.
             ::::dP::::::::88888888888::::::::Yb::::
            ::::dP:::::::::Y888888888P:::::::::Yb::::
           ::::d8:::::::::::Y8888888P:::::::::::8b::::
          .::::88::::::::::::Y88888P::::::::::::88::::.
          :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
          :::::::Y88888888888P::|::Y88888888888P:::::::
          ::::::::::::::::888:::|:::888::::::::::::::::
          `:::::::::::::::8888888888888b::::::::::::::'
           :::::::::::::::88888888888888::::::::::::::
            :::::::::::::d88888888888888:::::::::::::
             ::::::::::::88::88::88:::88::::::::::::
              `::::::::::88::88::88:::88::::::::::'
                `::::::::88::88::P::::88::::::::'
                  `::::::88::88:::::::88::::::'
                     ``:::::::::::::::::::''
                          ``:::::::::''""" + bcolors.ENDC


def fsociety():
    return bcolors.BOLD + """
            cddddddddddddddddddddddddddddddddddddddddddd;
            0Mo..........':ldkO0KKXXKK0kxoc,..........kMd
            0Ml......;d0WMMMMMMMMMMMMMMMMMMMWKx:......kMd
            0Ml...cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMWO:...kMd
            0Ml.lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc.kMd
            0MdKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0OMd
            0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd
            0MxcxWMMMMMNXXNMMMMMMMMMMMMMMMNXXNMMMMMWkcKMd
            0Md..lMKo,.,'...:kWMMMMMMMNx;...',.;dXMl.'XMd
            0Mx'.,O;dXMMMXl....:dWMNo;....oXMMMKd;0,.'KMd
            0MO;.,NMWMMMMMMWk;...XMK...:OWMMMMMMWMN,.cNMd
            0MxxNMX;KMMKdcclkWN0WMMMN0WNxc:lxXMMk;WMXdKMd
            0MMMMMO;MMl.......KMXOMNkMk.......xMM.NMMMMMd
            0MMMMMMXKoclddl;.oWMdkMN,MN:.:ldolcdXNMMMMMMd
            0MMMMMMWXMMMMMMMW0KdoNMMdox0MMMMMMMMXMMMMMMMd
            0MMMMXc'WMMMMMMMMkcWMMMMMMkcMMMMMMMMN'lXMMMMd
            0MMMd..cMMMMMMMMNdoKMMMMM0x:XMMMMMMMM:..kMMMd
            0MM0....d0KKOd:.....c0Kx'.....:d0NX0l....NMMd
            0MMO.....................................WMMd
            0Mdkc...................................0kOMd
            0Ml.:Ol;........';;.......;,........':oX:.kMd
            0Ml..,WMMMMWWWo...';;:c::;'...:WWMMMMMW;..kMd
            0Ml...dMMMMMMMMKl...........c0MMMMMMMMd...kMd
            0Ml...cMMMMMMMMMMMXOxdddk0NMMMMMMMMMMM'...kMd
            0Ml....KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO....kMd
            0Ml.....OMMMMMMMMMMMMMMMMMMMMMMMMMMMK.....kMd
            0Ml......:XMMMMMMMMMMMMMMMMMMMMMMMNl......kMd
            0Ml........lXMMMMMMMMMMMMMMMMMMMKc........kMd
            0Ml..........:KMMMMMMMMMMMMMMM0,..........kMd
            oO:............xOOOx:'';dOOOOd............lOc""" + bcolors.ENDC
