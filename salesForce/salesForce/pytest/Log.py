import datetime
import os
from selenium import webdriver


class Log:
    def __init__(self, test_case, env):
        base_path = r"D:\evidencias"
        self.tc = test_case
        self.path = base_path + "\\" + test_case + "_" + env + "_" + str(datetime.date.today().day) + str(
            datetime.date.today().month) + str(datetime.date.today().year)
        path_exist = os.path.exists(self.path)
        if not path_exist:
            os.makedirs(self.path)

    def save_log(self, log_text):
        path = self.path + "\\" + "log.txt"
        with open(path, "a") as log:
            log.writelines(str(datetime.datetime.now()) + " " + self.tc + " - " + log_text)
            log.writelines("\n")

    def save_screen(self, driver: webdriver, title):
        driver.save_screenshot(self.path + "\\" + self.tc + " - " + str(datetime.date.today().day) + str(
            datetime.date.today().month) + str(datetime.date.today().year) + " _ " + str(datetime.datetime.now().second) + " - " + title + ".png")

#
# log = Log("pospago", "PreProd")
# log.save_log("log")
# driver = webdriver.Chrome()
# url = "https://www.google.com/"
# driver.get(url)
# log.save_screen(driver,"Titulo")
