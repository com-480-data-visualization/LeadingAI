"""
This file is used to convert the raw data into json format.

The raw data is in the form of a csv file. The csv file is read and the data is stored in a dictionary.

We have the following columns in the csv file:

1. Country: Name of the country
2. Talent: Score for talent
3. Infrastructure: Score for infrastructure
4. Operating Environment: Score for operating environment
5. Research: Score for research
6. Development: Score for development
7. Government Strategy: Score for government strategy
8. Commercial: Score for commercial
9. Total score: Total score
10. Region: Region of the country
11. Political regime: Political regime of the country


The data is indexed by a 3 letter code for the country. The data is stored in the following format:

{
    "AFG": {
        "Country": "Afghanistan",
        "Talent": 2.0,
        "Infrastructure": 2.0,
        "Operating Environment": 2.0,
        "Research": 2.0,
        "Development": 2.0,
        "Government Strategy": 2.0,
        "Commercial": 2.0,
        "Total score": 2.0,
        "Region": "Asia",
        "Political regime": "Authoritarian"
    },
    ...
}

The first file is called data classic.json

"""

import csv
import json
import pycountry

def process_data():
    data = {}
    with open("./AI_index_db.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Country"]

            # convert the name to a ISO 3166-1 alpha-3 (3 letter code)
            # for the country

            try:
                country = pycountry.countries.search_fuzzy(name)[0]
                code = country.alpha_3
            except:
                
                if name == "Turkey":
                    code = "TUR"
                elif name == "Luxembourg":
                    code = "LUX"
                print(f"Country {name} not found, using {code}")

            data[code] = {
                "Country": row["Country"],
                "Talent": float(row["Talent"]),
                "Infrastructure": float(row["Infrastructure"]),
                "OperatingEnvironment": float(row["Operating Environment"]),
                "Research": float(row["Research"]),
                "Development": float(row["Development"]),
                "GovernmentStrategy": float(row["Government Strategy"]),
                "Commercial": float(row["Commercial"]),
                "TotalScore": float(row["Total score"]),
                "Region": row["Region"],
                "PoliticalRegime": row["Political regime"]
            }

    with open("data-classic.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    process_data()