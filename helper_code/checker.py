import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from shutil import copyfile

path = 'C:/Users/Paulo/Documents/blood-cells/dataset2-master/dataset2-master/images/TRAIN/NEUTROPHIL_ANOTATIONS'
imgs =  'C:/Users/Paulo/Documents/blood-cells/dataset2-master/dataset2-master/images/TRAIN/NEUTROPHIL'

dsta = 'C:/Users/Paulo/Documents/blood-cells/dataset2-master/dataset2-master/images/TRAIN/first_test/shuffle2/Annotations'
dsti = 'C:/Users/Paulo/Documents/blood-cells/dataset2-master/dataset2-master/images/TRAIN/first_test/shuffle2/Images'

bad_files = []
for d in os.listdir(path):
    doc = ET.parse(os.path.join(path, d))
    name = doc.findall('*/name')

    if len(name) > 1:
        print(d + ' bad file')
        bad_files.append(d)

    for node in name:
        if node.text != 'NEUTROPHIL':
            node.text = 'NEUTROPHIL'
            print("file {0} bad name, correcting...".format(d))

print("Done! {0} files removed.".format(str(len(bad_files))))
for f in bad_files:
    os.remove(os.path.join(path, f))
    
for a in os.listdir(path):    
    for i in os.listdir(imgs):
        if os.path.splitext(a)[0] == os.path.splitext(i)[0]:
            na = "na" + a
            ni = "ni" + i
            copyfile(os.path.join(path, a), os.path.join(dsta, na))
            copyfile(os.path.join(imgs, i), os.path.join(dsti, ni))
            break
