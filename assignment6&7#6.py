#Okechukwu Egeruoh
# Square the numbers in a list by modifying the list parameter.


# This function modifies the list argument passed in
def squareEach(nums):

    # nums coming in looks like [4,6,8]
    # modify nums to look like [16, 36, 64]
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
        

def main():
    nums = input("Enter a list of numbers with brackets, eg, [4,6,8] :")
    print (nums)   

    squareEach(nums)
	
    print ("Squaring this list gives:"), nums
    print (nums)   
                 
                 
main()
