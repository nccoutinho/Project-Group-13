from IPython.display import clear_output
import time

from projecttracker.utils import input_handler, file_handler
from projecttracker.management import operations, visualizations

def display_menu():
    
    print("\n===== Project Tracker =====", flush=True)
    print("1. View")
    print("2. Add Projects")
    print("3. Add Tasks")
    print("4. Modify")
    print("5. Delete")
    print("6. Open Visualization window")
    print("7. Download to csv")
    print("8. Exit", flush=True)

def viz_menu():
    print("\n===== Visualization Menu =====", flush=True)
    print("1. Project Schedule Overview")
    print("2. Task Status Distribution by Project")
    print("3. Project Priority vs Project Duration")
    print("4. Total Number of Tasks for each Project")
    print("5. Exit", flush=True)

def viz_define():
    
    while True:
        clear_output(wait=True)
        viz_menu()
        choice = input_handler.get_user_choice()
        match choice:
            case 1:
                visualizations.gantt_chart()
                input_handler.any_key_continue()
            case 2:
                visualizations.pie_chart()
                input_handler.any_key_continue()
            case 3:
                visualizations.scatter_plot()
                input_handler.any_key_continue()
            case 4:
                visualizations.bar_chart()
                input_handler.any_key_continue()
            case 5:
                clear_output(wait=True)
                print("Exiting from the Visualization window.")
                return
            case _:
                print("Invalid choice. Please enter a valid option.")
                

def startup():
    op = operations.Operations()

    while True:
        display_menu()
        choice = input_handler.get_user_choice()

        match choice:
            case 1:
                view_projects(op)

            case 2:
                add_project(op)

            case 3:
                add_task(op)

            case 4:
                op.modify_item()

            case 5:
                op.delete_item()

            case 6:
                viz_define()

            case 7:
                df = op.view()
                file_path = input_handler.get_file_path()
                file_handler.download_csv(df, file_path)
                print(f'The file has been downloaded in {file_path}')

            case 8:
                clear_output(wait=True)
                print("Exiting the Project Tracker application. Goodbye!")
                return

            case _:
                
                print("Invalid choice. Please enter a valid option.")
            
        time.sleep(2)
        clear_output(wait=True)

def view_projects(op):
    df = op.view()
    if df is not None and not df.empty:
        print(df.head(10))
    input_handler.any_key_continue()

def add_project(op):
    # Get project details
    name = input_handler.get_project_input()
    priority = input_handler.get_priority_input()
    duration = input_handler.get_duration_input()
    comments = input_handler.get_comments_input()
    assigned_to = input_handler.get_assigned_input()
    start_date = input_handler.get_start_date_input()
    deadline = input_handler.get_deadline_input()
    owner = input_handler.get_owner_input()

    # Add project
    op.add_proj(Name=name, Priority=priority, Duration=duration, Comments=comments,
                assignedTo=assigned_to, startDate=start_date, Deadline=deadline, Owner=owner)

def add_task(op):
    # Get task details
    name = input_handler.get_task_input()
    project_id = input_handler.get_projectID_input()
    priority = input_handler.get_priority_input()
    duration = input_handler.get_duration_input()
    comments = input_handler.get_comments_input()
    assigned_to = input_handler.get_assigned_input()
    start_date = input_handler.get_start_date_input()
    deadline = input_handler.get_deadline_input()

    # Add task
    op.add_task(projectID=project_id, Name=name, Priority=priority, Duration=duration, Comments=comments,
                assignedTo=assigned_to, startDate=start_date, Deadline=deadline)