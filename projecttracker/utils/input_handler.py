from datetime import datetime

def get_user_choice():
    try:
        choice = int(input('Enter your choice:'))
        return choice
    except ValueError:
        print('Invalid input')

def get_project_input():
    return input('Enter Project Name:')
    
def get_task_input():
    return input('Enter Task Name:')

def get_projectID_input():
    return input('Enter Project ID:')

def get_priority_input():
    return input('Enter priority:')

def get_duration_input():
    return input('Enter duration:')

def get_comments_input():
    return input('Enter comments:')
    
def get_assigned_input():
    return input('Enter name of the person it is assigned to:')

def get_start_date_input():
    return input('Enter start date:')
    
def get_deadline_input():
    return input('Enter deadline:')
    
def get_owner_input():
    return input('Enter name of the owner:')
    
def get_project_task_id():
    return input('Enter project or task ID:').upper()

def any_key_continue():
    return input("Press any key to continue.")

def get_file_path():
    return input('Enter the file path you want to download the file to:')