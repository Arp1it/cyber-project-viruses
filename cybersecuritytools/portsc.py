import socket


# IP_ADDRESS = input("enter ip: ")
# PORT = 139

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     try:
#         s.connect((IP_ADDRESS, PORT))
#         print(f"Successfully connected")

#     except:
#         print(f"failed to connect to port {PORT}")


IP_ADDRESS = input("enter ip: ")
PORT = input("enter port from - to: ")

pPORT = PORT.split("-")
portfrom, portto = int(pPORT[0]), int(pPORT[1])

# print(portfrom, portto)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    b = []
    for port in range(portfrom, portto+1):
        try:
            s.connect((IP_ADDRESS, port))
            a = f"{port} is open"
            b.append(port)
            print(a)

        except:
            print(f"failed to connect to port {port}")

    print(f"These ports are open - {b}")