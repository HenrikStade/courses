formatted_name_list = []

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for name in name_list:
        formatted_name_list.append(name.replace("\n", ""))

print(formatted_name_list)

for name in formatted_name_list:
    with open("Input/Letters/starting_letter.txt") as letter:
        lines = letter.readlines()
        new_line = lines[0].replace('[name]', name)
        lines[0] = f"{new_line}"
        file_to_save = f"Output/ReadyToSend/letter_to_{name}.txt"
        text = ' '.join(lines)
        f = open(file_to_save, "w")
        f.write(text)
        f.close()





#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp