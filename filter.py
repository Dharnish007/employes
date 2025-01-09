import os 
import pandas as pd
import csv

root_log_folder = os.path.join(os.getcwd(), 'csvs')

month = {'Jan':2,'Feb':0,'Mar':0,'Apr':2,'May':1,'Jun':0,'Jul':0,'Aug':1,'Sep':0,'Oct':2,'Nov':1,'Dec':1}

if os.path.exists(root_log_folder):
    log_files_file = [f for f in os.listdir(root_log_folder) if os.path.isfile(os.path.join(root_log_folder, f))]
    log_files = [f for f in log_files_file if f.endswith('.csv')]

data = {}
for file in log_files:
    path = os.path.join(root_log_folder, file)
    with open(path,'r') as file:
        reader = list(csv.reader(file))
        for row in reader[1:]:
            if row[2] in data.keys():
                data[row[2]]+=0 if row[-2]=='' else float(row[-2])-month[path.split()[-2][:3]]
            else:
                data[row[2]] = 0 if row[-2]=='' else float(row[-2])-month[path.split()[-2][:3]]

for key,value in data.items():
    with open('holidays.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([key,value])
    
    

