from project_1.task import Task

class Section:
    tasks = []

    def __init__(self, name):
        self.name = name

    def add_task(self, new_task: Task):
        if new_task in Section.tasks:
            return f'Task is already in the section {self.name}'
        Section.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        for task in Section.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        counter = 0
        for task in Section.tasks:
            if task.completed:
                Section.tasks.remove(task)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        a = []
        a.append(f'Section {self.name}:')
        for i in Section.tasks:
            a.append(i.details())
        return "\n".join(a)
