import os
import shutil
from xml.etree import ElementTree as ET
new_path = "Updated" #Naming the directory 
main_path = "E:\DataRepositories_Test" #Getting the exact path of the current directory
path = os.path.join(main_path,new_path)
old_path = "E:\DataRepositories_Test\Explainers"   #Getting the exact path of the Explainers
os.mkdir(path) #Creating the directory
old_path = "E:\DataRepositories_Test\Explainers"

for filename in os.listdir(old_path): #looping over the files and copying them to the "Updated" Folder
    full_file_name = os.path.join(old_path, filename)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, new_path)

for filename in os.listdir(new_path):
    fullname = os.path.join(new_path, filename)
    tree = ET.parse(fullname)
    root = tree.getroot()
    paragraphs = root.findall("")
    for p in root.iter("p"):
        par = p.text #Assigning the text to a variable
        p.text= None #Removing the text from the <p> tag
        s = ET.Element("s") #creating the element <s>
        s.text=par #adding the text taken from the p element to the new s element
        p.insert(1,s) #appending the s element as the first child of the p element
    tree.write(fullname) #updating the file and outputing it

