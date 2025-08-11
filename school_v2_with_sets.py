#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Displays children's reports by activity

Print a list of children, grouped by class
and attending each activity.
"""

__version__ = "0.1.1"
__author__ = "Fabiano Alves"

# Data
classroom_1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
classroom_2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

english_class = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
music_class = ["Erick", "Carlos", "Maria"]
dance_class = ["Gustavo", "Joana", "Sofia", "Antonio"]

activities = [
    ("English", english_class),
    ("Music", music_class),
    ("Dance", dance_class),
]

# List student in each activity per class

for activity_name, activity in activities:
    print(f"Activity Studentes {activity_name}\n")
    print("-" * 40)

    # Classroom_1 intersection with activity
    activity_classroom_1 = set(classroom_1).intersection(set(activity))
    activity_classroom_2 = set(classroom_2).intersection(set(activity))

    print("Classroom_1", activity_classroom_1)
    print("Classroom_2", activity_classroom_2)

    print()
    print("#" * 40)
