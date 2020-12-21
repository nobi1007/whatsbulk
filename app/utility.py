import platform
import os


def getDriver(driver):
    system = platform.system()

    cdPath = os.getcwd()
    if driver == "Firefox":
        cdPath += "/WebDrivers/firefox"
        if system == "Darwin":
            cdPath += "/mac/geckodriver"
        elif system == "Windows":
            cdPath += "/windows/geckodriver"
        elif system == "Linux":
            cdPath += "/linux/geckodriver"

    elif driver == "Chrome":
        cdPath += "/WebDrivers/chrome"
        if system == "Darwin":
            cdPath += "/mac/chromedriver"
        elif system == "Windows":
            cdPath += "/windows/chromedriver"
        elif system == "Linux":
            cdPath += "/linux/chromedriver"
    return cdPath


def formatToSendMessage(message):
    for i in range(len(message)):
        message[i] = message[i].replace("\t", "    ")
    return message


def formatNames(names):
    op = []
    for i in names:
        op.append(i.strip())
    return op
