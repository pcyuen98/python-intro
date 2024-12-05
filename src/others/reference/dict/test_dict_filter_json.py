data = {
    "11111==Cheras": [
        {"title": "THE BEST 1 ...", "description_my": "", "description_cn": ""},
        {"title": "THE BEST 2 ...", "description_my": "", "description_cn": ""},
    ],
    "2222==Cheras2": [
        {"title": "THE BEST 3 ...", "description_my": "", "description_cn": "Some values 1"},
        {"title": "THE BEST 4 ...", "description_my": "", "description_cn": ""},
    ],
    "3333==Cheras2": [
        {"title": "THE BEST 5 ...", "description_my": "", "description_cn": "Some values 2"},
        {"title": "THE BEST 6 ...", "description_my": "", "description_cn": "Some values 3"},
    ]
}

raw_data_from_cache = {key: value for key, value in data.items() if "Cheras2" in key}
is_cache_exist = len(raw_data_from_cache) > 0

print ('is_cache_exist-->', is_cache_exist)

# Find the record description_cn with some values and all arrays not blank
filtered_data = {key: value for key, value in raw_data_from_cache.items() 
                 if all(item["description_cn"] != "" for item in value) and all(item["description_cn"] for item in value)}
is_data_processed = len(filtered_data) > 0

print(filtered_data.values())

first_key = filtered_data.values()

