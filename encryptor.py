import hashlib, os, sys, time, random

W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'

def menu():
	print RR+"Author : Rizal Solehudin"+W
	print RR+"MD5, SHA1, SHA512 encryptor"+W
	
	print "What You Want ? "
	print O+"MD5, SHA1, SHA512"+W
	try:
		input = raw_input("Choice > ")
		if input == "MD5" or input == "md5":
			print "OPENING THE MD5 ENCRYPTOR"
			hash = hashlib.md5(str(raw_input("String > "))).hexdigest()
			print "Hash > ",hash
			menu()
		elif input == 'sha1' or input == 'SHA1':
			print "OPENING THE SHA1 ENCRYPTOR"
			desk = hashlib.sha1(str(raw_input("String > "))).hexdigest()
			print "Hash > ",desk
			menu()
		elif input == "sha512" or input == "SHA512":
			print "OPENING THE SHA512 ENCRYPTOR"
			fiks = hashlib.sha512(str(raw_input("String > "))).hexdigest()
			print "Hash > ",fiks
			menu()
	except KeyboardInterrupt:
		print "[!] Exiting From Program"
		
menu()