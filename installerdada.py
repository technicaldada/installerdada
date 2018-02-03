import sys, os, time

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
b = "apt install"
c = " "

os.system("clear")

print("   +--------------------------+")
print("   | Termux Installer  |")
print("   |       Version 1.0        |")
print("   +--------------------------+")
print("            Today is: ")
os.system("date")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("|   Powered By:- Technical Dada.   |")
print("|  Website:- http://technicaldada.in |")
print("|FB:- facebook.com/technicaldada.in |")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("|________________________________|")
print("|___________Type Any ____________|")

for s in range(3):
    print("")
print(" [01] Nmap")
print(" [02] Hydra")
print(" [03] Figlet")
print(" [04] Toilet")
print(" [05] Perl")
print(" [06] Htop")
print(" [07] Mc")
print(" [08] Wget")
print(" [09] Tor")
print(" [10] Php")
print(" [11] See All Termux Packages/Tools")
print(" [12] Exit Now")
print
a = raw_input("[+]0ne Click :")
if a == '01' or a == '1':
    print("nmap installing start now")
    os.system("apt install nmap")
    sys.exit()

elif a == '02' or a == '2':
    print("Hydra installing start now")
    os.system("apt install hydra")
    sys.exit()

elif a == '03' or a == '3':
    print("Figlet installing start now")
    print
    os.system("apt install figlet")
    os.system("figlet Technical Dada")
    print('figlist <--> Font for figlet')
    print('Please Type --> figlet yourname')
    print
    sys.exit()

elif a == '04' or a == '4':
    print("Toilet installing start now")
    print
    os.system("apt install toilet")
    os.system("toilet Technical Dada")
    print("toilet -h <--> toilet help")
    print("Please Type --> toilet yourname")
    print
    sys.exit()

elif a == '05' or a == '5':
    print("Perl installing start now")
    print
    os.system("apt install perl")
    print
    sys.exit()

elif a == '06' or a == '6':
    print("Htop installing now")
    print
    os.system("apt install htop")
    print
    sys.exit()

elif a == '07' or a == '7':
    print("Mc installing now")
    print
    os.system("apt install mc")
    print
    sys.exit()

elif a == '08' or a == '8':
    print("wget installing start now")
    print
    os.system("apt install wget")
    print
    sys.exit()

elif a == '09' or a == '9':
    print("Tor installing start now")
    print
    os.system("apt install tor")
    print
    sys.exit()

elif a == '10' or a == '10':
    print("Php installing start now")
    print
    os.system("apt install php")
    print
    sys.exit()

elif a == '12' or a == '12':
    print("Thanks For Using")
    print("Bye Bye Dear")
    sys.exit()



z="y"
while z !="n":
    if a == '11' or a == '11':
        print("See All Termux Package")
        time.sleep(3)
        print
        os.system("apt list")
        print
        print("Type Now Package Name")
        print
        pkg = raw_input("Pkg_Name : ")
        os.system(b+c+pkg)
        print
        print
        print
        z=raw_input(" [+] Try Again [Y/n] ")
    
