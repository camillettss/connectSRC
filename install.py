import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('localhost', 8080)
print('[*] Connecting to the server on '+server_address[0])
sock.connect(server_address)

def wrt(path, x):
    f=open(path, 'w+')
    f.write(x)
    f.close()

try:
    print('[..] Receiving datas...')
    cmptsrc=sock.recv(8000)
    # decompressing cmptsrc
    main, data, contacts, msg, admin = cmptsrc.split('\nskk\n')
    print('[*] All data were received.\n\rmaking files..')
    # file structure:
    '''
    ../
    tSrc/
        main.py - data
        .data/
            data.json
            ADMIN.txt
            contacts.txt
            message.txt
    '''
    wrt('C:/connect/help.py', main)
    wrt('C:/connect/.data/data.json', data)
    wrt('C:/connect/.data/ADMIN.txt', admin)
    wrt('C:/connect/.data/contacts.txt', contacts)
    wrt('C:/connect/.data/message.txt', msg) 
    print('[*] setted up, ready to use!')
finally:
    print('[*] u did it! closing socket.')
input()