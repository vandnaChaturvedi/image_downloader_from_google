from selenium import webdriver
from pathlib import Path
import time
import json
import sys
import getopt

PATH = Path.home() / "Desktop"  # Change this to where you stored your image folder
SPEED = 1  # Adjust to speed up the process. You do need a good internet connection for higher speeds.
# Otherwise images will be skipped

class Downloader:

    def __init__(self, image_folder, urlfile="urls.txt"):
        self.links = 0
        self.driver = webdriver.Firefox()  # This opens up Firefox. Change to your browser
        self.image_folder = PATH / image_folder
        self.urls_list_file = open(str(PATH / urlfile), "a")  # The URLs will be saved here

    def one_image(self, image_path, scroll):
        # This tries to upload on image from the provided folder (image_path) and downloads urls from similar images
        try:
            driver = self.driver
            links = []
            driver.get("https://www.google.com/imghp?hl=en&tab=wi&ogbl") # Opens google images
            time.sleep(3 / SPEED)
            driver.find_element_by_class_name("dRYYxd").click()
            driver.find_element_by_class_name("qbtbha.qbtbtxt.qbclr").click()
            driver.find_element_by_name("encoded_image").send_keys(image_path)
            time.sleep(5 / SPEED)
            driver.find_element_by_class_name("iu-card-header").click()
            time.sleep(3 / SPEED)
            for i in range(1, scroll):
                # This scroll the page down to load more images. Defined by 'scroll'
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            for pic_elem in driver.find_elements_by_css_selector(".rg_di .rg_meta"):
                link = json.loads(pic_elem.get_attribute('innerHTML'))['ou']
                links.append(link)
            self.save_to_txt(links)
        except:
            pass

    def all_images(self, scroll):
        # Loops through all images from folder and downloads all urls
        for path in list(self.image_folder.iterdir()):
            self.one_image(str(path), scroll)
            time.sleep(3 / SPEED)

    def save_to_txt(self, links):
        for link in links:
            self.urls_list_file.write(link + "\n")
        self.links += len(links)
        print(len(links))

    def run(self, scroll=2):
        self.all_images(scroll)
        self.driver.close()
        self.urls_list_file.close()
        print("All done")
        print(self.links) 
        print("links saved in total")


argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "f:txt:l:", ["folder", "txtfile", "length"])
    folder, txtfile, length = "", "", ""
    if (len(opts) == 0 and len(opts) > 1):
      print ("blusage: script.py -f <folder containing images> -txt <text file for urls> -l <higher number gives more pictures> ")
    else:
        for tpl in opts:
            if "-f" in tpl:
                folder = tpl[1]
            if "-txt" in tpl:
                txtfile = tpl[1]
            if "-l" in tpl:
                length = tpl[1]
        if txtfile is not "":
            downloader = Downloader(folder, txtfile)
        else:
            downloader = Downloader(folder)
        if length is not "":
            downloader.run(int(length))
        else:
            downloader.run()

except getopt.GetoptError:
    print ("usage: script.py -f <folder containing images> -txt <text file for urls> -l <higher number gives more pictures> ")
    sys.exit(2)
