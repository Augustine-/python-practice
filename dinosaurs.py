"""
You are given two CSV files containing data about dinosaurs. The first CSV file, dinosaurs.csv, contains the names of the dinosaurs along with whether they are bipedal or not. The second CSV file, measurements.csv, includes the same dinosaur names along with their leg length and stride length. Your task is to:

    Parse both CSV files.
    Identify which dinosaurs are bipedal.
    Calculate the speed of these bipedal dinosaurs using the formula:
    Speed=(stride lengthleg length)×leg length×g
    Speed=(leg lengthstride length​)×leg length×g

​
where g=9.8 m/s2g=9.8m/s2 is the acceleration due to gravity.
Output a list of bipedal dinosaurs, sorted by their speed in descending order.
"""