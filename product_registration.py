#!/usr/bin/env python3
"""
Product Registration
"""
__version__ = "0.1.1"
__author__ = "Fabiano Alves"

product = {
    "name": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

client = {"name": "Fabiano"}

buy = {
    "client": client,
    "product": product,
    "quantity": 3,
}

# pprint(buy)

total_buy = buy["quantity"] * buy["product"]["preco"]

print(f"The client {buy['client']['name']}"
      f" bought a {buy['quantity']} units of {buy['product']['name']}"
      f" and paid the total of {total_buy}")
