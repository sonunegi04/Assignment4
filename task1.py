try:
        with open('simple.txt', 'r') as file:
            print("Reading file content:")
            line_number=1;
            for line in file:
                print(f"Line {line_number}: {line.strip()}")
                line_number+=1

except FileNotFoundError:
    print(f"Error: The file simple.txt was not found.")

