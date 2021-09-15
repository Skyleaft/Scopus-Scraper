from elsapy.elsdoc import AbsDoc
from elsapy.elssearch import ElsSearch
from elsapy.elsprofile import ElsAuthor, ElsAffil
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
    doc_srch = ElsSearch("AU-ID(57204495477)",'author')
    doc_srch.execute(client)
    result = doc_srch.results
    if len(result) == 0 :
        print('Author tidak ditemukan')
    else:
        with open('author.json', 'w') as f:
            f.write(json.dumps(result))

def search_authorID(client, author):
    auth_srch = ElsAuthor(author_id=author)
    if auth_srch.read(client):
        print ("my_auth.full_name: ", auth_srch.full_name)
        with open('authorID.json', 'w') as f:
            f.write(json.dumps(auth_srch))
    else:
        print(client)
        print ("Read author failed.")

def printAll(client):
    my_aff = ElsAffil(affil_id = '60101411')
    if my_aff.read_docs(client):
        for doc in my_aff.doc_list:
            print (doc['dc:title'], doc['dc:identifier'], doc['authors'])
    else:
        print("Read Failed")
        

def search_afil(client, affiliation):
    doc_srch = ElsSearch(f"AFFILORG({affiliation})",'scopus')
    doc_srch.execute(client, get_all = False)
    result = doc_srch.results
    if len(result) == 0 :
        print('Instansi tidak ditemukan')
    else:
        with open('affiliation.json', 'w') as f:
            f.write(json.dumps(result))
