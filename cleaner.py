import csv
import json
from collections import OrderedDict

# Declaring the column names in the csv
fieldnames = (
    "video_id", "video_title", "views", "comments"
)
# Used to store all the data so it can be put inside the videos key
entries = []

# Open both the csv and a new json file (where csv data will be converted and dumped into)
with open('./results-20191105-104506.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames)
    next(csvfile)
    for row in reader:
            entry = OrderedDict()
            for field in fieldnames:
                entry[field] = row[field]
            entries.append(entry)

            output = {
                "videos": entries
            }
with open('./results-20191105-104506.json', 'w') as jsonfile:
    # Use JSON library to output the data
    json.dump(output, jsonfile)
    # Write new line at end of file (best practice)
    jsonfile.write('\n')




