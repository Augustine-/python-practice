"""
You are given two CSV files containing data about dinosaurs.
The first CSV file, dinosaurs.csv, contains the names of the dinosaurs along with whether they are bipedal or not.
The second CSV file, measurements.csv, includes the same dinosaur names along with their leg length and stride length.
Your task is to:

    Parse both CSV files.
    Identify which dinosaurs are bipedal.
    Calculate the speed of these bipedal dinosaurs using the formula:
    Speed=(stride length) x leg length x g


where g=9.8 m/s2 g=9.8m/s2 is the acceleration due to gravity.
Output a list of bipedal dinosaurs, sorted by their speed in descending order.
"""
import csv
dinos = {}

with open("dinosaurs/dinosaurs.csv") as dinosaurs:
    dinoreader = csv.DictReader(dinosaurs)
    for dino in dinoreader:
        for k, v in dino.items():
            if k == 'Name':
                name = v
                dinos[v] = {}
            else:
                dinos[name][k] = v

with open("dinosaurs/measurements.csv") as measurements:
    measurereader = csv.DictReader(measurements)
    for dino in measurereader:
        for k, v in dino.items():
            if k == 'Name':
                name = v
            else:
                dinos[name][k] = v

for dino in dinos:
    dino['speed'] = float(dino['Stride Length']) * float(dino['Leg Length']) * 9.8

sorted(dinos)
print(dinos)
