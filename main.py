from itertools import count
from elsapy.elsclient import ElsClient
import json
import sys
import time

from werkzeug.datastructures import Range
import scrapper
import connection
from tqdm import tqdm


if __name__ == '__main__':
    #load config api
    con_file = open("config.json")
    config = json.load(con_file)
    con_file.close()
    # ambil config api
    client = ElsClient(config['apikey'])
    print("Scraping Data.....")
    #looping sebanyak data dosen yang memiliki id scopus
    data = connection.loadScopusID()
    print(len(data),'Author Found')
    #print(len(scrapper.search_author(client,'56829262300')))
    #manualdata = scrapper.search_author(client,'56829262300')
    #connection.insertPush(manualdata,56829262300)
    totaldoc=0
    for row in tqdm(data):
         #cari author dari scopus id
         datas = scrapper.search_author(client,row[0])
         print('   --=>',len(datas),'Document Found')
         totaldoc+=len(datas)
         #push ke database
         connection.insertPush(datas,row[0])
         datas.clear()
         time.sleep(1)
    print("Scraping Selesai",totaldoc,'dokumen ditambahkan')
