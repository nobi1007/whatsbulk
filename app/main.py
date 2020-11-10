import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication, QTextEdit, QFileDialog
from PyQt5 import QtGui as qt
from PyQt5 import QtCore as qtc
from utility import getDriver, formatToSendMessage, formatNames
from xpaths import searchNameXPath, writeMessageXPath, singleUploadMediaXPath, multipleUploadMediaXPath, attachButtonXPath, sendMultiMediaXPath


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.mediaFilePath = ""
        self.setWindowTitle("WhatsBulk")
        self.setStyleSheet("background-color:white;")
        self.setWindowIcon(qt.QIcon(os.getcwd() + "/../assets/logo.ico"))

        # recipient's name section
        self.lbl_name = QLabel("Recipient's Name: ", self)
        self.lbl_name.setGeometry(qtc.QRect(20, 20, 150, 20))
        self.text_name = QLineEdit(self)
        self.text_name.setGeometry(qtc.QRect(200, 20, 600, 30))

        # text message section
        self.lbl_msg = QLabel("Text message: ", self)
        self.lbl_msg.setGeometry(qtc.QRect(20, 80, 150, 20))
        self.text_msg = QTextEdit(self)
        self.text_msg.setGeometry(qtc.QRect(200, 80, 600, 100))

        # media message section
        self.lbl_media = QLabel("Media Upload: ", self)
        self.lbl_media.setGeometry(qtc.QRect(20, 200, 250, 20))
        fileBtn = QPushButton("Upload File", self)
        fileBtn.clicked.connect(self.fileBtnClicked)
        fileBtn.move(200, 200)
        self.uploaded_file = QLabel(
            " --- No file selected --- ", self)
        self.uploaded_file.setGeometry(qtc.QRect(320, 200, 550, 30))

        # media caption section
        self.lbl_caption = QLabel("Media Caption: ", self)
        self.lbl_caption.setGeometry(qtc.QRect(20, 240, 250, 20))
        self.text_caption = QTextEdit(self)
        self.text_caption.setGeometry(qtc.QRect(200, 240, 600, 80))

        # send message button
        btn = QPushButton("Send Message", self)
        btn.clicked.connect(self.buttonClicked)
        btn.setGeometry(qtc.QRect(200, 360, 400, 40))

        # status block
        self.lbl_status = QLabel("Status: ", self)
        self.lbl_status.setGeometry(qtc.QRect(20, 420, 250, 20))
        self.text_status = QTextEdit(self)
        self.text_status.setReadOnly(True)
        self.text_status.setGeometry(qtc.QRect(200, 420, 600, 200))

        self.setGeometry(300, 120, 900, 700)
        self.show()

    def fileBtnClicked(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '/Users/nobi1007/Desktop', "Image files (*.jpg *.gif *.png *.jpeg)")
        self.mediaFilePath = fname[0]
        self.uploaded_file.setText(self.mediaFilePath)

    def buttonClicked(self):
        toBePrinted = "Total Recepients =   "
        names = self.text_name.text().strip().split(",")
        names = formatNames(names)
        message = self.text_msg.toPlainText()
        toSendMessage = message.split("\n")
        toSendMessage = formatToSendMessage(toSendMessage)

        if "".join(names).strip() and ("".join(self.mediaFilePath).strip() or "".join(toSendMessage).strip()):
            self.statusBar().showMessage("")
            toBePrinted += "%d \n\n" % (len(names))
            toBePrinted += "Recepients : \n"
            for i in range(len(names)):
                toBePrinted += "%d. %s,  " % (i+1, names[i])
            toBePrinted += "\n\nMessage : \n"
            toBePrinted += message

            driver = webdriver.Firefox(executable_path=getDriver("Firefox"))
            driver.set_window_position(0, 0)
            driver.set_window_size(564, 768)
            driver.get('https://web.whatsapp.com')
            time.sleep(20)

            for user in names:
                searchEle = driver.find_element_by_xpath(searchNameXPath)
                searchEle.clear()
                searchEle.send_keys(user)
                searchEle.send_keys(Keys.RETURN)

                if self.mediaFilePath:
                    # click attach file
                    captionMsg = self.text_caption.toPlainText()
                    captionMsg = captionMsg.split("\n")
                    captionMsg = formatToSendMessage(captionMsg)
                    attachBtnEle = driver.find_element_by_xpath(
                        attachButtonXPath)
                    attachBtnEle.click()

                    inputMediaEle = driver.find_element_by_xpath(
                        singleUploadMediaXPath)
                    driver.execute_script(
                        "arguments[0].style.display = 'block';", inputMediaEle)

                    medias = [self.mediaFilePath]

                    for i in range(len(medias)):
                        media = medias[i]
                        if i > 0:
                            inputMediaEle = driver.find_element_by_xpath(
                                multipleUploadMediaXPath)
                            driver.execute_script(
                                "arguments[0].style.display = 'block';", inputMediaEle)
                        inputMediaEle.send_keys(media)
                        driver.implicitly_wait(2)

                    driver.implicitly_wait(1)

                    sendMultiMediaEle = driver.find_element_by_xpath(
                        sendMultiMediaXPath)
                    sendMultiMediaEle.clear()
                    sendMultiMediaEle.send_keys()
                    for line in captionMsg:
                        if line == "":
                            sendMultiMediaEle.send_keys(Keys.SHIFT, Keys.ENTER)
                        else:
                            sendMultiMediaEle.send_keys(line)
                            sendMultiMediaEle.send_keys(Keys.SHIFT, Keys.ENTER)
                    sendMultiMediaEle.send_keys(Keys.RETURN)

                meassageEle = driver.find_element_by_xpath(writeMessageXPath)
                meassageEle.clear()
                for line in toSendMessage:
                    if line == "":
                        meassageEle.send_keys(Keys.SHIFT, Keys.ENTER)
                    else:
                        meassageEle.send_keys(line)
                        meassageEle.send_keys(Keys.SHIFT, Keys.ENTER)

                meassageEle.send_keys(Keys.RETURN)
                time.sleep(1)
            driver.implicitly_wait(5)
            driver.close()
            self.text_status.setText(toBePrinted)
        else:
            self.statusBar().showMessage("No recepient/message entered")


app = QApplication(sys.argv)
GUI = Window()
app.exec_()
sys.exit()
app.exec_()  # this has to be added in mac and linux
