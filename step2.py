import subprocess
import glob
import os
import jsonparse
import inspect



def copy_4k():
    #open the txt generated by George
    with open('cardinfo.txt', 'r') as file:
        card_details = file.read().split("\n")
    
    #define the local variables
    UID = "script run hf_mf_ultimatecard -u" + card_details[0]
    block_0 = "hf mf wrbl --blk 0 -k B0B1B2B3B4B5 -b -d " + card_details[1] + " --force"
    ATQA = card_details[2]
    SAK = card_details[3]
    ATQA_SAK = "script run hf_mf_ultimatecard -q " + ATQA + SAK
    dump_file_name = "hf-mf-" + card_details[0] + "-dump.json"
    remainingblocks_script = "hf mf gload --4k -v -f " + card_details[0] + " --start 1"

    #initiate the cloning scripts for the pm3
    copy_process = subprocess.run(["pm3"], input=UID, encoding="utf-8", capture_output=True).stdout
    print(copy_process)
    print("UID cloned")
    copy_process_manufacturer = subprocess.run(["pm3"], input=ATQA_SAK, encoding="utf-8", capture_output=True).stdout
    print(copy_process_manufacturer)
    print("ATQA and SAK cloned")
    copy_process_block0 = subprocess.run(["pm3"], input=block_0, encoding="utf-8", capture_output=True).stdout
    print(copy_process_block0)
    print("Block 0 copied")
    copy_process_remaining = subprocess.run(["pm3"], input=remainingblocks_script, encoding="utf-8", capture_output=True).stdout
    print(copy_process_remaining)
    print("Remaining blocks copied")
    
    #delete the dump file
    for filename in glob.glob('*.bin'):
        os.remove(os.path.join(os.getcwd(), filename))


def copy_1k():
    with open('cardinfo.txt', 'r') as file:
        card_details = file.read().split("\n")
    
    #define local var
    UID = card_details[0]
    dump_file_name = "hf-mf-" + UID + "-dump.json"
    remainingblocks_script = "hf mf cload -f " + dump_file_name
    
    #initiate the scripts on pm3
    copy_process = subprocess.run(["pm3"], input=remainingblocks_script, encoding="utf-8", capture_output=True).stdout
    print(copy_process)
    print("Blocks cloned")
    
    #delete the dump file
    for filename in glob.glob('*.bin'):
        os.remove(os.path.join(os.getcwd(), filename))


#understand the standard (4k vs 1k vs everything else)
def clones():
    jsonparse.parsejson()
    process = subprocess.run(["pm3"], input="hf 14a info", encoding="utf-8", capture_output=True).stdout
    if (process.find("MIFARE Classic 4K")) !=-1:
        print("4k cloned")
        copy_4k()
        print("Copied 4k!")

        
    elif (process.find("MIFARE Classic 1K")) !=-1:
        copy_1k()
        print("1k cloned")
        
        
    else:
        print("No valid card")
     