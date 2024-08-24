import subprocess

type = 0
process = subprocess.run(["pm3"], input="hf 14a info", encoding="utf-8", capture_output=True).stdout
if (process.find("MIFARE Classic 4K")) !=-1:
    print("4k cloned")
    tyoe = 1
    #print(subprocess.run(["pm3"], input="hf mf autopwn --4k", encoding="utf-8", capture_output=True).stdout)
elif (process.find("MIFARE Classic 1K")) !=-1:
    print("1k cloned")
    type = 2
    #print(subprocess.run(["pm3"], input="hf mf autopwn", encoding="utf-8", capture_output=True).stdout)
else:
    print("No valid card")
    type = 3 