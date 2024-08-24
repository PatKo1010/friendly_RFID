import subprocess,os,glob
import json
def parsejson():
   #path="F:\TEST"
   for filename in glob.glob('*.json'):
      with open(os.path.join(os.getcwd(), filename), 'r') as f: 
         jsonfile= json.load(f)

   #for i in jsonfile['blocks']:
   Card=jsonfile["Card"]
   UID=Card['UID']
   ATQA_rev=Card['ATQA']
   ATQA= ATQA_rev[2:]+ATQA_rev[0:2]
   print(ATQA_rev)
   print(ATQA)
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

   # for filename in glob.glob('*.bin'):
   #    os.remove(os.path.join(os.getcwd(), filename))