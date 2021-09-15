from elsapy.elsclient import ElsClient
import json
import scrapper
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('myIndexTemplate.html')

@app.route("/artikel")
def artikel():
    name = request.args.get("name")
    scrapper.search_article(client,name)
    data_file = open("artikel.json")
    data = json.load(data_file)
    return jsonify(data)

@app.route("/author")
def author():
    name = request.args.get("name")
    scrapper.search_author(client,name)
    data_file = open("author.json")
    data = json.load(data_file)
    return jsonify(data)

@app.route("/afil")
def affiliation():
    name = request.args.get("name")
    scrapper.search_afil(client,name)
    data_file = open("affiliation.json")
    data = json.load(data_file)
    return jsonify(data)


# API Routing to get JSON file
@app.route("/readFile")
def readFileRoute():
    data_file = open("artikel.json")
    data = json.load(data_file)
    return jsonify(data)


if __name__ == '__main__':
    con_file = open("config.json")
    config = json.load(con_file)
    con_file.close()
    #ambil config api
    client = ElsClient(config['apikey'])
    #scrapper.search_authorID(client,57204495477)
    scrapper.search_author(client,'57204495477')
    #scrapper.search_article(client,'Virtual Reality Education')
    #scrapper.search_afil(client,'Universitas Komputer Indonesia')
    #app.run()