import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address=('localhost', 8080)
print('[*] Starting up on '+address[0]+', port: '+str(address[1]))
sock.bind(address)
sock.listen(1)

data=open('tSrc/main.py').read()

while True:
    print('[*] Waiting for connection...')
    conn, addr=sock.accept()
    try:
        print('[*] Incoming connection from',addr)
        while True:
            # invia il testo
            conn.sendall(data.encode())
            print('[*] All data were successfully sended.')
            break
    finally:
        conn.close()
