from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

#set default variable
current_top1 = "Blank"
i = 0

# create infinite loop to keep program running
while True:
    # use BeautifulSoup to get BBC web page and access top story #1 headline
    page = requests.get("https://www.bbc.co.uk/news")
    soup = BeautifulSoup(page.content, 'html.parser')
    top1_div = soup.find("div", attrs={"data-entityid": "container-top-stories#1"})
    top1_head = top1_div.h3.string

    # used to add timestamp to any change to top story
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    # check if top story headline has changed and print relevant result
    if(top1_head != current_top1):
        print("New Top Story!!! (", current_time, ")")
        print(top1_head)
        current_top1 = top1_head
        i=0
    else:
        if(i % 10 == 0):
            print("No change to top story, current top story is:")
            print(top1_head)
        else:
            print("...")
    i+=1
    # to add delay to loop re-running
    time.sleep(10.0)
