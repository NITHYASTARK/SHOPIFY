import time
import colorama
import requests
colorama.init()


CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'
RESET = '\033[0m'
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[m"
REVERSE = "\033[m"


banner = """ 
\033[1;35;40m

░██████╗████████╗░█████╗░██████╗░██╗░░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░░░░██║░░░███████║██████╔╝█████═╝░
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗██╔═██╗░
██████╔╝░░░██║░░░██║░░██║██║░░██║██║░╚██╗
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
\n\t CODED BY - 𝙎𝙏𝘼𝙍𝙆
\033[0;37;40m
"""
print(CLEAR_SCREEN)
print(banner)
#################################################################################################################


def chk(pips, proxy):
    pips = pips.split('\n')[0]
    url = "http://127.0.0.1:5000/api?lista="+pips+"&sec="+proxy
    try:
        call = requests.get(url)
        response = call.text
        if response.__contains__("CHARGED"):
            print(
                GREEN+f''' [CHARGED]  =>   {pips}   Message =>  Charged card  - 𝙎𝙏𝘼𝙍𝙆''')
            with open("CHARGED.txt", 'a') as sav:
                sav.write(
                    f''' [CHARGED]  =>   {pips}   Message =>  Charged card  - 𝙎𝙏𝘼𝙍𝙆''')
                sav.write('\n')
        elif response.__contains__("CCN"):
            print(
                GREEN+f''' [LIVE CCN]  =>   {pips}   Message =>  Card security code is incorrect''')
            with open("CCN.txt", 'a') as sav:
                sav.write(
                    f''' [LIVE CCN]  =>   {pips}   Message =>  Card security code is incorrect - 𝙎𝙏𝘼𝙍𝙆''')
                sav.write('\n')
        elif response.__contains__("Street address and postal code do not match"):
            print(
                CYAN+f''' [MISMATCH]  =>   {pips}   Message =>  Street address and postal code do not match - 𝙎𝙏𝘼𝙍𝙆''')
            with open("MISMATCH.txt", 'a') as sav:
                sav.write(
                    f''' [MISMATCH]  =>   {pips}   Message =>  Street address and postal code do not match - 𝙎𝙏𝘼𝙍𝙆''')
                sav.write('\n')
        else:
            string1 = response
            start_index = string1.find("Response:") + len("Response:")
            end_index = string1.find("- 𝙎𝙏𝘼𝙍𝙆")
            substring = string1[start_index:end_index]
            print(
                RED + f''' [DEAD] ❌ =>   {pips}   Message => {substring} - 𝙎𝙏𝘼𝙍𝙆''')
    except:
        print(RED+f'  Something Went Wrong..  ')


#################################################################################################################

if __name__ == "__main__":
    print(CYAN)
    ccfile = input(" Enter the file name of ccs : ")
    opi = input(" Enter your proxy [ip:port:username:password] : ")
    print('\n\n')
    with open(ccfile, encoding='utf-8') as w:
        for x in w:
            chk(x, opi)
            time.sleep(12)
