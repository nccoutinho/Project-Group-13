import json

def write_to_json(obj, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(obj.__dict__, json_file)
        json_file.write('\n')

def read_from_json(file_name):
    result_list = []
    try:
        with open(file_name, 'r') as json_file:
            for line in json_file:
                result_list.append(json.loads(line))
    except FileNotFoundError:
        pass  # If the file is not found, return an empty list
    return result_list