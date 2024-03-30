#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("./input/Names/invited_names.txt","r") as File:
    Names = File.readlines()
    Names = list(map(lambda Name: Name.replace("\n",""),Names))
   
with open("./input/Letters/starting_letter.txt",mode="r") as File:
    Layout = File.read()
    
for Name in Names:
    with open(f"Invites/{Name}_Invite.txt",mode="w") as File:
        NewLayout = Layout.replace("[name]",Name)
        File.write(NewLayout)