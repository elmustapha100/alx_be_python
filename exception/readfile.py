def read_file(filepath) : 
    try : 
        with open(filepath, "r") as file : 
            file_content = file.read()
            print(f"File ' {filepath}' read successfully!")
            return file_content 

    except FileNotFoundError : 
        print(f"Custom Error : Could not find '{filepath}' does not exist.Please check the file name .")
        return None 

print("Test 1: Reading an existing file")
file_content = read_file("library_management.py")
# if file_content :
#     print(f"File content lenght : {len(file_content)} characters") 
#     print("First 100 characters :", file_content[:100])

# print("\nText 2 : Reading a non-existing file")
# file_content = read_file("library_management.py")       