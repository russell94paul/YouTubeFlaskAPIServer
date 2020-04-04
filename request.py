import requests
import json
from pandas import DataFrame
from pandas.io.json import json_normalize



with requests.get("http://127.0.0.1:5000/videos", stream=True) as r:
    
    # Parsing JSON Object
    data = json.loads(r.text)

    # Json normalize
    df = json_normalize(data["videos"])
    # Converting the views column from string to int in order for it to be sorted
    df["views"] = df["views"].astype(int)
    df.sort_values(by=["views"], inplace=True, ascending=False)

    # Variable to store top 10 videos with the most views
    top10_results = df.head(10)
    print(top10_results)

 



