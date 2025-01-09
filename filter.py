import os 
import pandas as pd
import csv

root_log_folder = os.path.join(os.getcwd(), 'csvs')

if os.path.exists(root_log_folder):
    log_files = [f for f in os.listdir(root_log_folder) if os.path.isfile(os.path.join(root_log_folder, f))]
    log_files = [f for f in log_files if f.endswith('.csv')]

data = {}
for file in log_files:
    path = os.path.join(root_log_folder, file)
    with open(path,'r') as file:
        reader = list(csv.reader(file))
        for row in reader[1:]:
            if row[2] in data.keys():
                data[row[2]]+=0 if row[-2]=='' else float(row[-2])
            else:
                data[row[2]] = 0 if row[-2]=='' else float(row[-2])

for key,value in data.items():
    with open('holidays.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([key,value])
    
    

