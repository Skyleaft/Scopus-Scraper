from asyncio.windows_events import NULL
import json
from tokenize import String
import mysql.connector
from datetime import datetime
from tqdm import tqdm

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    database="db_scopus"
)


def loadScopusID():
    cursor = db.cursor()
    if db.is_connected():
        sql = "SELECT id_scopus FROM author WHERE id_scopus is not null"
        cursor.execute(sql)
        records = cursor.fetchall()
        return records


def insertPush(data, scopus_id):
    cursor = db.cursor()
        
    for i in data:
        if db.is_connected():
            sql = "REPLACE INTO publisher(issn, publication_name, aggregation_type, createAt, updateAt) VALUES(%s,%s,%s,%s,%s)"
            try:
                val = (i['prism:issn'], i['prism:publicationName'],
                       i['prism:aggregationType'], datetime.now(), datetime.now())
            except:
                try:
                    val = (i['prism:isbn'][0]['$'], i['prism:publicationName'],
                       i['prism:aggregationType'], datetime.now(), datetime.now())
                except:
                    val = ('', i['prism:publicationName'],
                       i['prism:aggregationType'], datetime.now(), datetime.now())
            cursor.execute(sql, val)
            db.commit()

        if db.is_connected():
            sql = "REPLACE INTO documents(identifier,eid, doi, tittle, type, coverDate, volume, citiedCount, scopus_id, issn, createAt, updateAt, page) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            eid = i['eid']
            uniqtuple = eid[7:],'-',scopus_id
            uniq = ''.join(uniqtuple)
            try:
                val = (uniq,i['eid'], i['prism:doi'], i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], i['prism:volume'], i['citedby-count'],
                       scopus_id, i['prism:issn'], datetime.now(), datetime.now(),i['prism:pageRange'])
            except:
                try:
                    val = (uniq,i['eid'], NULL, i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], i['prism:volume'], i['citedby-count'],
                           scopus_id, i['prism:issn'], datetime.now(), datetime.now(), i['prism:pageRange'])
                except:
                    try:
                        val = (uniq,i['eid'], i['prism:doi'], i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], '', i['citedby-count'],
                           scopus_id, i['prism:isbn'][0]['$'], datetime.now(), datetime.now(), i['prism:pageRange'])
                    except:
                        val = (uniq,i['eid'], NULL, i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], '', i['citedby-count'],
                           scopus_id, '', datetime.now(), datetime.now(), i['prism:pageRange'])
            cursor.execute(sql, val)
            db.commit()