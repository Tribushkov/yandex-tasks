
# 1
def my_zip(a, b):
    if len(a) > len(b):
        res = map(None, a, b)
    else:
        res = zip(a, b)
    return dict(res)

# 2
import re

login_pattern = re.compile('^[a-zA-Z][a-zA-Z0-9\-\.]{0,19}(?<![\-\.])$')

def validate_login_one(login):
return bool(login_pattern.match(login))


def validate_login_two(login):
    if 1 <= len(login) <= 20 and login[0].isalpha() and (login[-1].isalpha() or login[-1].isdigit()):
    res = True
        for c in login[1:-1]:
            if not c.isalpha() and not c.isdigit() and c != '-' and c != '.':
                res = False
                break
    else:
    res = False
    return res


letters = 'abcdefghijklmnpqrstuvwxyz'
digits = '1234567890'
symbols = '.-'
left_edge = list(letters)
right_edge = list(letters + digits)
allowed = list(letters + digits + symbols)

def validate_login_three(login):
    login = login.lower()
    return \
        0 < len(login) < 21 and \
        login[0] in left_edge and \
        login[-1] in right_edge and \
        set(login) == set(login).intersection(allowed)

#3
SELECT users.Name, count(messages.msg) 
FROM users LEFT JOIN messages ON users.UID = messages.UID 
GROUP BY users.UID;

#4
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' access.log | sort | uniq -c | sort -rn | head -n 10 | sed -E 's/^ *[0-9]+ //g'


import re
from collections import Counter

f = open('access.log')
data = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', f.read())
f.close()
for ip in Counter(data).most_common(10):
    print ip[0]