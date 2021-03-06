import os
import socket
import re
import json

class ScanNet(object):
    def __init__(self):
        self.start_ip = '192.168.56.' # '192.168.6.'
        self.begin_ip = 100 # 70
        self.end_ip = 103  # 90
        self.begin_port = 1 # 4100
        self.end_port = 100 # 4200
        self.computers = []
        self.struct_net = {}

    #  find available computers
    def ping_computers(self):
        computers = []
        for i in xrange(self.begin_ip, self.end_ip):
            host = self.start_ip + str(i)
            response = os.system('ping -c 1 ' + host)
            if response == 0:
                computers.append(host)
        return computers

    # find open ports
    def get_open_ports(self, ip):
        open_ports = []
        for port in xrange(self.begin_port, self.end_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01)
            try:
                sock.connect((ip, port))
            except:
                pass
            else:
                open_ports.append(str(port))
            sock.close()
        return open_ports

    def get_struct_net(self):
        self.struct_net = {}
        for ip in self.ping_computers():
            self.struct_net[ip] = self.get_open_ports(ip)
        return self.struct_net


if __name__ == '__main__':
    s_net = ScanNet().get_struct_net()
    print(s_net)
    json.dump(s_net, open('struct_net', 'w'))


# def get_alt_open_ports(ip):
#     ports = []
#     try:
#         res = os.system('which nmap')
#         if not res == 0:
#             ports = get_open_ports(ip)
#         else:
#             os.system('sudo nmap {} -p {} | grep tcp > 1.txt'.format(ip, '1-100'))
#             with open('1.txt', 'r') as f:
#                 text = f.read()
#                 patt = re.compile('([0-9]{1,5})')
#                 ports = patt.findall(text)
#     except:
#         print('error nmap')
#         ports = get_open_ports(ip)
#         #return ports
#     finally:
#         return ports
#




