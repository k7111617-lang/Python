country_code={"Jamaica": "0067", "UAE": "00971", "UK": "0044", "USA": "001", "India": "0091"}
print("The country code for Jamaica is: ")
print(country_code.get("Jamaica", "Not found"))
print("The country code for USA is: ")
print(country_code.get("USA", "Not found"))
print("The country code for Democratic Republic of Congo is: ")
print(country_code.get("Democratic Republic of Congo", "Not found"))