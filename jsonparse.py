import subprocess,os,glob
import json
#path="F:\TEST"
for filename in glob.glob('*.json'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f: 
      jsonfile= json.load(f)

#for i in jsonfile['blocks']:
Card=jsonfile["Card"]
UID=Card['UID']
ATQA=Card['ATQA']
SAK=Card['SAK']

blocks=list(jsonfile['blocks'].values())

print(blocks[0])
f.close()
#1k- UID,block 0
#4k- UID, Block 0, ATQA, SAK,

with open("cardinfo.txt",'w') as info:
   info.write(UID+'\n')
   info.write(blocks[0]+'\n')
   info.write(ATQA+'\n')
   info.write(SAK+'\n')
info.close()

os.remove(os.path.join(os.getcwd(), filename))