def main():
    """
    This program will ask the user to enter a number and then double that number and print the result. It will repeat the process until the value is 100 or greater.
    """
    
    curr_value = int(input("Enter a number: ")) #defining a variable that asks for user to input a number
    
    while curr_value < 100: #while the number is less than 100 - keep printing
        curr_value = curr_value * 2 #the number will be doubled and that doulbed number is now the "curr_value"
        print(curr_value)
        
if __name__ == '__main__':
    main()