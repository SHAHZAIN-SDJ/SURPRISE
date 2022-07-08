#!/usr/bin/python3
# coding=utf-8
#CODE BY SHAHZAIN DAVID JOIYA
#IFF U WANT TO RECORD BRO THEN GIVE ME CREDIT
#OPEN____SOURCE
#SOURCE_____ALT
import os,random,time
try:
	import lolcat
except ImportError:
	os.system('pip install lolcat')
	time.sleep(1)
	
try:
	import figlet
except ImportError:
	os.system('pkg install figlet')
	time.sleep(1)
	
logo = """\033[1;92m   ▄████████ ████████▄       ▄█ \n  ███    ███ ███   ▀███     ███ \n  ███    █▀  ███    ███     ███ \n  ███        ███    ███     ███ \n▀███████████ ███    ███     ███ \n         ███ ███    ███     ███ \n   ▄█    ███ ███   ▄███     ███ \n ▄████████▀  ████████▀  █▄ ▄███ \n                        ▀▀▀▀▀▀      """
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'July', 'August', 'Sep', 'Okt', 'Nov', 'DeC']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = months[nTemp]
os.system('git pull')
P = "\033[97;1m" # White
M = "\033[91;1m" # Red
H = "\033[92;1m" # Green
K = "\033[93;1m" # Yellow
B = "\033[94;1m" # Blue
U = "\033[95;1m" # Purple
O = "\033[92;1m" # Light blue
N = "\033[93;1m"
my_color = [
P, M, H, K, B, U, O, N]
color = random.choice(my_color)
os.system('clear')


def main():
		print(logo)
		print(" %s[%s#%s] ═══════════════════════════════════════"%(N,O,N))
		print("\033[1;92m         THIS SCRIPT IS SPECIAL FOR YOU")
		print(" %s[%s#%s] ═══════════════════════════════════════"%(N,O,N))
		print(" %s[%s1%s] CHECK SURPRISE"%(N,O,N))
		print(" %s[%s2%s] AUTHOR INFO"%(N,O,N))
		print(" %s[%s3%s] FOLLOW AUTHOR"%(N,O,N))
		c = input(" CHOSE : ")
		if c in ['1','01']:
				s1()
		elif c in ['2','02']:
				  s2()
		elif c in ['3','03']:
				  s3()
		
def s1():
	print(logo)
	os.system("clear")
	os.system("figlet EID MUBARIK  |lolcat") 
	print("				 %s[%s+%s] REGARDS BY SDJ "%(N,O,N))
	print("				 %s[%s+%s] PRESS ENTER TO BACK "%(N,O,N))
	b = input(" ")
	if b in ['']:
		os.system ("clear")
		main()
		
def s2():
	os.system ("clear")
	print(logo)
	os.system('echo "\n [+] CREATER OF THIS SCRIPT SDJ \n [+] SHAHZAIN DAVID JOIYA \n [+] RESEARCHER NOT PROGRAMMER XD "| lolcat -a -d 8')
	print("				 %s[%s+%s] PRESS ENTER TO BACK "%(N,O,N))
	d = input(" ")
	if d in ['']:
		os.system ("clear")
		main()
		
def s3 ():
	print(logo)
	os.system ("clear")
	os.system("xdg-open https://www.facebook.com/HATERZKAABUUGZAINI2")
	os.system("xdg-open https://youtube.com/channel/UCgg2SsDgxcKQm-a4QLqCvuA")
	main()
	

if __name__ == '__main__':
	main()
