# 📂 File Handling & Exception Assignment

# --- File Read & Write Challenge 🖋️ ---
# Reads "input.txt", reverses each line, and writes results into "output.txt"

try:
    with open("input.txt", "r") as infile:
        lines = infile.readlines()   # read all lines

    # Reverse the text in each line for uniqueness
    modified_lines = [line.strip()[::-1] + "\n" for line in lines]

    with open("output.txt", "w") as outfile:
        outfile.writelines(modified_lines)

    print("✅ File processed successfully. Modified version written to output.txt")

except FileNotFoundError:
    print("⚠️ Error: input.txt not found. Please create the file with some content first.")


# --- Error Handling Lab 🧪 ---
# Ask the user for a filename and handle errors gracefully

try:
    filename = input("\nEnter the filename you want to read: ")
    with open(filename, "r") as f:
        print("\n📂 File contents:\n")
        print(f.read())
except FileNotFoundError:
    print("⚠️ Error: The file you entered does not exist.")
except PermissionError:
    print("⚠️ Error: You don’t have permission to open this file.")
except Exception as e:
    print(f"⚠️ Unexpected error occurred: {e}")
finally:
    print("\n🎉 Program finished.")
