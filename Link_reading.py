import csv

fb_gourps_path = "./fb_groups.csv"

fb_groups_links = []
with open(fb_gourps_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        
        if row:
            first_column = row[0]
            if first_column =='Fb_group_Links':
                continue
            else:
                print(first_column)
                fb_groups_links.append(first_column)
