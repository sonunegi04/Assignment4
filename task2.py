inputText = input("\nEnter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(inputText + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data
additional_text = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())