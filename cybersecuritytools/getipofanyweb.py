from IPy import IP
import socket

target_web = input("[+] Enter website name here: ")

def checkip(webname):
    try:
        IP(webname)
        # return webname, socket.gethostbyaddr(webname), socket.gethostname(webname)
        return webname

    except:
        return socket.gethostbyname(webname), socket.gethostbyname_ex(webname)

print(checkip(target_web))
# try:
#     print(checkip(target_web))

# except:
#     print("May the ipaddress not exist")