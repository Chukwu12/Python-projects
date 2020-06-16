#Okechukwu Egeruoh
#
def intro():
   # inform user of the purpose of the program
    print ("This program will take plain-text plus a key and encode the")
    print ("text using a Caesar cipher.")
    print()


def function():
    code = int(input("type 2 to encode or 4 to decode a message"))
    message = str(input("Find the key"))
    key = int(input("Please enter the message"))
    newmessage = []
    change = []
    if code == 2:
        for ch in massage:
              newmessage.append(ord(ch) + key)
                   
                       

    ciphertext = string.join(msgList,"")    
    print ("The resulting cipher-text would be '%s'.")


def result():
    print()

def main():
   intro()
   function()
   result()
main()

