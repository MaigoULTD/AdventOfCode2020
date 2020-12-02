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
            num = x[0].split("-") #Get number requirement field, sans the "-"
            numlist = list(map(int,num)) #Requirement field outputted as strings, output as ints for comparison.
            letter = x[1].split(":") # Get letter, sans ":"
            key = (letter[0]) # Set key to the letter.
            for l in password: # For each char in password
                if l == key: # If the char is equal to the letter
                    inc = inc + 1 # Increase the increment.
            if inc >= numlist[0]: # If the increment is greater than or equal to the first letter in requirement list (lower number requirement)
                if inc <= numlist[1]: # Then check if its less than or equal to the last letter in requirement list (higher number requirement)
                    total = total + 1 # If both are true, then add one to overall total
                else:
                    continue # Otherwise skip and continue.
                     
print (total) # Print total, which should be 416!






