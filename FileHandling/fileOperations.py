from FileHandling.Baseclass import Base, create_directory, create_file

class FileOperations(Base):
    def __int__(self):
        super().__init__()


# Creating path with test data directory
file_path = create_directory()

# delete files
for files in file_path.iterdir():
    files.unlink()

# create a txt file
file = create_file('.txt')

# write single line to txt file
with open(file, 'w') as c:
    c.write("ChowNow Project")

# write multiple lines to txt file
words = ['Created directory\n', 'created file name with todays date and time\n',
         'using write and writelines commands to insert text into file\n']

with open(file, 'w') as c:
    c.writelines(words)

# Read the file content from txt file
with open(file, 'r') as f:
    print(f.readlines())

