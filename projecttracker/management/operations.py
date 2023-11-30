class Operations:
    def __init__(self):
        self.projects = {}
        self.tasks = {}
        
    #def view
        
    def add_proj(self, **kwargs): #add exceptional handling if proj exists
        new_proj = Project(**kwargs)
        self.projects[new_proj.projectID] = new_proj
        print(f"Project '{new_proj.projectID}' added.")
        return new_proj
        
    def add_task(self, **kwargs):
        new_task = Task(**kwargs)
        self.tasks[new_task.taskID] = new_task
        print(f"Task '{new_task.taskID}' added.")
        return new_task
    
    def delete_item(self):
        delete_type = input("Enter 'project' or 'task' ID to delete: ").upper()
        
        if delete_type[0] == 'P':
            if delete_type in self.projects:
                del_proj = self.projects.pop(delete_type)
                print(f"Project '{delete_type}' deleted.")
                return del_proj
            else:
                print(f"Project '{delete_type}' not found.")
                return None
        elif delete_type[0] == 'T':
            if delete_type in self.tasks:
                del_task = self.tasks.pop(delete_type)
                print(f"Task '{delete_type}' deleted.")
                return del_task
            else:
                print(f"Task '{delete_type}' not found.")
                return None
        else:
            print("Invalid input. Please enter 'project' or 'task'.")
            return None

class Project(Operations):
    project_counter = 0
    def __init__(self, Name, Priority, Duration, Comments, assignedTo, startDate, Deadline, Owner):
        Project.project_counter += 1
        self.projectID = f'P{Project.project_counter:04}'
        self.projectName = Name
        self.projectPriority = Priority
        self.projectDuration = Duration
        self.projectComments = Comments
        self.assignedToProjectTL = assignedTo
        self.projectStartDate = startDate 
        self.projectDeadline = Deadline
        self.projectOwner = Owner
        self.IsProjectCompleted = 'N'


class Task(Project):
    task_counter = 0
    def __init__(self, projectID, Name, Priority, Duration, Comments, assignedTo, startDate, Deadline):
        self.projectID = projectID
        Task.task_counter += 1
        self.taskID = f'T{Task.task_counter:04}'
        self.taskName = Name
        self.taskPriority = Priority
        self.taskDuration = Duration
        self.taskComments = Comments
        self.assignedToTask = assignedTo
        self.taskStartDate = startDate
        self.taskDeadline = Deadline
        self.IsTaskCompleted = 'N'