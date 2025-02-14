import csv
import re
import sys

def parse_log(file_path):
    with open(file_path, 'r') as file, open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Line', 'File', 'Message'])
        for line in file:
            if re.match(r'.*:\d+:.*', line):  # Find lines with line number, file, and message
                parts = line.strip().split(':', 2)
                writer.writerow(parts)
                
if __name__ == "__main__":
    log_file = sys.argv[1]
    parse_log(log_file)
