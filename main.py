
from web import web
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def getAll():
	return web()

