with open("my_file.txt") as file:
    contents = file.read()
    print(contents) 
    
with open("new_file1.txt", mode="w") as file:
    file.write(" \n Congrats for being sucessful" )