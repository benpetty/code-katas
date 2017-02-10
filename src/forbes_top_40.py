# -*- coding: utf-8 -*-
u"""Forbes Top 40.

Write a function that,

- returns the name, net worth, and industry of the oldest billionaire
under 80 years old AND the youngest billionaire with a valid age.
- Oldest under 80, not including 80.
- You may not use a sorting function.
- You may not use any external library (you don’t need it).

Stretch Goals
Write another function that takes the company owned by the oldest under 80
and youngest billionaire and scrapes the web for its current stock price.
If the company is not public, have an appropriate message.
If the company is not an actual company, have an appropriate message.
"""


import json


def forbes():
    """Sort the richy guys."""
    with open('src/data/forbes_billionaires_2016.json') as data_list:
        data = data_list.read()
    if data[-3] == ',':
        data = data[:-3] + data[-2:]
    data = json.loads(data)
    oldest = data[0]
    youngest = data[0]
    for dude in data:
        if dude['age'] < 80 and dude['age'] > oldest['age']:
            oldest = dude
    for dude in data:
        if dude['age'] > 0 and dude['age'] < youngest['age']:
            youngest = dude
    return (oldest['name'], oldest['net_worth (USD)'], oldest['source'],
            youngest['name'], youngest['net_worth (USD)'], youngest['source'])
