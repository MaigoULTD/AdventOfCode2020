import csv 
sublist = []
total = 0

#PT1
with open ('input.txt') as csv_file:
    csv = csv.reader(csv_file, delimiter='\n')
    for row in csv:
        for x in row: # For each item in the row
            inc = 0
            x = x.split(" ") #Split by space, separate fields
            password = x[2] # Get password field
            password = list(password) #Turn password into list for easy comparison
            num = x[0].split("-") #Get number requirement field, sans the "-"
            numlist = list(map(int,num)) #Requirement field outputted as strings, output as ints for comparison.
            lower= (numlist[0] - 1)
            upper = (numlist[1] - 1)
            letter = x[1].split(":") # Get letter, sans ":"
            key = (letter[0]) # Set key to the letter.
            if password[lower] == key and password[upper]==key: ## If both are found then exit
                exit
            elif password [lower] == key and password[upper]!=key: #If lower is found but upper is not, total + 1
                total+=1
            elif password [lower] != key and password[upper]==key: #If lower is not found but upper is, total +1
                total+=1
            if password [lower] != key and password[upper]!=key: ## If neither found, exit.
                exit
print(total)






