
import tkinter as tk
import subprocess
UID=''
#12 counting spaces
# UID: 00 00 00 00

def find_UID():
    process = subprocess.run(["pm3"], input="hf 14a info", encoding="utf-8", capture_output=True).stdout
    x=process.find("UID:")
    UIDs=''
    for i in range(x+5,x+16):
        if process[i] != ' ' and process[i] != '\n':
            UIDs+=process[i]
    return UIDs

def create_privilege():
    global UID
    print("Place the card to grant access to in the reader")
    UID=find_UID()
    print("\nPRIVILEGED CARD SET")

def check_privilege():
    print("Place the card on the reader")
    UID_check=find_UID()
    #print(UID_check+"\n")
    print(UID)
    if(UID_check == UID):
       print("VALID CARD!")
    else:
       print("INVALID CARD")
    

def exit_program():
   root.quit()

root = tk.Tk()
root.title("Main Menu")

# Create and place buttons on the window
tk.Label(root, text="Main Menu", font=("Arial", 20)).pack(pady=10)

tk.Button(root, text="Give Privilege", command=create_privilege).pack(pady=5)
tk.Button(root, text="Request Access", command=check_privilege).pack(pady=5)
tk.Button(root, text="Exit", command=exit_program).pack(pady=5)

root.mainloop()
