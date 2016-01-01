# coding=utf-8
import os
import sys

from banners import disclaimer, license_text
from utils import SubCmd, YesNoCmd
from ..config import CONFIG

# Py2/3 compatibility
# Python3 renamed raw_input to input
try:
    input = raw_input
except NameError:
    pass


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


class AcceptLicense(YesNoCmd):
    def __init__(self, *args, **kwargs):
        super(AcceptLicense, self).__init__(*args, **kwargs)
        self.intro = "{0}Do you agree to the terms of service [y/n]: {1}".format(bcolors.GREEN, bcolors.ENDC)

    def preloop(self):
        print(license_text())
        print(disclaimer())

    def do_yes(self, line):
        CONFIG['accepted_license'] = True
        CONFIG.write()
        return True

    def do_no(self, line):
        print("{0}[!] Exiting the Social-Engineer Toolkit, have a nice day.{1}".format(bcolors.RED, bcolors.ENDC))
        sys.exit()


class SocialEngineeringAttacks(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(SocialEngineeringAttacks, self).__init__(prompt, *args, **kwargs)
        self.intro = ("Select from the following options:\n"
                      "1) Spear-Phishing Attack Vectors\n"
                      "2) Website Attack Vectors\n"
                      "3) Infectious Media Generator\n"
                      "4) Create a Payload and Listener\n"
                      "5) Mass Mailer Attack\n"
                      "6) Arduino-Based Attack Vector\n"
                      "7) Wireless Access Point Attack Vector\n"
                      "8) QRCode Generator Attack Vector\n"
                      "9) Powershell Attack Vectors\n"
                      "10) SMS Spoofing Attack Vector\n"
                      "11) Third Party Modules\n"
                      "99) Return to previous menu\n")

    def do_1(self, line):
        SpearFishing(self.prompt).cmdloop()

    def do_2(self, line):
        #     show_webattack_menu = create_menu( text.webattack_text, text.webattack_menu)
        #     attack_vector = raw_input(setprompt(["2"], ""))
        #     choice3 = ""
        #
        #     # full screen attack vector
        #     if attack_vector == '7':
        #         # dont need site cloner
        #         site_cloned = False
        #         # skip nat section and exit out
        #         choice3 = "-1"
        #         import full
        #
        #     # Removed to delete MLITM
        #     if attack_vector != "99999":
        #
        #         #
        #         # USER INPUT: SHOW WEB ATTACK VECTORS MENU    #
        #         #
        #
        #         if attack_vector != "7":
        #             show_webvectors_menu = create_menu( text.webattack_vectors_text, text.webattack_vectors_menu)
        #             choice3 = raw_input(setprompt(["2"], ""))
        #
        #
        #     try:
        #         # write our attack vector to file to be called later
        #         filewrite = open(setdir + "/attack_vector", "w")
        #
        #         # webjacking and web templates are not allowed
        #         if attack_vector == "5" and choice3 == "1":
        #             print( bcolors.RED + "\n Sorry, you can't use the Web Jacking vector with Web Templates." + bcolors.ENDC)
        #             break
        #
        #         # if we select multiattack, web templates are not allowed
        #         if attack_vector == "6" and choice3 == "1":
        #             print( bcolors.RED + "\n Sorry, you can't use the Multi-Attack vector with Web Templates." + bcolors.ENDC)
        #             break
        #
        #         # if we select web template and tabnabbing, throw this
        #         # error and bomb out to menu
        #         if attack_vector == "4" and choice3 == "1":
        #             print( bcolors.RED + "\n Sorry, you can only use the cloner option with the tabnabbing method." + bcolors.ENDC)
        #             break
        #
        #         # specify java applet attack
        #         if attack_vector == '1':
        #             attack_vector = "java"
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #
        #         # specify browser exploits
        #         if attack_vector == '2':
        #             attack_vector = "browser"
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #
        #         if attack_vector == '':
        #             attack_vector = '3'
        #         # specify web harvester method
        #         if attack_vector == '3':
        #             attack_vector = "harvester"
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #             print_info( "Credential harvester will allow you to utilize the clone capabilities within SET")
        #             print_info( "to harvest credentials or parameters from a website as well as place them into a report")
        #
        #         # specify tab nabbing attack vector
        #         if attack_vector == '4':
        #             attack_vector = "tabnabbing"
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #
        #         # specify webjacking attack vector
        #         if attack_vector == "5":
        #             attack_vector = "webjacking"
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #
        #         # specify Multi-Attack Vector
        #         attack_vector_multi = ""
        #         if attack_vector == '6':
        #             # trigger the multiattack flag in SET
        #             attack_vector = "multiattack"
        #             # write the attack vector to file
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #
        #         # hta attack vector
        #         if attack_vector == '8':
        #             # call hta attack vector
        #             attack_vector = "hta"
        #             filewrite.write(attack_vector)
        #             filewrite.close()
        #
        #         # pull ip address
        #         if choice3 != "-1":
        #             fileopen = open( "/etc/setoolkit/set.config", "r").readlines()
        #             for line in fileopen:
        #                 line = line.rstrip()
        #                 match = re.search("AUTO_DETECT=ON", line)
        #                 if match:
        #                     try:
        #                         ipaddr = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
        #                         ipaddr.connect(('google.com', 0))
        #                         ipaddr.settimeout(2)
        #                         ipaddr = ipaddr.getsockname()[0]
        #                         update_options("IPADDR=" + ipaddr)
        #                     except Exception as error:
        #                         log(error)
        #                         ipaddr = raw_input( setprompt(["2"], "Your interface IP Address"))
        #                         update_options("IPADDR=" + ipaddr)
        #
        #             # if AUTO_DETECT=OFF prompt for IP Address
        #             for line in fileopen:
        #                 line = line.rstrip()
        #                 match = re.search("AUTO_DETECT=OFF", line)
        #                 if match:
        #                     if attack_vector != "harvester":
        #                         if attack_vector != "tabnabbing":
        #                             if attack_vector != "webjacking":
        #                                 if attack_vector != "hta":
        #                                     # this part is to determine if NAT/port forwarding is used
        #                                     # if it is it'll prompt for
        #                                     # additional questions
        #                                     print_info( "NAT/Port Forwarding can be used in the cases where your SET machine is")
        #                                     print_info( "not externally exposed and may be a different IP address than your reverse listener.")
        #                                     nat_or_fwd = yesno_prompt( '0', 'Are you using NAT/Port Forwarding [yes|no]')
        #                                     if nat_or_fwd == "YES":
        #                                         ipquestion = raw_input(setprompt( ["2"], "IP address to SET web server (this could be your external IP or hostname)"))
        #
        #                                         filewrite2 = open( setdir + "/interface", "w")
        #                                         filewrite2.write( ipquestion)
        #                                         filewrite2.close()
        #                                         # is your payload/listener
        #                                         # on a different IP?
        #                                         natquestion = yesno_prompt( ["2"], "Is your payload handler (metasploit) on a different IP from your external NAT/Port FWD address [yes|no]")
        #                                         if natquestion == 'YES':
        #                                             ipaddr = raw_input( setprompt(["2"], "IP address for the reverse handler (reverse payload)"))
        #                                         if natquestion == "NO":
        #                                             ipaddr = ipquestion
        #                                     # if you arent using NAT/Port
        #                                     # FWD
        #                                     if nat_or_fwd == "NO":
        #                                         print_info( "Enter the IP address of your interface IP or if your using an external IP, what")
        #                                         print_info( "will be used for the connection back and to house the web server (your interface address)")
        #                                         ipaddr = raw_input( setprompt(["2"], "IP address or hostname for the reverse connection"))
        #                                         # here we check if they are
        #                                         # using a hostname else we
        #                                         # loop through until they
        #                                         # have a legit one
        #                                         if validate_ip(ipaddr) == False:
        #                                             while 1:
        #                                                 choice = raw_input(setprompt( ["2"], "This is not an IP address. Are you using a hostname? [y/n] "))
        #                                                 if choice == "" or choice.lower() == "y":
        #                                                     print_status( "Roger that. Using hostnames moving forward..")
        #                                                     break
        #                                                 else:
        #                                                     ipaddr = raw_input( setprompt(["2"], "IP address for the reverse connection"))
        #                                                     if validate_ip(ipaddr) == True:
        #                                                         break
        #
        #                     if attack_vector == "harvester" or attack_vector == "tabnabbing" or attack_vector == "webjacking":
        #                         print_info( "This option is used for what IP the server will POST to.")
        #                         print_info( "If you're using an external IP, use your external IP for this")
        #                         ipaddr = raw_input( setprompt(["2"], "IP address for the POST back in Harvester/Tabnabbing"))
        #
        #                     if check_options("IPADDR=") != 0:
        #                         ipaddr = check_options("IPADDR=")
        #                         update_options("IPADDR=" + ipaddr)
        #                     else:
        #                         if ipaddr != "":
        #                             update_options("IPADDR=" + ipaddr)
        #
        #             # if java applet attack
        #             if attack_vector == "java":
        #                 applet_choice()
        #
        #         # Select SET quick setup
        #         if choice3 == '1':
        #
        #             # get the template ready
        #             import template
        #
        #             # grab browser exploit selection
        #             if attack_vector == "browser":
        #                 # grab clientattack
        #                 import gen_payload
        #
        #             # arp cache attack, will exit quickly
        #             # if not in config file
        #             import arp
        #
        #             # actual website attack here
        #             # web_server.py is main core
        #
        #             # clean up stale file
        #             if os.path.isfile(setdir + "/cloner.failed"):
        #                 os.remove(setdir + "/cloner.failed")
        #
        #             site_cloned = True
        #
        #             import src.webattack.web_clone.cloner
        #
        #             # grab java applet attack
        #             if attack_vector == "java":
        #                 import src.core.payloadgen.create_payloads
        #
        #             if os.path.isfile(setdir + "/cloner.failed"):
        #                 site_cloned = False
        #
        #             if site_cloned == True:
        #
        #                 # cred harvester for auto site here
        #                 if attack_vector == "harvester" or attack_vector == "tabnabbing" or attack_vector == "webjacking":
        #                     if attack_vector == "tabnabbing" or attack_vector == "webjacking":
        #                         import src.webattack.tabnabbing
        #                     # start web cred harvester here
        #                     import harvester
        #
        #                 # if we are using profiler lets prep everything to
        #                 # get ready
        #                 if attack_vector == "profiler":
        #                     from src.webattack.profiler.webprofiler import *
        #
        #                     prep_website()
        #
        #                 # launch HTA attack vector after the website has
        #                 # been cloned
        #                 if attack_vector == "hta":
        #                     # launch HTA attack vector after the website
        #                     # has been cloned
        #                     from src.webattack.hta.main import *
        #
        #                     # update config
        #                     update_options("ATTACK_VECTOR=HTA")
        #                     gen_hta_cool_stuff()
        #                     attack_vector = "hta"
        #                     print_status( "Automatically starting Apache for you...")
        #                     subprocess.Popen( "service apache2 start", shell=True).wait()
        #
        #                 if attack_vector != "harvester" and
        #                    attack_vector != "tabnabbing" and
        #                    attack_vector != "multiattack" and
        #                    attack_vector != "webjacking" and
        #                    attack_vector != "multiattack" and
        #                    attack_vector != "profiler" and
        #                    attack_vector != "hta":
        #                        # spawn web server here
        #                        import src.html.spawn
        #
        #                 # multi attack vector here
        #                 if attack_vector == "multiattack":
        #                     if choice3 == "1":
        #                         filewrite = open( "src/progam_junk/multiattack.template", "w")
        #                         filewrite.write("TEMPLATE=TRUE")
        #                         filewrite.close()

        #                         import src.webattack.multi_attack.multiattack
        #
        #         # Create a website clone
        #         if choice3 == '2':
        #             # flag that we want a custom website
        #             definepath = os.getcwd()
        #             if os.path.isfile(setdir + "/site.template"):
        #                 os.remove(setdir + "/site.template")
        #             filewrite = open(setdir + "/site.template", "w")
        #             filewrite.write("TEMPLATE=CUSTOM")
        #             print_info("SET supports both HTTP and HTTPS")
        #             # specify the site to clone
        #             print_info("Example: http://www.thisisafakesite.com")
        #             URL = raw_input( setprompt(["2"], "Enter the url to clone"))
        #             match = re.search("http://", URL)
        #             match1 = re.search("https://", URL)
        #             if not match:
        #                 if not match1:
        #                     URL = ("http://" + URL)
        #
        #             match2 = re.search("facebook.com", URL)
        #             if match2:
        #                 URL = ("https://login.facebook.com/login.php")
        #
        #             # changed based on new landing page for gmail.com
        #             match3 = re.search("gmail.com", URL)
        #             if match3:
        #                 URL = ("https://accounts.google.com")
        #
        #             filewrite.write("\nURL=%s" % (URL))
        #             filewrite.close()
        #
        #             # launch HTA attack vector after the website has been
        #             # cloned
        #             if attack_vector == "hta":
        #                 # launch HTA attack vector after the website has
        #                 # been cloned
        #                 from src.webattack.hta.main import *
        #
        #                 # update config
        #                 update_options("ATTACK_VECTOR=HTA")
        #                 gen_hta_cool_stuff()
        #                 attack_vector = "hta"
        #                 print_status( "Automatically starting Apache for you...")
        #                 subprocess.Popen( "service apache2 start", shell=True).wait()
        #
        #             # grab browser exploit selection
        #             if attack_vector == "browser":
        #                 # grab clientattack
        #                 import gen_payload
        #
        #             # set site cloner to true
        #             site_cloned = True
        #
        #             if attack_vector != "multiattack":
        #                 # import our website cloner
        #
        #                 site_cloned = True
        #                 import src.webattack.web_clone.cloner
        #
        #                 if os.path.isfile(setdir + "/cloner.failed"):
        #                     site_cloned = False
        #
        #             if site_cloned == True:
        #
        #                 if attack_vector == "java":
        #                     # import our payload generator
        #                     import src.core.payloadgen.create_payloads
        #
        #                 # arp cache if applicable
        #                 definepath = os.getcwd()
        #                 import arp
        #
        #                 # tabnabbing and harvester selection here
        #                 if attack_vector == "harvester" or attack_vector == "tabnabbing" or attack_vector == "webjacking":
        #                     if attack_vector == "tabnabbing" or attack_vector == "webjacking":
        #                         import tabnabbing
        #
        #                     import harvester
        #
        #                 # multi_attack vector here
        #                 if attack_vector == "multiattack":
        #                     import multiattack
        #
        #                 # if we arent using credential harvester or
        #                 # tabnabbing
        #                 if attack_vector != "harvester":
        #                     if attack_vector != "tabnabbing":
        #                         if attack_vector != "multiattack":
        #                             if attack_vector != "webjacking":
        #                                 if attack_vector != "hta":
        #                                     import spawn
        #
        #         # Import your own site
        #         if choice3 == '3':
        #
        #             if os.path.isfile(setdir + "/site.template"):
        #                 os.remove(setdir + "/site.template")
        #             filewrite = open(setdir + "/site.template", "w")
        #             filewrite.write("TEMPLATE=SELF")
        #             # specify the site to clone
        #             if not os.path.isdir(setdir + "/web_clone"):
        #                 os.makedirs(setdir + "/web_clone")
        #             print_warning( "Example: /home/website/ (make sure you end with /)")
        #             print_warning( "Also note that there MUST be an index.html in the folder you point to.")
        #             URL = raw_input( setprompt(["2"], "Path to the website to be cloned"))
        #             if not URL.endswith("/"):
        #                 if not URL.endswith("index.html"):
        #                     URL = URL + "/"
        #             if not os.path.isfile(URL + "index.html"):
        #                 if os.path.isfile(URL):
        #                     shutil.copyfile( "%s" % (URL), setdir + "/web_clone/index.html")
        #                 if not os.path.isfile(URL):
        #                     if URL.endswith("index.html"):
        #                         shutil.copyfile( URL, "%s/web_clone/index.html" % (setdir))
        #                     else:
        #                         print_error("ERROR:index.html not found!!")
        #                         print_error( "ERROR:Did you just put the path in, not file?")
        #                         print_error( "Exiting the Social-Engineer Toolkit...Hack the Gibson.\n")
        #                         exit_set()
        #
        #             if os.path.isfile(URL + "index.html"):
        #                 print_status( "Index.html found. Do you want to copy the entire folder or just index.html?")
        #                 choice = raw_input( "\n1. Copy just the index.html\n2. Copy the entire folder\n\nEnter choice [1/2]: ")
        #                 if choice == "1" or choice == "":
        #                     if os.path.isfile("%s/web_clone/index.html" % (setdir)):
        #                         os.remove( "%s/web_clone/index.html" % (setdir))
        #                     shutil.copyfile( URL + "index.html", "%s/web_clone/" % (setdir))
        #                 if choice == "2":
        #                     if os.path.isdir(URL + "src/webattack"):
        #                         print_error( "You cannot specify a folder in the default SET path. This goes into a loop Try something different.")
        #                         URL = raw_input( "Enter the folder to import into SET, this CANNOT be the SET directory: ")
        #                         if os.path.isdir(URL + "src/webattack" % (URL)):
        #                             print_error( "You tried the same thing. Exiting now.")
        #                             sys.exit()
        #                     copyfolder(URL, "%s/web_clone/" % setdir)
        #
        #             filewrite.write("\nURL=%s" % (URL))
        #             filewrite.close()
        #
        #             # if not harvester then load up cloner
        #             if attack_vector == "java" or attack_vector == "browser":
        #                 # import our website cloner
        #                 import src.webattack.web_clone.cloner
        #
        #             # launch HTA attack vector after the website has been
        #             # cloned
        #             if attack_vector == "hta":
        #                 # launch HTA attack vector after the website has
        #                 # been cloned
        #                 from src.webattack.hta.main import *
        #
        #                 # update config
        #                 update_options("ATTACK_VECTOR=HTA")
        #                 gen_hta_cool_stuff()
        #                 attack_vector = "hta"
        #                 print_status( "Automatically starting Apache for you...")
        #                 subprocess.Popen( "service apache2 start", shell=True).wait()
        #
        #             # if java applet attack
        #             if attack_vector == "java":
        #                 # import our payload generator
        #
        #                 import src.core.payloadgen.create_payloads
        #
        #             # grab browser exploit selection
        #             if attack_vector == "browser":
        #                 # grab clientattack
        #                 import gen_payload
        #
        #             # arp cache if applicable
        #             import arp
        #
        #             # if not harvester spawn server
        #             if attack_vector == "java" or attack_vector == "browser":
        #                 # import web_server and do magic
        #                 import spawn
        #
        #             # cred harvester for auto site here
        #             if attack_vector == "harvester":
        #                 # get the url
        #                 print_info("Example: http://www.blah.com")
        #                 URL = raw_input( setprompt(["2"], "URL of the website you imported"))
        #                 match = re.search("http://", URL)
        #                 match1 = re.search("https://", URL)
        #                 if not match:
        #                     if not match1:
        #                         URL = ("http://" + URL)
        #                 filewrite = open(setdir + "/site.template", "w")
        #                 filewrite.write("\nURL=%s" % (URL))
        #                 filewrite.close()
        #
        #                 # start web cred harvester here
        #                 import harvester
        #
        #             # tabnabbing for auto site here
        #             if attack_vector == "tabnabbing" or attack_vector == "webjacking":
        #                 # get the url
        #                 print_info("Example: http://www.blah.com")
        #                 URL = raw_input( setprompt(["2"], "URL of the website you imported"))
        #                 match = re.search("http://", URL)
        #                 match1 = re.search("https://", URL)
        #                 if not match:
        #                     if not match1:
        #                         URL = ("http://" + URL)
        #                 filewrite = open(setdir + "/site.template", "w")
        #                 filewrite.write("\nURL=%s" % (URL))
        #                 filewrite.close()
        #                 # start tabnabbing here
        #                 import tabnabbing
        #
        #                 # start web cred harvester here
        #                 import harvester
        #
        #             # multi attack vector here
        #             if attack_vector == "multiattack":
        #                 filewrite = open( "src/progam_junk/multiattack.template", "w")
        #                 filewrite.write("TEMPLATE=TRUE")
        #                 filewrite.close()

        #                 import src.webattack.multi_attack.multiattack
        pass

    def do_3(self, line):
        Infect(self.prompt).cmdloop()
        pass

    def do_4(self, line):
        # update_options("PAYLOADGEN=SOLO")
        # import src.core.payloadgen.solo
        #
        # if os.path.isfile(setdir + "/msf.exe"):
        #     shutil.copyfile(setdir + "/msf.exe", "payload.exe")
        pass

    def do_5(self, line):
        # import src.phishing.smtp.client.smtp_web
        pass

    def do_6(self, line):
        Teensy(self.prompt).cmdloop()

    def do_7(self, line):
        airbase_path = CONFIG['AIRBASE_NG_PATH']
        dnsspoof_path = CONFIG['DNSSPOOF_PATH']

        if not os.path.isfile(airbase_path):
            print("Warning airbase-ng was not detected on your system. Using one in SET.")
            print("If you experience issues, you should install airbase-ng on your system.")
            print("You can configure it through the set_config and point to airbase-ng.")
            airbase_path = ("src/wireless/airbase-ng")

        if not os.path.isfile(dnsspoof_path):
            if os.path.isfile("/usr/local/sbin/dnsspoof"):
                dnsspoof_path = "/usr/local/sbin/dnsspoof"
            if os.path.isfile("/usr/sbin/dnsspoof"):
                dnsspoof_path = "/usr/sbin/dnsspoof"

        Wireless(self.prompt).cmdloop()

    def do_8(self, line):
        print("The QRCode Attack Vector will create a QRCode for you with "
              "whatever URL you want.\n\nWhen you have the QRCode Generated, "
              "select an additional attack vector within SET and deploy "
              "the QRCode to your victim. For example, generate a QRCode of"
              " the SET Java Applet and send the QRCode via a mailer.")

        url = input("Enter the URL you want the QRCode to go to: ")

        # gen_qrcode(url)

    def do_9(self, line):
        # import src.powershell.powershell
        pass

    def do_10(self, line):
        # import src.sms.sms
        pass

    def do_11(self, line):
        # import module_handler
        pass


class FastTrack(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(FastTrack, self).__init__(prompt, *args, **kwargs)


class ThirdParyMods(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(ThirdParyMods, self).__init__(prompt, *args, **kwargs)


class UpdateSET(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(UpdateSET, self).__init__(prompt, *args, **kwargs)


class UpdateConfig(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(UpdateConfig, self).__init__(prompt, *args, **kwargs)


class SpearFishing(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(SpearFishing, self).__init__(prompt, *args, **kwargs)

        self.intro = ("The {bold}Spearphishing{end} module allows you to specially "
                      "craft email messages and send them to a large (or small) "
                      "number of people with attached file format malicious payloads. "
                      "If you want to spoof your email address, be sure 'Sendmail' "
                      "is installed (apt-get install sendmail) and change the "
                      "config/set_config SENDMAIL=OFF flag to SENDMAIL=ON. There "
                      "are two options, one is getting your feet wet and letting "
                      "SET do everything for you (option 1), the second is to "
                      "create your own FileFormat payload and use it in your "
                      "own attack. Either way, good luck and enjoy!\n\n"
                      "1) Perform a Mass Email Attack\n"
                      "2) Create a FileFormat Payload\n"
                      "3) Create a Social-Engineering Template\n"
                      "99) Return to previous menu\n".format(bold=bcolors.BOLD, end=bcolors.ENDC))

    def do_1(self, line):
        # import create_payload
        pass

    def do_2(self, line):
        # import create_payload
        pass

    def do_3(self, line):
        # custom_template()
        pass


class Wireless(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(Wireless, self).__init__(prompt, *args, **kwargs)
        self.intro = ("The {bold}Wireless Attack{end} module will create an access point leveraging your"
                      "wireless card and redirect all DNS queries to you. The concept is fairly"
                      "simple, SET will create a wireless access point, dhcp server, and spoof"
                      "DNS to redirect traffic to the attacker machine. It will then exit out"
                      "of that menu with everything running as a child process.\n"
                      "You can then launch any SET attack vector you want, for example the Java "
                      "Applet attack and when a victim joins your access point and tries going to "
                      "a website, will be redirected to your attacker machine.\n"
                      "This attack vector requires AirBase-NG, AirMon-NG, DNSSpoof, and dhcpd3.\n"
                      "1) Start the SET Wireless Attack Vector Access Point\n"
                      "2) Stop the SET Wireless Attack Vector Access Point\n"
                      )

    def do_1(self, line):
        # import wifiattack
        pass

    def do_2(self, line):
        # import stop_wifiattack
        pass


class Teensy(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(Teensy, self).__init__(prompt, *args, **kwargs)

        self.intro = ("The {bold}Arduino-Based Attack{end} Vector utilizes the Arduin-based device to\n"
                      "program the device. You can leverage the Teensy's, which have onboard\n"
                      "storage and can allow for remote code execution on the physical\n"
                      "system. Since the devices are registered as USB Keyboard's it\n"
                      "will bypass any autorun disabled or endpoint protection on the\n"
                      "system.\n\n"
                      "You will need to purchase the Teensy USB device, it's roughly\n"
                      "$22 dollars. This attack vector will auto generate the code\n"
                      "needed in order to deploy the payload on the system for you.\n\n"
                      "This attack vector will create the .pde files necessary to import\n"
                      "into Arduino (the IDE used for programming the Teensy). The attack\n"
                      "vectors range from Powershell based downloaders, wscript attacks,\n"
                      "and other methods.\n\n"
                      "For more information on specifications and good tutorials visit:\n\n"
                      "http://www.irongeek.com/i.php?page=security/programmable-hid-usb-keystroke-dongle\n\n"
                      "To purchase a Teensy, visit: http://www.pjrc.com/store/teensy.html\n"
                      "Special thanks to: IronGeek, WinFang, and Garland\n\n"
                      "This attack vector also attacks X10 based controllers, be sure to be leveraging\n"
                      "X10 based communication devices in order for this to work.\n\n"
                      "Select a payload to create the pde file to import into Arduino:\n\n"

                      "1) Powershell HTTP GET MSF Payload\n"
                      "2) WSCRIPT HTTP GET MSF Payload\n"
                      "3) Powershell based Reverse Shell Payload\n"
                      "4) Internet Explorer/FireFox Beef Jack Payload\n"
                      "5) Go to malicious java site and accept applet Payload\n"
                      "6) Gnome wget Download Payload\n"
                      "7) Binary 2 Teensy Attack (Deploy MSF payloads)\n"
                      "8) SDCard 2 Teensy Attack (Deploy Any EXE)\n"
                      "9) SDCard 2 Teensy Attack (Deploy on OSX)\n"
                      "10) X10 Arduino Sniffer PDE and Libraries\n"
                      "11) X10 Arduino Jammer PDE and Libraries\n"
                      "12) Powershell Direct ShellCode Teensy Attack\n"
                      "13) Peensy Multi Attack Dip Switch + SDCard Attack\n"
                      "99) Return to previous menu\n".format(bold=bcolors.BOLD, end=bcolors.ENDC))

        # This code is executed on this options selection.  It seems to create files with some values
        #  that are read later on by ... something.   It seems like a lot of these menu options currently
        #  do nothing EXCEPT write to these files!

        #     # set our teensy info file in program junk
        #     filewrite = open(setdir + "/teensy", "w")
        #     filewrite.write(teensy_menu_choice + "\n")
        #     if teensy_menu_choice != "3" and
        #        teensy_menu_choice != "7" and
        #        teensy_menu_choice != "8" and
        #        teensy_menu_choice != "9" and
        #        teensy_menu_choice != "10" and
        #        teensy_menu_choice != "11" and
        #        teensy_menu_choice != "12" and
        #        teensy_menu_choice != "13":
        #         yes_or_no = yesno_prompt( "0", "Do you want to create a payload and listener [yes|no]: ")
        #         if yes_or_no == "YES":
        #             filewrite.write("payload")
        #             # load a payload
        #             import create_payloads
        #     # need these default files for web server load
        #     filewrite = open(setdir + "/site.template", "w")
        #     filewrite.write("TEMPLATE=CUSTOM")
        #     filewrite.close()
        #     filewrite = open(setdir + "/attack_vector", "w")
        #     filewrite.write("hid")
        #     filewrite.close()

    def do_1(self, line):
        # import teensy
        pass

    def do_2(self, line):
        # import teensy

        pass

    def do_3(self, line):
        # import teensy

        pass

    def do_4(self, line):
        # import teensy

        pass

    def do_5(self, line):
        # import teensy

        pass

    def do_6(self, line):
        # import teensy

        pass

    def do_7(self, line):
        #         import src.teensy.binary2teensy

        pass

    def do_8(self, line):
        #         import src.teensy.sd2teensy

        pass

    def do_9(self, line):
        #         print_status( "Generating the SD2Teensy OSX pde file for you...")
        #         if not os.path.isdir(setdir + "/reports/osx_sd2teensy"):
        #             os.makedirs(setdir + "/reports/osx_sd2teensy")
        #         shutil.copyfile("src/teensy/osx_sd2teensy.pde", "%s/reports/osx_sd2teensy/osx_sd2teensy.pde" % (setdir))
        #         print_status( "File has been exported to ~/.set/reports/osx_sd2teensy/osx_sd2teensy.pde")
        pass

    def do_10(self, line):
        #         print_status( "Generating the Arduino sniffer and libraries pde..")
        #         if not os.path.isdir(setdir + "/reports/arduino_sniffer"):
        #             os.makedirs(setdir + "/reports/arduino_sniffer")
        #         shutil.copyfile("src/teensy/x10/x10_sniffer.pde", setdir + "/reports/arduino_sniffer/x10_sniffer.pde")
        #         shutil.copyfile("src/teensy/x10/libraries.zip", setdir + "/reports/arduino_sniffer/libraries.zip")
        #         print_status("Arduino sniffer files and libraries exported to ~/.set/reports/arduino_sniffer")

        pass

    def do_11(self, line):
        #         print_status( "Generating the Arduino jammer pde and libraries...")
        #         if not os.path.isdir(setdir + "/reports/arduino_jammer"):
        #             os.makedirs(setdir + "/reports/arduino_jammer")
        #         shutil.copyfile("src/teensy/x10/x10_blackout.pde", setdir + "/reports/arduino_jammer/x10_blackout.pde")
        #         shutil.copyfile("src/teensy/x10/libraries.zip", setdir + "/reports/arduino_hammer/libraries.zip")
        #         print_status( "Arduino jammer files and libraries exported to ~/.set/reports/arduino_jammer")
        pass

    def do_12(self, line):
        #         print_status( "Generating the Powershell - Shellcode injection pde..")
        #         import src.teensy.powershell_shellcode
        pass

    def do_13(self, line):
        pass


class Infect(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(Infect, self).__init__(prompt, *args, **kwargs)
        self.intro = ("The {bold}{green}Infectious{end} USB/CD/DVD "
                      "module will create an autorun.inf file and a "
                      "Metasploit payload. When the DVD/USB/CD is "
                      "inserted, it will automatically run if autorun "
                      "is enabled. Pick the attack vector you wish to "
                      "use: fileformat bugs or a straight executable.\n\n"
                      "1) File-Format Exploits\n"
                      "2) Standard Metasploit Executable\n"
                      "99) Return to previous menu\n".format(bold=bcolors.BOLD,
                                                             green=bcolors.GREEN,
                                                             end=bcolors.ENDC))

    # This code is executed on this options selection.
    # filewrite1 = open(setdir + "/payloadgen", "w")
    # filewrite1.write("payloadgen=solo")
    # filewrite1.close()

    def do_1(self, line):
        #     ipaddr = input("IP address for the reverse connection (payload)")
        #     update_options("IPADDR=" + ipaddr)

        #     filewrite = open(setdir + "/fileformat.file", "w")
        #     filewrite.write("fileformat=on")
        #     filewrite.close()
        #     import create_payload

        #     import src.autorun.autolaunch

        pass

    def do_2(self, line):
        #     # trigger set options for infectious media
        #     update_options("INFECTION_MEDIA=ON")
        #     import src.core.payloadgen.solo
        #     import src.autorun.autolaunch
        pass


class WebAttack(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(WebAttack, self).__init__(prompt, *args, **kwargs)


class WebAttackVector(SubCmd):
    def __init__(self, prompt, *args, **kwargs):
        super(WebAttackVector, self).__init__(prompt, *args, **kwargs)
