#Okechukwu Egeruoh Final Exam
# Intro to the program to be displayed for the user
def intro():
    print("Enter username and password. You will have 3 chances to enter correct username and password.")


# Get input of username and password from user
def getInfo():
    # Set global username to be accessed outside of this function
    global username
    username = input('What is your username: ')
    # Set global passwd to be accessed outside of this function
    global passwd
    passwd = input('What is your password: ')
   

# Check the file to see if the username and password entered by the user matches the file
def checkFile():
    # Open file and read it
    infile = open("unames_passwords.txt", "r")
    infile.seek(0)
    # Read opened file line by line
    for line in infile :
        line = line.strip("\n")
        # Create set of username and password read from file
        set1 = set(line.split(' '))
        
        # Create set of username and password read from user
        set2 = username + " " + passwd
        set2 = set(set2.split(' '))

        # Compare sets, if matches return true
        if(set1 == set2):
            return True

    return False


def main():
    intro()
    count = 0
    check = False
    # Loop for three times if entered username and password are incorrect
    while(check == False):
        if count >= 0:
            getInfo()
        check = checkFile()
        # Check the file and break if true else increase the count
        if  check == True:
            print("Username and password entered are correct")
            break
        elif count == 3:
            print("Goodbye")
            break
        else:
            count = count + 1
            print((3 - count),"Attempts left")

    


if __name__ == '__main__':
    main()


"""Enter username and password. You will have 3 chances to enter correct username and password.
What is your username: house
What is your password: yard
2 Attempts left
What is your username: basketball
What is your password: football
1 Attempts left
What is your username: jprince
What is your password: mutt
Username and password entered are correct
>>> 
"""
