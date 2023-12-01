import json

def write_to_json(obj, file_name, method = 'a'):
    with open(file_name, method) as json_file:
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

  
def delete_all_objects(file_path):
    try:
        # Open the JSON file and read its content line by line
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Open the same file in write mode and clear its content
        with open(file_path, 'w') as file:
            pass  # Clear the file content

        print(f"All objects deleted from '{file_path}'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def write_to_json_dict(obj, file_name, method = 'a'):
    with open(file_name, method) as json_file:
        json.dump(obj, json_file)
        json_file.write('\n')