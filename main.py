from elsapy.elsclient import ElsClient
import json
import sys

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
    for row in tqdm(connection.loadScopusID()):
        #cari author dari scopus id
        data = scrapper.search_author(client,row[0])
        #push ke database
        connection.insertPush(data,row[0])
    print("Scraping Selesai")
