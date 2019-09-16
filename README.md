
Python Image URL Downloader Script

I have found that google finds much better images if you supply an example image compared to a keyword image search. That is why I have created this simple python script, which uploads your handpicked images from a defined folder to google image search and downloads all the urls.
IMPORTANT

So far this script only works for firefox. You need selenium and geckodriver installed!
Instructions:

Please change into your desired working directory and change the PATH variable in the script.

The default PATH is set to your Desktop, this is where your folder containing your handpicked images should be and the urls.txt will also be saved here.

To run the script type (assuming the script is on your desktop):

$ cd Desktop

$ python imagescript.py -f <folder with your images> [-txt <outputURLs.txt>] [-l <some number>]

or

$ cd Desktop

$ python3 imagescript.py -f <folder with your images> [-txt <outputURLs.txt>] [-l <some number>]

Higher -l will scroll the page more, thus give more URLs for one image if available.

This script will open a web browser, don't close it!

150 handpicked images got me around 28000 URLs in ~40 min time.
