import os
import datetime
import requests
import shutil
import zipfile

months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

def download(url, fpath):
    dirname = os.path.dirname(fpath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    if not os.path.exists(fpath):
        print "Downloading: %s" % url
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(fpath, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)   

def run():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    for year in range(2015, 2019):
        for i, month in enumerate(months):
            if today < "%d-%02d" % (year, (i+1)):
                return
            for week in [1,2,3,4,5]:
                url = "http://ratedata.gaincapital.com/%d/%02d %s/USD_JPY_Week%d.zip" % (year, (i+1), month, week)
                fpath = "../download/%d/%02d_%s/USD_JPY_Week%d.zip" % (year, (i+1), month, week)
                download(url, fpath)

if __name__ == "__main__":
    run()
