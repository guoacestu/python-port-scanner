import socket
import re
'''
user=('Enter a domain')
ip=socket.gethostbyname(user)

print(ip)


'''

user=input('Enter a ip address: ')
ipvalidator="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
if re.fullmatch(ipvalidator, user):
    host=user

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(2)
            s.connect((host,80))
            print('connection successful!')

        except:
            print('It failed for some reason')