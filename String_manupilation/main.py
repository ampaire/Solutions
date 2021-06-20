import sys
import re
import csv

def read_file(file):
  warnings = ["UVM_INFO", "UVM_WARNING", "UVM_ERROR"]

  with open(file, "r") as f:
    field_names = [
      'message type', 
      'hierarchical location', 
      'filename', 
      'line number', 
      'time', 
      'message'
    ]

    rows = []

    for line in f:
      if line.split()[0] in warnings:
        if re.search( '../..//*',line.split()[1]):
          message_type = line.split()[0]
          hierarchical_location = line.split()[4]
          file_name = line.split()[1].split('/')[-1].split('(')[0]
          line_number = line.split()[1].split('/')[-1].split('(')[-1].split(')')[0]
          time = line.split()[3].split('n')[0]
          message = " ".join(line.split()[5: len(line.split())])

          record = {
            'message type': message_type, 
            'hierarchical location': hierarchical_location, 
            'filename': file_name, 
            'line number': line_number, 
            'time': time, 
            'message': message
          }

          rows.append(record)
    
    with open('error_logs.csv', 'w', encoding='UTF8', newline='') as f:
      writer = csv.DictWriter(f, fieldnames=field_names)
      writer.writeheader()
      writer.writerows(rows)

def main():
  file = sys.argv[1]
  read_file(file)

if __name__ == '__main__':
  main()