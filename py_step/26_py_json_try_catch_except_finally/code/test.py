import json

test_diction = {'a': 'a','b' : [1,2,3]}
json_data = json.dumps(test_diction, indent=1)
print(json_data)

