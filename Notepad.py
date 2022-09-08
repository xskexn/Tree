prompt = "None"
fileName = input("Input name of the new file: ")
f = open(fileName, "a")
userDecision = input("Do you want to write in the file? (y/n): ")
if userDecision == "y":
    print("Currently Writing in the file... leave blank to close the file")
    while prompt:
        f = open(fileName, "a")
        prompt =  input("Input text: ")
        f.writelines(prompt + "\n")
    if prompt == False:
        print("Closing the file")
        f.close()
print(f"Currently closing the File: {fileName}")