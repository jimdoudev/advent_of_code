from readlines import *

class Dir:
    def __init__(self, name) -> None:
        self.name = name
        self.subdirectories= []
        self.files = []

    def __str__(self) -> str:
        return f"{self.name}({self.subdirectories})({self.files})"

    def dir_size(self) -> int:
        total_size = 0
        if(len(self.subdirectories) > 0):
            for subdir in self.subdirectories:
                total_size += subdir.dir_size()
        if(len(self.files) > 0):
            for file in self.files:
                total_size += int(file.size)
        return total_size
            
class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        return f"{self.name}({self.size})"

lines = [x.split(" ") for x in input_to_lines("day7.txt")]

root = Dir("/")
current_dir = []
directories = [root]

for line in lines:
    if line[0] == "$":
        match line[1]:
            case "cd":
                if line[2] == "..":
                    current_dir.pop()
                else: 
                    if line[2] == "/":
                        current_dir.clear()
                        current_dir.append(root)
                    else:
                        for directory in current_dir[-1].subdirectories:
                            if directory.name == line[2]:
                                current_dir.append(directory)
                                break
            case "ls":
                continue
    elif line[0] == "dir":
        new_dir = Dir(line[1])
        directories.append(new_dir)
        current_dir[-1].subdirectories.append(new_dir)
    else:
        current_dir[-1].files.append(File(line[1], int(line[0])))

solution = 0

for directory in directories:
    if(directory.dir_size()) <= 100000:
        solution += directory.dir_size()


print(solution)