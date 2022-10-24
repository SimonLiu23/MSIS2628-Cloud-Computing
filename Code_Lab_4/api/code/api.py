from random import randint
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def get_meal_recommendation():

	meals = [
		{'name':'Krabby Patty', 'price':5.99},
		{'name':'Krabby Patty Deluxe', 'price':6.99},
		{'name':'Krabby Patty Jr', 'price':3.99},
		{'name':'Vegan Krabby Patty', 'price':6.99},
		{'name':'Krabby Double Patty', 'price':7.99},
		{'name':'Krabby Triple Patty', 'price':9.99},
		{'name':'Krabby Fries', 'price':2.99},
		{'name':'Krabby Fries with Cheese', 'price':3.99},
		{'name':'Krabby Vanilla Shake', 'price':3.99},
		{'name':'Krabby Chocolate Shake', 'price':3.99},
		{'name':'Krabby Strawberry Shake', 'price':3.99},
		{'name':'Krabby Onion Rings', 'price':2.99},
		{'name':'Soda', 'price':1.99}
	]

	return meals[randint(0,(len(meals)-1))]

@app.route('/')
@app.route('/recommendation/')
def index():
	return jsonify(get_meal_recommendation())

app.run(host='0.0.0.0', port=os.environ.get('API_PORT'))



