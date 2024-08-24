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
print(blocks)
