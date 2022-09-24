fileName = input("Input name of the new file: ")
with open(fileName, "a") as f:
    userDecision = input("Do you want to write in the file? (y/n): ")
    if userDecision == "y":
        print("Currently Writing in the file... type EOF to close the file")
        while prompt != "EOF":
            prompt = input("Input text: ")
            f.writelines(prompt + "\n")
        if prompt == False:
            print("Closing the file")
    print("Currently closing the File: " + fileName)
