import json
import mysql.connector
from datetime import datetime
from tqdm import tqdm

db = mysql.connector.connect(
    host="localhost",
    port="39000",
    user="milzandb",
    passwd="@RootDBCybercode",
    database="db_scopus"
)


def loadScopusID():
    cursor = db.cursor()
    if db.is_connected():
        sql = "SELECT id_scopus FROM author"
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
                val = (i['prism:isbn'][0]['$'], i['prism:publicationName'],
                       i['prism:aggregationType'], datetime.now(), datetime.now())
            cursor.execute(sql, val)
            db.commit()

        if db.is_connected():
            sql = "REPLACE INTO documents(eid, doi, tittle, type, coverDate, volume, citiedCount, scopus_id, issn, createAt, updateAt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            try:
                val = (i['eid'], i['prism:doi'], i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], i['prism:volume'], i['citedby-count'],
                       scopus_id, i['prism:issn'], datetime.now(), datetime.now())
            except:
                try:
                    val = (i['eid'], i['openaccessFlag'], i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], i['prism:volume'], i['citedby-count'],
                           scopus_id, i['prism:issn'], datetime.now(), datetime.now())
                except:
                    val = (i['eid'], i['prism:doi'], i['dc:title'], i['subtypeDescription'], i['prism:coverDate'], i['prism:pageRange'], i['citedby-count'],
                           scopus_id, i['prism:isbn'][0]['$'], datetime.now(), datetime.now())
            cursor.execute(sql, val)
            db.commit()
