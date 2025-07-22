writing_file=input('enter text to write in a file')
with open('output.txt','w') as file:
    file.write(writing_file + "\n")
    print("data successfully written to output.txt file")

appending_file = input('enter additional text to append:')
with open('output.txt', 'a') as file:
    file.write(appending_file + "\n")
    print("data successfully appended")

print("\n final content of output.txt:")
with open("output.txt","r") as file:
    content=file.read()
    print(content)
