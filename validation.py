from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QTimer
from PySide6.QtGui import QFont
import sys
from cryptography.fernet import Fernet
import subprocess

# Global counter to track when all animations are complete
animation_counter = 0
UID=''
UID_check=''
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

def reset_to_main_menu():
    print("Hello")
    # WHY THIS NO WORKKK?!
    for i in reversed(range(layout.count())): 
        widget = layout.itemAt(i).widget()
        if widget is not None:
            widget.deleteLater()

    # Add the main menu widgets back
    label = QLabel("Main Menu")
    label.setAlignment(Qt.AlignCenter)  
    layout.addWidget(label)

    button1 = QPushButton("Give Privilege")
    button1.clicked.connect(create_privilege)
    layout.addWidget(button1)

    button2 = QPushButton("Request Access")
    button2.clicked.connect(check_privilege)
    layout.addWidget(button2)

    button3 = QPushButton("Exit")
    button3.clicked.connect(lambda: handle_button_press(exit_program))
    layout.addWidget(button3)


    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(20)


    window.setLayout(layout)
    window.show()


def handle_button_press(function):
    global animation_counter
    animation_counter = 3  
    window.message_to_display = function()
    start_animations()

def complete_function_execution(function):
    window.message_to_display = function()
    start_animations()

def start_animations():
    global animation_counter
    animation_counter = 3  

    
    fade_and_move_out(button1)
    fade_and_move_out(button2)
    fade_and_move_out(button3)

def fade_and_move_out(button):
    global animation_counter

    
    fade_animation = QPropertyAnimation(button, b"windowOpacity")
    fade_animation.setDuration(2000)
    fade_animation.setStartValue(1)
    fade_animation.setEndValue(0)
    
    
    move_animation = QPropertyAnimation(button, b"geometry")
    move_animation.setDuration(1000)
    move_animation.setStartValue(button.geometry())
    move_animation.setEndValue(QRect(button.geometry().x() + 200, button.geometry().y(), button.width(), button.height()))

   
    fade_animation.start()
    move_animation.start()

    
    move_animation.finished.connect(animation_finished)

def animation_finished():
    global animation_counter
    animation_counter -= 1

    if animation_counter == 0:
        QTimer.singleShot(1000, reset_to_main_menu)

def show_message(message):
    
    for i in reversed(range(layout.count())): 
        widget = layout.itemAt(i).widget()
        if widget is not None:
            widget.deleteLater()

    
    message_label = QLabel(message)
    message_label.setAlignment(Qt.AlignCenter)
    message_label.setFont(QFont("Arial", 24, QFont.Bold))
    message_label.setWordWrap(True)
    layout.addWidget(message_label)


def create_privilege():
    global UID
    show_message("Place the card to grant access to in the reader")
    UID = find_UID()  
    QTimer.singleShot(2000, set_privileged_message)

def set_privileged_message():
    global UID
    key=Fernet.generate_key()
    with open('secret.key','wb') as key_file:
        key_file.write(key)
    key_file.close()
    fernet=Fernet(key)
    encrypted_UID=fernet.encrypt(UID.encode())
    with open("UID.txt","wb") as passfile:
        passfile.write(encrypted_UID)
    passfile.close()
    window.message_to_display = "PRIVILEGED CARD SET"
    show_message(window.message_to_display)
    start_animations()
    QTimer.singleShot(2000, reset_to_main_menu)


def check_privilege():
    show_message("Place the card on the reader")
    global UID_check 
    UID_check = find_UID()  
    QTimer.singleShot(2000, set_privileged_check)

    
def set_privileged_check():    
    global UID
    global UID_check
    with open("UID.txt",'rb') as uid:
        encrypted_UID=uid.read()
    uid.close()
    with open('secret.key','rb') as keyfile:
        key=keyfile.read()
    keyfile.close()
    fernet=Fernet(key)
    decrypted_UID=fernet.decrypt(encrypted_UID)
    UID=decrypted_UID.decode()
    if UID_check == UID:
        window.message_to_display = "VALID CARD!"
    else:
        window.message_to_display = "INVALID CARD"
    show_message(window.message_to_display)
    start_animations()

def exit_program():
    sys.exit()


app = QApplication(sys.argv)


dark_style = """
    QWidget {
        background-color: #1c1f24;
        color: #ffffff;
    }
    QLabel {
        color: #ffffff;
        font-size: 26px;
    }
    QPushButton {
        background-color: #283593;
        color: #ffffff;
        border: none;
        padding: 15px;
        font-size: 18px;
    }
    QPushButton:hover {
        background-color: #3f51b5;
    }
    QPushButton:pressed {
        background-color: #1a237e;
    }
"""

app.setStyleSheet(dark_style)


window = QWidget()
window.setWindowTitle("Main Menu")
window.setFixedSize(400, 300)  


layout = QVBoxLayout()


label = QLabel("Main Menu")
label.setAlignment(Qt.AlignCenter)  
layout.addWidget(label)

button1 = QPushButton("Give Privilege")
button1.clicked.connect(create_privilege)
layout.addWidget(button1)

button2 = QPushButton("Request Access")
button2.clicked.connect(check_privilege)
layout.addWidget(button2)

button3 = QPushButton("Exit")
button3.clicked.connect(lambda: handle_button_press(exit_program))
layout.addWidget(button3)


layout.setContentsMargins(20, 20, 20, 20)
layout.setSpacing(20)


window.setLayout(layout)
window.show()


sys.exit(app.exec())