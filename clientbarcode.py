import barcode,socket,random

ip = '127.0.0.2'
port = 1817
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
while True:
	code = s.recv(100)
	print(code)