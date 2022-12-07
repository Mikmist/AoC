def parse_line(line):
    return [y.strip() for y in line.split(' ')]

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File({self.name}, {self.size})"

class Directory:
    def __init__(self, name, files, directories, parent = None): 
        self.name = name
        self.files = files
        self.directories = directories
        self.parent = parent
        self.size = 0
        for i in files:
            self.size+=i.size

    def get_dir(self, name):
        for dir in self.directories:
            if dir.name == name:
                return dir

    def get_parent(self):
        return self.parent

    def add_empty_dir(self, name):
        self.directories.append(Directory(name, [], [], self))
    
    def add_file(self, name, size):
        self.files.append(File(name, int(size)))
        self.size += int(size)

    def get_size(self):
        total = self.size
        for i in self.directories:
            total += i.get_size()
        return total

    def __repr__(self):
        return f"Directory({self.name}, {self.directories}, {self.files}, {self.size})"

def get_dirs(dir, max_size):
    dirs = []
    for i in dir.directories:
        dirs += get_dirs(i, max_size)
    dirs+=filter(lambda x: x.get_size() <= max_size, dir.directories)
    return dirs

with open('../input/test') as data:
    root = Directory("/", [], [])
    lines = data.readlines()
    size = len(lines)
    idx = 0
    current_dir = root
    while idx < size:
        line = lines[idx]
        parts = parse_line(line)
        if parts[0] == '$':
            if parts[1] == "ls":
                while idx+1 < size:
                    pline = parse_line(lines[idx+1])
                    if pline[0] == '$': 
                        break
                    if pline[0] == "dir":
                        current_dir.add_empty_dir(pline[1])
                    else:
                        current_dir.add_file(pline[1], pline[0])
                    idx += 1
            if parts[1] == "cd":
                if parts[2] == "..":
                    current_dir = current_dir.get_parent()
                elif parts[2] == "/":
                    current_dir = root
                else:
                    current_dir = current_dir.get_dir(parts[2])
        idx += 1 
    total = 0

    for i in get_dirs(root, 100_000):
        total += i.get_size()
    print(total)
