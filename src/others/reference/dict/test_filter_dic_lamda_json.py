# Fitler cheras2 in the data_set
data_set = {
    '1730695523.0538654==Cheras, Kuala Lumpur, 55300, Malaysia': 'value',
    '1730695523.0538654==Cheras2, Kuala Lumpur, 55300, Malaysia': 'value2'
}

# Extract the key with 'Cheras2' using lambda function
filtered_data = dict(filter(lambda item: 'Cheras2' in item[0], data_set.items()))

print(filtered_data)