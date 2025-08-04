#!/usr/bin/env python3
"""
This script will now  make  multi language 

Depending of each language is configured at the environment, the program 
shows a correspondent message.

Usage:

Make your LANG variable configured like:
    export LANG=pt_BR
"""
__version__ = "0.0.1"
__author__ = "Fabiano Alves"

# This script make upper to a string

import os

current_language = os.getenv("LANG", "en_US")[:5]
message = "Crash"

if current_language == "pt_BR":
    message = "Bateu"
elif current_language == "it_IT":
    message = "ha colpito"
    

print(message)
