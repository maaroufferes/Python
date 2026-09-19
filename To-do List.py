import flet as ft
priority_order={"Must":0, "Should":1, "Could":2}
color={"Must":ft.Colors.RED, "Should":ft.Colors.YELLOW, "Could":ft.Colors.GREEN}

def main(page: ft.Page):
    page.title="To-do List"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    new_task=ft.TextField(hint_text="Task",expand=True)
    priority_dropdown=ft.Dropdown(width=120, value="Should", options=[ft.dropdown.Option(p) for p in priority_order],)

    tasks_view=ft.Column()
    tasks_data=[]

    def sort_tasks():
        tasks_data.sort(key=lambda item:priority_order[item[0]])
        tasks_view.controls=[row for _, row in tasks_data]
        page.update()

    def delelte_task(entry):
        tasks_data.remove(entry)
        sort_tasks()

    def add_clicked(e):
        if new_task.value.strip()=="":
            return

        priority=priority_dropdown.value
        label=ft.Text(f"[{priority}] {new_task.value}", color=color[priority])
        delete_button=ft.IconButton(icon=ft.Icons.DELETE)
        task_row=ft.Row(controls=[label, delete_button], expand=True)

        entry=(priority, task_row)
        delete_button.on_click=lambda e, entry=entry: delelte_task(entry)
        tasks_data.append(entry)
        new_task.value=""
        sort_tasks()
    page.add(ft.Text("My Tasks", size=24, weight=ft.FontWeight.BOLD), ft.Row(controls=[new_task, priority_dropdown, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)]), tasks_view)

ft.run(main)