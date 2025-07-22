file1="sample.txt"
try:
    with open('sample.txt','r') as file:
        print("reading file content:")
        for i,line in enumerate(file,1):
            print(f"line{i}:{line}")
except FileNotFoundError:
    print("file not found.")
