import os


dirName = '/home/nudlesoup/Research/MakingImagesfromDataset/trial1'
outputPath = '/home/nudlesoup/Research/MakingImagesfromDataset/trial2'
# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    for file in filenames:
        structure = os.path.join(outputPath, dirpath[len(dirName) + 1:],file)
     #   myfile = Path(structure)
        if os.path.isfile(structure):
            print("0")
        else:
            print("1")
    '''    if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            print("Folder does already exits!")'''
# listOfFiles += [os.path.join(dirpath, file) for file in filenames]


