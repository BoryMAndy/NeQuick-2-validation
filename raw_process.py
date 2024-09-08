import os
import csv
import datetime as dt
import NeQuick_2 as nq


def get_file_paths(directory):
    # Returns a list of paths to files in the specified directory
    return [os.path.join(directory, f) for f in sorted(os.listdir(directory))]


def read_f107_data(f107_path):
    # Reads F107 data from CSV files and receives it as a dictionary
    f107_data = {}
    with open(f107_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = dt.datetime.strptime(row['time (yyyy MM dd)'], "%Y %m %d").date()
            f107_data[date] = float(row['absolute_f107 (solar flux unit (SFU))'])
    return f107_data


def process_swarm_file(file_path, f107_data, new_file):
    # Processes data from a Swarm file and writes the results to a new file
    with open(file_path, 'r') as swarm_file:
        date_temp = None
        num = 0  # counter to ignore file description

        for row in swarm_file:
            if num < 3:
                num += 1
                continue

            data = row.split()
            n_mes = data[0]
            date_str = data[1][:6] + '20' + data[1][6:]
            time_str = data[2]
            lat = float(data[3])
            lon = float(data[4])
            h = float(data[5])
            tec = data[15]

            date_dt = dt.datetime.strptime(date_str + ' ' + time_str, '%d-%m-%Y %H:%M:%S.%f')

            if date_temp is None or date_dt.date() != date_temp:
                # get new f107 index if its necessary 
                f107_temp = f107_data.get(date_dt.date(), None)
                if f107_temp is None:
                    print(f"No f107 data for {date_dt.date()}")
                    continue
                date_temp = date_dt.date()

            # time as hour of the day
            time_temp = date_dt.hour + date_dt.minute / 60 + date_dt.second / 3600 + date_dt.microsecond / 3600000000

            # NeQuick processing
            ne = nq.nequick(h, lat, lon, date_dt.month, f107_temp, time_temp)

            # write result
            new_file.write(f"{data[1]} {time_str} {h} {lat} {lon} {tec} {ne}\n")



swarm_data_path = '_C/'
f107_file_path = 'cls_radio_flux_f107(2014).csv'
result_file_path = 'Result_SWARM_C.txt'

# get list of swarm file paths
swarm_files = get_file_paths(swarm_data_path)

# read f107 file
f107_data = read_f107_data(f107_file_path)

# process data
with open(result_file_path, 'w') as result_file:
    for i, swarm_file in enumerate(swarm_files, start=1):
        process_swarm_file(swarm_file, f107_data, result_file)
        print(f"File {i} ({swarm_file}) processed")
