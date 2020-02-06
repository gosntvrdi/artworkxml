import requests
import dicttoxml


url = ("https://public.radio.co/stations/s5ad4b474a/status")
response = requests.get(url).json()
xml = dicttoxml.dicttoxml(response)
xmlString = xml.decode(encoding='UTF-8')
with open("artwork.xml", "w") as f:
    f.write(xmlString)


