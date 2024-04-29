empty_list = [] #To store the contents of the file
try:
    with open("even.txt", "r") as file:
        for line in file:
            empty_list.append(line)
except FileNotFoundError: #If the file called is not existing
    print("Please select an existing file.")
except IOError: #If there is a problem involving the operating system
    print("Your disk might have been full.")
else:
    print(empty_list) #Printing the result if there is no errors