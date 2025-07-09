#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
letter_names=[]        
    
with open ("C:/Users/USER/Documents/Python/day24/mai/Input/Names/invited_names.txt") as file:
        for line in file:
            new_name=line.strip()
            if new_name:
                letter_names.append(new_name)
            

            
with open ("C:/Users/USER/Documents/Python/day24/mai/Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    
for naam in letter_names:
    new_letter= letter.replace("[name]" , naam )
    
    with open(f"C:/Users/USER/Documents/Python/day24/mai/Output/ReadyToSend/{naam}.txt", mode="w") as file:
        file.write(new_letter)
        
    
    
with open("C:/Users/Public/BlueStacks/filw.txt") as file:
    contents=file.read()
    print(contents)
