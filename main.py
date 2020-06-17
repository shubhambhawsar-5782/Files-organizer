import os

#This function for creating folder if not exists previously
def createIfnotExists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

#This function for moving files 
def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")

#show the files or directory
files=os.listdir()
files.remove('main.py')
#print(files)

createIfnotExists('Images')
createIfnotExists('Docs')
createIfnotExists('Media')
createIfnotExists('Others')

imgExts = ['.png','.jpeg','.jpg']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
#print(images)

docsExts = ['.docx','.txt','.doc','.pdf']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExts]
#print(docs)

mediaExts = ['.mkv','.mp4','.mp3']
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
#print(media)

others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docsExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)
#print(others)

move("Images",images)
move("Docs",docs)
move("Media",media)
move("Others",others)
