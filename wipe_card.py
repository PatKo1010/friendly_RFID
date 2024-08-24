import subprocess
import glob
import os
import jsonparse
import inspect



def wipe_4k():
    
    #define the local variables
    UID = "005678BB"
    string_UID_change = "script run hf_mf_ultimatecard -u " + UID

    #initiate the UID change script for the pm3
    UID_change_process = subprocess.run(["pm3"], input=string_UID_change, encoding="utf-8", capture_output=True).stdout
    print("Card wiped")
    

#function to wipe 1k cards
def wipe_1k():
    
    #initiate cwipe scripts on pm3
    wipe_process = subprocess.run(["pm3"], input="hf mf cwipe", encoding="utf-8", capture_output=True).stdout
    print("Card Wiped")
    


#understand the standard (4k vs 1k vs everything else)
def wipe_card():
    #jsonparse.parsejson()
    process = subprocess.run(["pm3"], input="hf 14a info", encoding="utf-8", capture_output=True).stdout
    if (process.find("MIFARE Classic 4K")) !=-1:
        print("4k cloned")
        wipe_4k()
        print("Wiped 4k!")

        
    elif (process.find("MIFARE Classic 1K")) !=-1:
        wipe_1k()
        print("Wiped 1k")
        
        
    else:
        print("No valid card")
     

wipe_card()