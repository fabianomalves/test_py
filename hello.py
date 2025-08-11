#!/usr/bin/env python3
"""
This script will now  make  multi language 

Depending of each language is configured at the environment, the program 
shows a correspondent message.

Usage:

Make your LANG variable configured like:
    export LANG=pt_BR
"""
__version__ = "0.1.1"
__author__ = "Fabiano Alves"

import os

current_language = os.getenv("LANG", "en_US")[:5]

message = {
    "en_US": "Crash",
    "pt_BR": "Bateu",
    "it_IT": "ha colpito",
}

print(message[current_language])
