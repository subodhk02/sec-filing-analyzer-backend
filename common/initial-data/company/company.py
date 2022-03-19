import csv

def extract_csv_data(file):
    data = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        json_output = []
        
        line_count = 0
        for row in csv_reader:
            index = row[0]
            company_name = row[1]
            cik = row[2]
            
            json_output.append({
                'name': company_name,
                'cik_number': cik
            })
            line_count += 1
        
        file = open('company.json', 'w+')
        print(json_output, file = file)
        
        print(f'Processed {line_count} lines.')
    return data

extract_csv_data('./company.csv')