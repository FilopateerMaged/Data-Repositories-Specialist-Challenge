import pandas as pd
import os
from xml.etree import ElementTree as ET

path = "E:\DataRepositories_Test\Explainers" #declaring a path variable for ease of accessing multiple folders 
lst = [] 
i = 0
for filename in os.listdir(path):
    fullname = os.path.join(path, filename)
    # Parsing the files 
    tree = ET.parse(fullname)
    # Accessing the root element and wanted values
    root = tree.getroot()
    developer_id = root.attrib['id']
    seo_metadata = root.find('seo_meta_description')
    Dev_Name = root.find("developer_name")
    source_Id = root.find("source_id")
    i = i+1    
    filename= "file" + str(i)
    #Making sure selected tags dont return None when it comes to text/attributes
    #if all(elem is not None for elem in[Dev_Name,source_Id,seo_metadata]): #this cause a bug of giving non values and repeating the loop that I couldn't fix
    if Dev_Name is not None:
        name = Dev_Name.text
    if seo_metadata is not None:    
        seo = seo_metadata.text
    if source_Id is not None:
        source = source_Id.text
        
    
     #appending every 4 values to the list 
    lst.append((filename,developer_id,name,seo,source))
      

    

df = pd.DataFrame(lst)
df.to_csv('Explainers.csv')
#print(lst)