# CSI 31 Okechukwu Egeruoh average.py
# This program computes the average of three numbers.

def main():
    print("This program computes the average of three numbers.")
    print()
    sum = 0
    for i in range(3):
        x = eval(input("Enter a number:"))
        sum = sum + x
    avg = sum/3
    print()
    print("The average is:", avg)

main()
"""
This program computes the average of three numbers.

Enter a number:3
Enter a number:3
Enter a number:3

The average is: 3.0
    
