__author__ = 'cita'
from socket import socket, AF_INET, SOCK_DGRAM
import sys
import time
from models import MessageProcessor
PORT = 4582

def socket_server(address):

    try:
        #Creates socket with UDP Protocol
        sock = socket(AF_INET, SOCK_DGRAM)
        print 'Socket created'
        response = None

    #In case of an error with the socket creation, print the error code
    except socket.error, msg:
        print 'Failed to create socket. Error Code : ' + str (msg[0]) + ' Message ' + msg[1]
        sys.exit()

    #Binds the socket with the defined IP Address
    sock.bind (address)
    print('Connected to port ' + str (PORT))
    while True:
        print('Waiting for data')
        #Receiving message with a size of 1024 bytes, from the address
        msg, addr = sock.recvfrom (1024)

        #In case there's no message from GPRS
        if not msg:
            print('No data received')
            break

        print('Got message from', addr)
        print msg[:2]
        
        if msg[:2] == '01':
            response = '0'
        else:
            response = '010'
            processor = MessageProcessor.MessageProcessor()
            processor.process_message(msg)

        sock.sendto(response, addr)

if __name__ == '__main__':
    socket_server(('', PORT))
