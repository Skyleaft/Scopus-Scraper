from elsapy.elsdoc import AbsDoc
from elsapy.elssearch import ElsSearch
from elsapy.elsclient import ElsClient
import re
import json
import os
from flask import Flask, request, render_template



def search_article(client, article, ID):
    doc_srch = ElsSearch(f"Title({article})",'scopus')
    doc_srch.execute(client, get_all = True)
    result = doc_srch.results
    if len(result) > 1:
        print('Artikel tidak ditemukan')
        for article in result:
            print(article['dc:title'])
        t = input('print the number of article you need info about')
        t -=1
        result = result[t]
    else:
        result = result[0]
    scp_id = re.findall(r'[0-9]+', result['dc:identifier'])[0]
    scp_doc = AbsDoc(scp_id = scp_id)
    scp_doc.read(client)
    with open('data.json', 'w') as outfile:
        json.dump(scp_doc.data, outfile)
    


if __name__ == '__main__':
    con_file = open("config.json")
    config = json.load(con_file)
    con_file.close()
    #ambil config api
    client = ElsClient(config['apikey'])
    #search_article(client,'Bitcoin influence on E-commerce',1)