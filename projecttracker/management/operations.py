from projecttracker.utils import file_handler
from projecttracker.utils import input_handler
import pandas as pd
from IPython.display import clear_output

class Operations:
    def __init__(self):
        self.projects = {}
        self.tasks = {}
        
    def view(self):
        try:
            # Read projects and tasks from JSON files
            projects_from_json = file_handler.read_from_json('project.json')
            tasks_from_json = file_handler.read_from_json('task.json')

            # Check if both projects and tasks data are available
            if not projects_from_json:
                print("No data available for projects.")
                return None
            elif not tasks_from_json:
                project_df = pd.DataFrame(projects_from_json)
                return project_df.head(10)
            else:
                # Convert data to pandas DataFrame
                project_df = pd.DataFrame(projects_from_json)
                task_df = pd.DataFrame(tasks_from_json)

                # Merge projects and tasks separately using left merge
                result_df = pd.merge(project_df, task_df, on='projectID', how='left')

                # Display the result
                return result_df
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def add_proj(self, **kwargs):
        new_proj = Project(**kwargs)
        print(f"Project '{new_proj.projectID}' added.")
        file_handler.write_to_json(new_proj, 'project.json', 'a')  # Write to JSON file
        return new_proj

    def add_task(self, **kwargs):
        new_task = Task(**kwargs)
        projects_from_json = file_handler.read_from_json('project.json')
        project_ids = [project['projectID'] for project in projects_from_json]
        
        if new_task.projectID in project_ids:
            file_handler.write_to_json(new_task, 'task.json', 'a')  # Write to JSON file
            print(f"Task '{new_task.taskID}' added.")
            return new_task
        else:
            print(f"Project {new_task.projectID} does not exist.")
            return None
    
    def modify_item(self):
        modify_type = input("Enter 'project' or 'task' ID to modify: ").upper()
        
        while True:
            # Read data from JSON files
            projects_from_json = file_handler.read_from_json('project.json')
            tasks_from_json = file_handler.read_from_json('task.json')

            # Identify the list and ID based on user input
            if modify_type[0] == 'P':
                items_list = projects_from_json
                item_ids = [project['projectID'] for project in projects_from_json]
            elif modify_type[0] == 'T':
                items_list = tasks_from_json
                item_ids = [task['taskID'] for task in tasks_from_json]
            else:
                print("Invalid input. Please enter correct 'project' or 'task' IDs.")
                break  # Exit the loop if the input is invalid

            # Check if the specified ID exists
            if modify_type not in item_ids:
                print(f"{modify_type} not found.")
                break  # Exit the loop if the ID is not found

            # Find the dictionary with the specified ID
            item_index = item_ids.index(modify_type)
            item = items_list[item_index]

            # Display current attributes
            clear_output(wait=True)
            print(f"Current attributes of {modify_type}:")
            for key, value in item.items():
                print(f"{key}: {value}")

            # Get the attribute to modify
            attribute = input("Enter the attribute to modify: ")

            # Check if the attribute exists
            if attribute not in item:
                print(f"Attribute '{attribute}' does not exist in {modify_type}.")
            else:
                # Get the new value for the attribute
                new_value = input(f"Enter new value for '{attribute}': ")

                # Update the attribute in the dictionary
                item[attribute] = new_value

                # Write the modified list of dictionaries back to the JSON file
                if modify_type[0] == 'P':
                    file_handler.delete_all_objects('project.json')
                    for project_item in projects_from_json:
                        file_handler.write_to_json_dict(project_item, 'project.json')
                elif modify_type[0] == 'T':
                    file_handler.delete_all_objects('task.json')
                    for task_item in tasks_from_json:
                        file_handler.write_to_json_dict(task_item, 'task.json')

                print(f"Attribute '{attribute}' updated for '{modify_type}'.")

            if input(f"Do you want to continue updating {modify_type} (Y/N)?").upper() != 'Y':
                break  # Exit the loop if the user does not want to continue
    
    def delete_item(self):
        projects_from_json = file_handler.read_from_json('project.json')
        project_ids = [project['projectID'] for project in projects_from_json]
        tasks_from_json = file_handler.read_from_json('task.json')
        task_ids = [task['taskID'] for task in tasks_from_json]
        
        delete_type = input("Enter 'project' or 'task' ID to delete: ").upper()

        confirm_delete = input(f"Are you sure you want to delete {delete_type} Y/N? ").upper()
        
        if confirm_delete != "Y":
            return None
        if delete_type[0] == 'P':
            if delete_type in project_ids:
                project_list = [project for project in projects_from_json if project['projectID'] != delete_type]
                file_handler.delete_all_objects('project.json')
                for project_item in project_list:
                    file_handler.write_to_json_dict(project_item, 'project.json')
                print(f"Project '{delete_type}' deleted.")
                return delete_type
            else:
                print(f"Project '{delete_type}' not found.")
                return None
        elif delete_type[0] == 'T':
            if delete_type in task_ids:
                task_list = [task for task in tasks_from_json if task['taskID'] != delete_type]
                file_handler.delete_all_objects('task.json')
                for task_item in task_list:
                    file_handler.write_to_json_dict(task_item, 'task.json')
                print(f"Task '{delete_type}' deleted.")
                return delete_type
            else:
                print(f"Task '{delete_type}' not found.")
                return None
        else:
            print("Invalid input. Please enter 'project' or 'task'.")
            return None

