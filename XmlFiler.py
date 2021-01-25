import xml.etree.ElementTree as ET
from tokenize import Name


class XmlFilerClass(object):
    serverIpPath = "Server/serverIP"
    serverPortPath = "Server/serverPort"
    clienIpPath = "Client/ClientIp"
    clienIpPortPath = "Client/ClientPort"
    clientConnectToServerIpPath = "Client/Connection/serverConnectIP"
    clientConnectToServerPortPath = "Client/Connection/serverConnectPort"

    def RootFileGet(self):
        root_node = ET.parse('config.xml').getroot()
        return root_node

    def ServerProperties(self, root_node):

        for tag in root_node.findall(self.clienIpPath):
            print(tag.text)
        for tag in root_node.findall(self.clienIpPortPath):
            print(tag.text)
        for tag in root_node.findall(self.clientConnectToServerIpPath):
            print(tag.text)
        for tag in root_node.findall(self.clientConnectToServerPortPath):
            print(tag.text)

    def ClientProperties(self):
        pass

    def ClentConnectionProperties(self):
        pass


if __name__ == "__main__":
    XMCLS = XmlFilerClass
    XMCLS.ServerProperties(XMCLS, XMCLS.RootFileGet(XMCLS))

