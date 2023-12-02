from projecttracker.utils import file_handler
from projecttracker.utils import input_handler
import pandas as pd

class Operations:
    def __init__(self):
        self.projects = {}
        self.tasks = {}
        
    def view(self):
        # Read projects and tasks from JSON files
        projects_from_json = file_handler.read_from_json('project.json')
        tasks_from_json = file_handler.read_from_json('task.json')
        
        # Convert data to pandas DataFrame
        task_df = pd.DataFrame(tasks_from_json)
        project_df = pd.DataFrame(projects_from_json)

        # Merge the two DataFrames on 'projectID'
        result_df = pd.merge(project_df, task_df, on='projectID', how='left')

        # Display the result
        result_df.head(10)
        
    def add_proj(self, **kwargs):
        new_proj = Project(**kwargs)
        #self.projects[new_proj.projectID] = new_proj
        print(f"Project '{new_proj.projectID}' added.")
        file_handler.write_to_json(new_proj, 'project.json', 'a')  # Write to JSON file
        return new_proj

    def add_task(self, **kwargs):
        new_task = Task(**kwargs)
        #self.tasks[new_task.taskID] = new_task
        print(f"Task '{new_task.taskID}' added.")
        file_handler.write_to_json(new_task, 'task.json', 'a')  # Write to JSON file
        return new_task
    
    def modify_item(self):
        
        modify_type = input("Enter 'project' or 'task' ID to modify: ").upper()
        
        while True:

            if modify_type[0] == 'P' and modify_type in self.projects:
                project = self.projects[modify_type]
                print(f"Current attributes of Project '{modify_type}':")
                for key, value in project.__dict__.items():
                     print(f"{key}: {value}")

                attribute = input("Enter the attribute to modify: ")
                if hasattr(project, attribute):
                    new_value = input(f"Enter new value for '{attribute}': ")
                    setattr(project, attribute, new_value)
                    print(f"Attribute '{attribute}' updated for Project '{modify_type}'.")
                else:
                    print(f"Attribute '{attribute}' does not exist in the project.")
            elif modify_type[0] == 'T' and modify_type in self.tasks:
                task = self.tasks[modify_type]
                print(f"Current attributes of Task '{modify_type}':")
                for key, value in task.__dict__.items():
                    print(f"{key}: {value}")

                attribute = input("Enter the attribute to modify: ")
                if hasattr(task, attribute):
                    new_value = input(f"Enter new value for '{attribute}': ")
                    setattr(task, attribute, new_value)
                    print(f"Attribute '{attribute}' updated for Task '{modify_type}'.")
                else:
                    print(f"Attribute '{attribute}' does not exist in the task.")
            else:
                print("Item not found or invalid item type.")
            
            if input(f"Do you want to continue updating {modify_type} (Y/N)?") == 'N':
                break
    
    def delete_item(self):
        projects_from_json = file_handler.read_from_json('project.json')
        project_ids = [project['projectID'] for project in projects_from_json]
        tasks_from_json = file_handler.read_from_json('task.json')
        task_ids = [task['taskID'] for task in tasks_from_json]
        
        delete_type = input("Enter 'project' or 'task' ID to delete: ").upper()
        
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
        self.IsProjectCompleted = 'N'
    
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
        self.IsTaskCompleted = 'N'
    
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