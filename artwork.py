import requests
import dicttoxml
import json
from urllib.request import urlopen
from apscheduler.schedulers.blocking import BlockingScheduler

def artworkXML():
    url = ("https://public.radio.co/stations/s5ad4b474a/status")
    response = requests.get(url).json()
    urllink = urlopen(url).read()
    result = json.loads(urllink)
    xml = dicttoxml.dicttoxml(result)

    xmlString = xml.decode(encoding='UTF-8')
    print(xmlString)
    with open("artwork.xml", "w") as f:
        f.write(xmlString)


scheduler = BlockingScheduler()
scheduler.add_job(artworkXML, 'interval', seconds=10, max_instances=1)
scheduler.start()
