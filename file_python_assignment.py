try:
    # File Creation
    with open('my_file.txt', 'w') as file:
        file.write("Line 1: Hello, world!\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome!\n")
    print("File creation process completed.")
    
    # File Reading and Display
    with open('my_file.txt', 'r') as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
    print("File reading process completed.")
    
    # File Appending
    with open('my_file.txt', 'a') as file:
        file.write("Line 4: Adding more content\n")
        file.write("Line 5: 98765\n")
        file.write("Line 6: File handling in Python\n")
    print("File appending process completed.")

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File handling process completed.")
