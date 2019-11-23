import barcode,socket,random,time,os

ip = '127.0.0.2'
port = 1817
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip, port))
# #socket.gethostname()
s.listen(5)
conn,addr = s.accept()

 while True:
	def barcode_generator():
		num = random.randrange(1,1000000000000)
		image = barcode.get_barcode_class('ean13')
		image_bar = image(u'{}'.format(num))
		file = open('barcode.svg',"w")
		image_bar.write(file)
		os.system("lpr -P L5190 /home/dafa/Desktop/programming/barcode.svg")
		# conn.send(str(num))

barcode_generator()
#time.sleep(5)