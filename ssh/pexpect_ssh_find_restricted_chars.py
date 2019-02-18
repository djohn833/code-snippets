import getpass
import pexpect
import time
from tqdm import tqdm
import string


password = getpass.getpass('password:')


s = pexpect.spawn('ssh level3@challenges.ringzer0team.com -p 10220')
s.expect('password:')
time.sleep(0.1)
s.sendline(password)


restricted_chars = ''
for c in tqdm(string.printable):
    input = c
    if c == '\\':
        input = '\\' + c

    s.expect('Your input:\r\n')
    s.sendline(input)

    response = s.expect(['Command executed', 'Restricted characters has been used'])
    if response == 1:
        restricted_chars += c


print('restricted_chars: "%s"' % restricted_chars)
