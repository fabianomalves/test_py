#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Displays children's reports by activity

Print a list of children, grouped by class
and attending each activity.
"""

__version__ = "0.1.0"
__author__ = "Fabiano Alves"

# Data
classroom_1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
classroom_2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

english_class = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
music_class = ["Erick", "Carlos", "Maria"]
dance_class = ["Gustavo", "Manuel", "Sofia", "Antonio"]

activities = [
    ("English", english_class),
    ("Music", music_class),
    ("Dance", dance_class),
]

# List student in each activity per class

for activity_name, activity in activities:
    print(f"Activity Studentes {activity_name}\n")
    print("-" * 40)

    activity_classroom_1 = []
    activity_classroom_2 = []

    for student in activity:
        if student in classroom_1:
            activity_classroom_1.append(student)
        elif student in classroom_2:
            activity_classroom_2.append(student)

    print("Classroom_1", activity_classroom_1)
    print("Classroom_2", activity_classroom_2)

    print()
    print("#" * 40)
