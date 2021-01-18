import socket, threading, time

class ClientClass(object):

	#server
	serverHost = "localhost"
	serverPort = 12345
	server = (serverHost, serverPort)

	#client
	host = "localhost"
	port = 0

	shutdown = False
	join = False

	def receving (self, name, sock):
		while not self.shutdown:
			try:
				while True:
					data, addr = sock.recvfrom(1024)
					print(data.decode("utf-8"))

					time.sleep(0.2)
			except:
				pass

	def ClientStart(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.bind((self.host,self.port))
		s.setblocking(0)

		clientName = input("Name: ")

		rT = threading.Thread(target = self.receving, args = ("RecvThread",s))
		rT.start()

		while self.shutdown == False:
			if self.join == False:
				s.sendto(("["+ clientName + "] => join chat ").encode("utf-8"),self.server)
				self.join = True
			else:
				try:
					message = "DF20023030DF210130DF2206303844374234DF230154DF24034B4C4BDF260130DF270130"
					print("try message was sended in server: " + message)

					if message != "":
						s.sendto((message).encode("utf-8"),self.server)

					time.sleep(3)

				except:
					s.sendto(("[" + clientName + "] <= left chat ").encode("utf-8"),self.server)
					self.shutdown = True

		rT.join()
		s.close()

if __name__ == "__main__":
	f = ClientClass()
	f.ClientStart()