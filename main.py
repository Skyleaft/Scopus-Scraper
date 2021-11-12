from elsapy.elsclient import ElsClient
import json

from werkzeug.datastructures import Range
import scrapper
import connection
from tqdm import tqdm


if __name__ == '__main__':
    con_file = open("config.json")
    config = json.load(con_file)
    con_file.close()
    # ambil config api
    client = ElsClient(config['apikey'])
    #id_scopus=connection.loadScopusID()
    #data = scrapper.search_author(client,idsatu)
    #connection.insertPush(data,idsatu)

    for row in tqdm(connection.loadScopusID()):
        data = scrapper.search_author(client,row[0])
        connection.insertPush(data,row[0])
