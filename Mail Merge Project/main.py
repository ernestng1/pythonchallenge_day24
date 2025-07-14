invited_names_list = open("Input/Names/invited_names.txt", "r")
for i in invited_names_list:
    with open(f"Output/ReadyToSend/starting_letter_{i.split()[0]}.txt","w") as file:
        with open("Input/Letters/starting_letter.txt", "r") as file2:
            file_to_read = file2.read()
        file_to_read = file_to_read.replace("[name]", i.split()[0])
        file.write(file_to_read)
