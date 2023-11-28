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
    