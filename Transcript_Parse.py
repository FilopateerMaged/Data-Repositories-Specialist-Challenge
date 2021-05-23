import pandas as pd
import os
from xml.etree import ElementTree as ET

path = "E:\DataRepositories_Test\Video Transcripts" #declaring a path variable for ease of accessing multiple folders 
for filename in os.listdir(path):
    fullname = os.path.join(path, filename)
    nameOfFile = os.path.splitext(filename)[0] #saving the filename in a variable and removing the extension 
    # Parsing the files 
    tree = ET.parse(fullname)
    # Accessing the root element and wanted values
    root = tree.getroot()
    questions = root.findall("")
    rows=[] #Re Intialzing the list everytime to make sure there's no duplicates
   
    for question in root.iter('question'):
          if 'id' in question.attrib: #Making sure the id attribute exists since some files have it missing .get() wont work in this case
                question_id = question.attrib["id"]
                rows.append(("question_id",question_id))
                
    for question in root.iter('question'):
        if "media_identifier" in question.attrib:
            media_iden = question.attrib["media_identifier"]
            rows.append(("Identifier:",media_iden))
            
    for title in root.iter('question_title'):
            questionTitle = title.text   
            rows.append(("question title:",questionTitle))
            
    for time in root.iter('question'): #Obtaining the first P child inside Question to obtain the question's START_TIME
        time = question.find('p')
        start = time.find("s").attrib["start_time"]
        rows.append(("start_time:",start))
        

    for time in root.iter('question'): #Finding both the last P and S element to Obtain the question's  END_TIME
        time = question.find(".//p[last()]")
        end = time.find(".//s[last()]").attrib["end_time"] 
        rows.append(("end time:",end))
    
    
    df = pd.DataFrame(rows)
    df.to_csv(str(nameOfFile) +'.csv')

    

    
    
#print(lst)   
#print(rows)


