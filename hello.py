#!/usr/bin/env python3
"""
This script will now  make  multi language

Depending of each language is configured at the environment, the program
shows a correspondent message.

Usage:

Make your LANG variable configured like:
    export LANG=pt_BR
Or informa through the CLI argument '--lang'

Or the user must type.

"""
__version__ = "0.1.3"
__author__ = "Fabiano Alves"

import os
import sys

print(f"{sys.argv=}")

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Create ValueError validation
    key, value = arg.split("=")
    key = key.lstrip("--").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: use repetition
    if current_language is None:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

message = {
    "en_US": "Crash",
    "pt_BR": "Bateu",
    "it_IT": "ha colpito",
}

print(message[current_language] * int(arguments["count"]))
