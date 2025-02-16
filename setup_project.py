import os

# Create project structure
directories = ['data', 'notebooks', 'src']
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create necessary files
files = ['README.md', 'requirements.txt']
for file in files:
    open(file, 'w').close()
