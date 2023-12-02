import os
os.chdir('/Users/nats/Desktop/Project-Group-13')
from projecttracker.utils import file_handler

import plotly.express as px
import datetime

def gantt_chart():
    data = []
    projects_from_json = file_handler.read_from_json('project.json')
    project_list = [project for project in projects_from_json]
    for x in project_list:
            data.append(dict(Project=x["projectName"], Start=x["projectStartDate"], Finish=x["projectDeadline"], Priority=x["projectPriority"]))

    # Create a Gantt chart
    fig = px.timeline(data, x_start="Start", x_end="Finish", y="Project", hover_data={"Priority": True})

    # Current date
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Add a vertical line for the current date
    fig.update_layout(shapes=[
        dict(
            type="line",
            x0=current_date,
            x1=current_date,
            y0=0,
            y1=1,
            yref="paper",
            line=dict(color="black", width=2),
        )
    ])

    # Show the Gantt chart
    fig.show()

    project_id = input("Enter Project ID: ")
    data = []
    tasks_from_json = file_handler.read_from_json('task.json')
    task_list = [task for task in tasks_from_json if task['projectID'] == project_id_input]

    for x in task_list:
        data.append(dict(Task=x['taskName'], Start=x['taskStartDate'], Finish=x['taskDeadline'], Priority=x['taskPriority']))

    # Create a Gantt chart for each Project holding different Tasks
    fig = px.timeline(data, x_start="Start", x_end="Finish", y="Task", hover_data={"Priority": True}, labels={"Task": f"Project: {project_id_input}"})

    # Show the Gantt chart for each Project holding different Tasks
    fig.show()

def pie_chart():
    # Create a Pie chart for the Project holding different Tasks
    fig = px.pie(data, names='Status', title='Task Status Distribution',
        color_discrete_map={'Completed': 'lightcoral', 'In Progress': 'blue', 'Not Started': 'green'})

# Show the Pie Chart
fig.show()  