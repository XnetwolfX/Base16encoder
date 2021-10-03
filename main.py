import base64
import time
import os
import sys
def design():
	print("""
	made by: XnetwolfX(github)
	author : RadiationBolt
	facebook: rad.taren
	follow me on github for more tools
	""")
def encodeit():
	string_path = input("""
{1} string 
{2} file
> """)
	if string_path == "1":
		string = input("give the string > ")
		bytes = string.encode()
		print(f"byteslike object: {bytes}")
		enc = base64.b16encode(bytes)
		print(enc)
		
	elif string_path == "2":
		path = input("give the path > ")
		outpath = input("output file> ")
		if outpath == "":
			iop = input("do you want it to print in screen y/n:" )
			if iop == "n":
				print("you must choose an output file, restart the program")
				sys.exit()
			else:
				sys.exit()
		if path == "":
			iop = input("do you want to encode it to a file y/n:")
			if iop == "n":
				print("you must have a file to encode, restart the program")
				sys.exit()
			else:
				 sys.exit()
	print("reading file")
	f = open(path, "r")
	
	ren = f.read()
	bytes = ren.encode()
	enc = base64.b16encode(bytes)
	print("openning/creating output file")
	out = open(outpath, "wb")
	print(f"{design}\nwriting encoded type of {path} to {out}")
	out.write(enc)
	print("writing complete")
	out.close
			
start = design()		
option_1 = input(f"""
{start}\n
{1} encode (base16)
{2} decode (base16)

> """)
if option_1 == "1":
	os.system("clear")
	print("starting encoding lab ")
	time.sleep(2)
	os.system("clear")
	encodeit()
elif option_1 == "2":
	os.system("clear")
	print("starting decoding lab ")
	time.sleep(2)
	os.system("clear")
	decodeit()
else:
	print("please restart the script and select an option which is listed")
	