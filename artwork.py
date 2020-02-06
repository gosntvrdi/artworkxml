import requests
import dicttoxml
from apscheduler.schedulers.blocking import BlockingScheduler

def artworkXML():
    url = ("https://public.radio.co/stations/s5ad4b474a/status")
    response = requests.get(url).json()
    xml = dicttoxml.dicttoxml(response)
    xmlString = xml.decode(encoding='UTF-8')
    with open("artwork.xml", "w") as f:
        f.write(xmlString)


scheduler = BlockingScheduler()
scheduler.add_job(artworkXML, 'interval', seconds=6, max_instances=1)
scheduler.start()
