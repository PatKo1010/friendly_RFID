Welcome to the friendly_RFID Project!
The purpose of this project is to provide a friendly UI to clone RFID devices

Make sure you have installed the proxmark 3 firmware installed on your device before you run!

File descriptions:
1. Validation.py: This file is used to test success of your RFID clone. It pops up a GUI with three buttons: One for granting privilege to store the contents of the card, one for 'Request access', to check if your clone worked and one for exiting. Note that only one card can be stored at a time before cloning. Successive read attempts will get overwritten.The program will read your UID and store it in an encrypted txt file. To test if your clone worked, run the program again and press 'request access'. if the program shows "valid card" then your clone is sucessful
2. main.py and main.html: Opens the front end of our project. Run 'uvicorn main:app --reload' to load the webpage and run the html to bring up the UI

ENJOY! 
