import os

filename="/home/hrushikesh/door.png"
print("using",os.name,"...")
print("split","-->",os.path.split(filename))
print("splitext", "=>", os.path.splitext(filename))#it's split-extension
print("dirname", "=>", os.path.dirname(filename))
print("basename", "=>", os.path.basename(filename))
print("join", "=>", os.path.join(os.path.dirname(filename),os.path.basename(filename)))
print("using sep","=>",filename.split(os.path.sep))
print("without sep","=>",filename.split())
print("using /","=>",filename.split("/"))

'''
using posix ...
split --> ('/home/hrushikesh', 'door.png')
splitext => ('/home/hrushikesh/door', '.png')
dirname => /home/hrushikesh
basename => door.png
join => /home/hrushikesh/door.png
using sep => ['', 'home', 'hrushikesh', 'door.png']
without sep => ['/home/hrushikesh/door.png']
using / => ['', 'home', 'hrushikesh', 'door.png']
'''

FILES= (
        os.curdir, #different from os.getcwd(). This returns '.'
        "/",
        "file",
        "/file",
        "samples",
        "samples/sample.jpg",
        "directory/file",
        "../directory/file",
        "/directory/file")

for File in FILES:
    print(File,"-->")
    if os.path.exists(File):print("exists") 
    if os.path.isabs(File):print("ISABS"), #absolute path or not
    if os.path.isdir(File):print("ISDIR"), 
    if os.path.isfile(File):print("ISFILE"),
    if os.path.ismount(File):print("ISMOUNT")
            
for (root,dirs,files) in os.walk(os.curdir, topdown=True):
    print(root)
    print(dirs)
    print(files)

# Say you have 
p=["home","desktop"]
print(os.path.sep.join(p))  # home/desktop
print("#".join(p))          # home#desktop
# join() method takes all methods in an iterable and joins them into one string
