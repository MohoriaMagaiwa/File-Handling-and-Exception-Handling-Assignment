# 📂 File Handling & Exception Assignment in Python  

This project demonstrates **how to work with files and handle errors in Python**.  
It includes two tasks:  

1. **File Read & Write Challenge 🖋️** – Read a file and write a modified version into a new file.  
2. **Error Handling Lab 🧪** – Ask the user for a filename and handle errors gracefully.  

---

## 🚀 File Read & Write Challenge 🖋️

```python
# Read from an existing file and write a modified copy to another file

with open("input.txt", "r") as f:
    content = f.read()

# Modify the text (make it uppercase for this example)
modified_content = content.upper()

with open("output.txt", "w") as f:
    f.write(modified_content)

print("File has been read and modified version written to output.txt ✅")

