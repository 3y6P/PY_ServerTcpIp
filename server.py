import socket, time

from filer import FilerClass
from regexer import RegexClass


class ServerClass(RegexClass, FilerClass):
	clients = []
	quit = False

	host = "localhost"
	port = 12345

	def MessageSendAllClients(self, addr, data, s):
		for client in self.clients:
			if addr != client:
				s.sendto(data)


	def ServerStart(self):

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((self.host, self.port))

		print("[ Server was started ]")


		while not self.quit:
			try:
				data, addr = s.recvfrom(1024)

				if addr not in self.clients:
					self.clients.append(addr)

				clientDataTimeJoin = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

				print("["+addr[0]+"]=["+str(addr[1])+"]=["+clientDataTimeJoin+"]/",end="")

				clientStroke = RegexClass.StrokeMagic(self, data.decode("utf-8"))
				print(clientStroke)
				if clientStroke != "":
					FilerClass.FileWrtie(self, "serverResultFile.txt", str(clientStroke) + "\n")


			except:
				print("\n[ Server was stopped ]")
				self.quit = True

		s.close()

if __name__ == "__main__":
	f = ServerClass()
	f.ServerStart()