import socket

def scanner(host,set):
    counter=0
    for port in set:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            try:
                s.connect((host, port))
                print(f'port {port} is open')
                counter+=1
            except socket.timeout:
                print("Connection timed out after 5 seconds!")    
            except ConnectionRefusedError:
                print(f"Port {port} is closed")
            except:
                print('Unable to connect due to some reason (eg, custom port is not correct, host is not up)')
    return counter
