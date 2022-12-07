file = open('Day7/input.txt', 'r')
lines = file.readlines()

class ExecutedCommand:
    def __init__(self, command, output, args = '') -> None:
        self.command = command
        self.args = args
        self.outputRows = output

class directory:
    def __init__(self, name, path, files):
        self.name = name
        self.path = path
        self.files = files
    
    def getTotalFileSize(self):
        bytes = 0
        for size in self.files:
            bytes += size
        return bytes

counter = 0
executedCommands = []

while True:
    if(counter + 1 >= len(lines)):
        break

    if lines[counter].startswith('$ '):
        command = lines[counter].strip('\n').split(' ')

    nextRow = lines[counter + 1].strip('\n')
    outputRows = []
    outputRowsCounter = 0
    while((counter + outputRowsCounter + 1) < len(lines) and nextRow.startswith('$ ') == False): # collect output until we find a new command
        outputRows.append(nextRow)
        outputRowsCounter += 1
        if(counter + outputRowsCounter + 2) <= len(lines):
            nextRow = lines[counter + 1 +outputRowsCounter].strip('\n')
        
    if(len(command) > 2):
        executedCommands.append(ExecutedCommand(command[1], outputRows, command[2]))
    else:
        executedCommands.append(ExecutedCommand(command[1], outputRows))

    counter += 1 + len(outputRows)

currentPath = ""
directories = []

for currentCommand in executedCommands:
    
    #print(currentPath + ' ' + currentCommand.command + ' ' + currentCommand.args)

    if(currentCommand.command == "cd"):
        if(currentCommand.args == '..'): # moving up
            currentPath = currentPath.replace(currentPath[currentPath.rindex('/'):], '')
            if(currentPath==''):
                currentPath = '/' # Fix if we´re at root
        else: #moving down
            if(currentPath == '/' or currentPath == ''):
                currentPath += currentCommand.args
            else:
                currentPath += '/' + currentCommand.args
    elif(currentCommand.command == 'ls'):
        filesSizes = []
        for outputRow in currentCommand.outputRows:
            if(outputRow[0].isnumeric()):
                fileSize = outputRow.strip('\n').split(' ')[0] # skipping file name
                filesSizes.append(float(fileSize))
        
        currentFolder = '/'
        if(currentPath != '/'):
            currentFolder = currentPath[currentPath.rindex('/'):]

        directories.append(directory(currentFolder, currentPath, filesSizes))
    
foldersWithSize = {}
                
for folder in directories:
  
    sizeInCurrentFolder = folder.getTotalFileSize()
    sizeInSubFolders = 0
    totalSizeSubFolders = 0
    for subFolder in directories:
        if((folder.path == '/' and subFolder.path != '/') or (subFolder.path.startswith(folder.path+'/') and subFolder.path != '/')):
            totalSizeSubFolders += subFolder.getTotalFileSize()
    
    totalSizeInFolder = sizeInCurrentFolder + totalSizeSubFolders
    print('Total size in ' + folder.name + ' is ' + str(totalSizeInFolder))
    foldersWithSize[folder.name] = totalSizeInFolder

filesystemSpace = 70000000
spaceRequired = 30000000
filesystemSpace = 70000000
currentlyFree = filesystemSpace - foldersWithSize['/']
neededSpace = spaceRequired-currentlyFree

candidates = {key:value for (key, value) in foldersWithSize.items() if value >= neededSpace}
sortedCandidates = {k: v for k, v in sorted(candidates.items(), key=lambda item: item[1])}

print(list(sortedCandidates.values())[0])