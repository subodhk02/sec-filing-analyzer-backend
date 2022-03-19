import csv, datetime, json


def get_timestamps_from_year(string):
    start_year, end_year = string.split('-')
    start_year = int(start_year)
    end_year = int(end_year)
    start_timestamp = datetime.datetime(year=start_year, month=4, day=1)
    end_timestamp = datetime.datetime(year=end_year, month=3, day=30)
    return [ start_timestamp, end_timestamp ]
    

def extract_csv_data(file):
    data = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        COLUMN_TIMESTAMPS = []
        
        json_output = []
        
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                row.pop(0)
                print(row)
                for item in row:
                    COLUMN_TIMESTAMPS.append(get_timestamps_from_year(item))
            else:
                company_name = row.pop(0)
                for index, item in enumerate(row):
                    json_output.append({
                        'company': company_name,
                        'start_timestamp': str(COLUMN_TIMESTAMPS[index][0]),
                        'end_timestamp': str(COLUMN_TIMESTAMPS[index][1]),
                        'ebitda': float(item) if item else None
                    })
            line_count += 1
        
        file = open('ebitda.json', 'w+')
        print(json.dumps(json_output), file = file)
        
        print(f'Processed {line_count} lines.')
    return data

extract_csv_data('./ebitda.csv')