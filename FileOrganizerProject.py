import os
import shutil

folder = input("Which folder do you want to organize? ")

base_path = fr"C:\Users\nakul\OneDrive\Desktop\Python\{folder}"#using raw string r" bcz \U can impact as a escape sequence. r=raw string,f  = f-strings
print(base_path)

python_files = os.path.join(base_path, "PythonFiles")
docs = os.path.join(base_path, "Docs")

os.makedirs(python_files, exist_ok=True)
os.makedirs(docs, exist_ok=True)

for file in os.listdir(base_path):
    full_path = os.path.join(base_path, file)

    if os.path.isfile(full_path):
        if file.endswith(".py"):
            shutil.move(full_path, python_files)
            # shutil.move(file, python_files) #python looks for file in current working directory, NOT in your target folder.
        elif file.endswith(".txt"):
            shutil.move(full_path, docs)#moving