import ecrypto
import sys
import os

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")    

#Created By: EH
print("\033[1;32m1)Encrypt\n2)Decrypt\033[1;0m\n")

choice = str(input("\033[1;32mEnter You're Choice: \033[1;0m"))
if choice == "1":
    key = str(input("Key: "))
    Message = str(input("Message: "))
    access = ecrypto.ecrypt()
    encrypted = access.encrypt(Message, key)
    print("[+]Encrypted: ", encrypted)
elif choice == "2":
    key = str(input("Key: "))
    Message = str(input("Encrypted Message: "))
    access = ecrypto.ecrypt()
    decrypted = access.decrypt(Message, key)
    print("[+]Decrypted: ", decrypted)
else:
    print("[-]Invalid Input")


