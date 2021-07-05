#!/usr/bin/python3 

import re
r = 'attack\.t\d+'
toWrite = open('parsedFile5.xml','w')
for line in open("sigwah.xml","r").readlines():
    splitted = line.split(',')
    newline = "\t\t<mitre>"
    flag = False
    for split in splitted:
        a = re.search(r, split)
        if(a!=None):
            flag = True
            # print(a.group())
            b = a.group().split('.')
            b = b[1].upper()
            newline += f"\n\t\t  <id>{b}</id>"
    newline += "\n\t\t</mitre>\n"
    if(flag == True):
        toWrite.write(newline)
    toWrite.write(line)


# line = '		<group>attack.discovery,attack.execution,attack.t1087,attack.t1075,attack.t1114,attack.t1059,MITRE</group>'
# line = '       <info type="link">https://car.mitre.org/wiki/CAR-2016-04-005 </info>'
# line = '       <group>attack.credential_access,attack.persistence,MITRE</group>'
# splitted = line.split(',')
# newline = "\t\t<mitre>"
# flag = False
# for split in splitted:
#     a = re.search(r, split)
#     if(a!=None):
#         flag = True
#         # print(a.group())
#         b = a.group().split('.')
#         b = b[1].upper()
#         newline += f"\n\t\t  <id>{b}</id>"
# newline += "\n\t\t</mitre>"
# if(flag == True):
#     print(newline)
