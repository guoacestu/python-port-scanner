import sys
from scanner import scanner
from validation import number_valid
import re

ipv4_format=r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
#ip address of http://scanme.nmap.org/ == 45.33.32.156

top_10 = (80, 23, 443, 21, 22,25, 3389, 110, 445, 139)

top_100=(
    80, 23, 443, 21, 22, 25, 3389, 110, 445, 139,143, 53, 135, 3306, 8080, 1723, 111, 995, 993, 5900,1025, 587, 8888, 199, 1720, 465, 548, 113, 81, 6001,10000, 514, 5060, 179, 1026, 2000, 8443, 8000, 32768, 554,26, 1433, 49152, 2001, 515, 8008, 49154, 1027, 5666, 646,5000, 5631, 631, 49153, 8081, 2049, 88, 79, 5800, 106,2121, 1110, 49155, 6000, 513, 990, 5357, 427, 49156, 543,544, 5101, 144, 7, 389, 8009, 3128, 444, 9999, 5009,7070, 5190, 3000, 5432, 1900, 3986, 13, 1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100, 119, 37
)
while True:
    host=input('Enter the ip address or domain name of the website you want to scan (press q to quit): ')
    if host == 'q':
        print("Exiting program...")
        sys.exit()
    if not re.fullmatch(ipv4_format,host):
        print('This is not an valid ip address, please try again. ')
    else:
        while True:
            print('1) Top 10 most common port')
            print('2) Top 100 most common port')
            print('3) Custom ports')
            scan_port=input('Enter what port you want to scan, choose 1,2,3 (press q to go to quit,back to previous part): ')
            if scan_port=='q':
                print("Exiting program...")
                sys.exit()
            elif scan_port=='back':
                break
            if number_valid(scan_port) == True:
                scan_port=int(scan_port)
                if 0 < scan_port <=3:
                    if scan_port == 1:
                        amount=scanner(host,top_10)
                    elif scan_port == 2:
                        amount=scanner(host,top_100)
                    if scan_port == 3:
                        custom_port_list=[]
                        custom=input('Enter custom ports (separate with comna,press q to quit): ').split(',')
                        if custom == ['q']:
                            print("Exiting program...")
                            sys.exit()
                        if custom == ['back']:
                            break
                        if custom != [''] and custom != [' '] :
                            print('test')
                            for i in custom:
                                if number_valid(i) == True:
                                    number=i
                                    number=int(number)
                                    if not 1<= number <= 65535:
                                        print(f"Invalid port: {number}")
                                    else:
                                        custom_port_list.append(number)
                            custom_port=set(custom_port_list)
                            amount=scanner(host,custom_port)
                        else:
                            print('There is no content inside.')
                            amount=0
                    print(f'There is {amount} ports open')
                    retry=input('Would you like to run another scan (y/n): ').lower()
                    if retry == 'y':
                        break
                    elif retry== 'n':
                        print("Exiting program...")
                        sys.exit()
                else:
                    print("Please choose 1, 2 or 3.")
                    continue
            else:
                print("Invalid input. Please enter 1, 2 or 3.") 
