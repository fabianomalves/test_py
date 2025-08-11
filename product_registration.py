#!/usr/bin/env python3
"""
Product Registration
"""
__version__ = "0.1.0"
__author__ = "Fabiano Alves"

produto_nome = "Caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 45678
produto_codebar = None


compra = ("Bruno", produto_nome, 3)
total_compra = compra[2] * produto_preco

print(
    f"The client {compra[0]}, bought a {compra[1]}"
    f" and paid the total of {total_compra}"      
)
