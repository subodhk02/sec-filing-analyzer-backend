import csv, datetime, json

MONTHS = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

def get_timestamp_from_string(string):
    month, year = string.split(' ')
    month = MONTHS.index(month) + 1
    year = int(year)
    
    timestamp = datetime.datetime(year=year, month=month, day=1)
    return timestamp
    
    

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
                for item in row:
                    COLUMN_TIMESTAMPS.append(get_timestamp_from_string(item))       
            else:
                company_name = row.pop(0)
                # json_output[company_name] = []
                for index, item in enumerate(row):
                    # print(company_name, COLUMN_TIMESTAMPS[index], item or None)
                    json_output.append({
                        'company': company_name,
                        'timestamp': str(COLUMN_TIMESTAMPS[index]),
                        'revenue': float(item) if item else None
                    })
            line_count += 1
        
        file = open('revenue.json', 'w+')
        print(json.dumps(json_output), file = file)
        
        print(f'Processed {line_count} lines.')
    return data

extract_csv_data('./revenue.csv')