class Project(Operations):
    def __init__(self, Name, Priority, Duration, Comments, assignedTo, startDate, Deadline, Owner):
        project_id = self.get_next_project_id()
        self.projectID = f'P{project_id:04}'
        self.projectName = Name
        self.projectPriority = Priority
        self.projectDuration = Duration
        self.projectComments = Comments
        self.assignedToProjectTL = assignedTo
        self.projectStartDate = startDate 
        self.projectDeadline = Deadline
        self.projectOwner = Owner
        self.projectStatus = 'Not Started'

    def get_next_project_id(self):
        last_project_id = 0
        try:
            projects_from_json = file_handler.read_from_json('project.json')
        except:
            pass
        else:
            project_ids = [project['projectID'] for project in projects_from_json]
            last_inserted_project_id = max(project_ids, key=lambda x: int(x[1:]))
            last_project_id = int(last_inserted_project_id[1:])
        finally:
            last_project_id += 1
            return last_project_id

class Task(Project):
    def __init__(self, projectID, Name, Priority, Duration, Comments, assignedTo, startDate, Deadline):
        self.projectID = projectID
        task_id = self.get_next_task_id()
        self.taskID = f'T{task_id:04}'
        self.taskName = Name
        self.taskPriority = Priority
        self.taskDuration = Duration
        self.taskComments = Comments
        self.assignedToTask = assignedTo
        self.taskStartDate = startDate
        self.taskDeadline = Deadline
        self.taskStatus = 'Not Started'

    def get_next_task_id(self):
            last_task_id = 0
            try:
                tasks_from_json = file_handler.read_from_json('task.json')
            except:
                pass
            else:
                task_ids = [task['taskID'] for task in tasks_from_json]
                last_inserted_task_id = max(task_ids, key=lambda x: int(x[1:]))
                last_task_id = int(last_inserted_task_id[1:])
            finally:
                last_task_id += 1
                return last_task_id
    
    def get_next_task_id(self):
        last_task_id = 0
        try:
            tasks_from_json = file_handler.read_from_json('task.json')
        except:
            pass
        else:
            task_ids = [task['taskID'] for task in tasks_from_json]
            last_inserted_task_id = max(task_ids, key=lambda x: int(x[1:]))
            last_task_id = int(last_inserted_task_id[1:])
        finally:
            last_task_id += 1
            return last_task_id
