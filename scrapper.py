from elsapy.elsdoc import AbsDoc
from elsapy.elssearch import ElsSearch
import re
import json

def search_article(client, article):
    doc_srch = ElsSearch(f"Title({article})",'scopus')
    doc_srch.execute(client, get_all = False)
    result = doc_srch.results
    if len(result) == 0 :
        print('Artikel tidak ditemukan')
    else:
        with open('artikel.json', 'w') as f:
            f.write(json.dumps(result))


def rw_doc(client,scp_id):
    scp_doc = AbsDoc(scp_id = scp_id)
    scp_doc.read(client)
    #with open('data.json', 'w') as outfile:
        #json.dump(scp_doc.data, outfile)

def search_author(client, author):
    doc_srch = ElsSearch(f"AUTHOR-NAME({author})",'scopus')
    doc_srch.execute(client, get_all = True)
    result = doc_srch.results
    if len(result) == 0 :
        print('Author tidak ditemukan')
    else:
        with open('author.json', 'w') as f:
            f.write(json.dumps(result))

def search_afil(client, affiliation):
    doc_srch = ElsSearch(f"AFFILORG({affiliation})",'scopus')
    doc_srch.execute(client, get_all = False)
    result = doc_srch.results
    if len(result) == 0 :
        print('Instansi tidak ditemukan')
    else:
        with open('affiliation.json', 'w') as f:
            f.write(json.dumps(result))
