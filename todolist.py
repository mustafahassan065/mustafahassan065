import os

def Show_task(tasks):
   if not tasks:
      print("No Tasks found")
   else:
      for i, task in enumerate(tasks , i):
         print(f"{i}- {task} ")

def add_task(tasks , new_task):
            tasks.append(new_task)
            print("Task is added Successfully")

def update_task(tasks,index,update):
    if 1<=index<=len(tasks):
        tasks[index-1] = update
        print("Task is updated successfully")
    else:
        print("Invalid try")    

def delete_task(tasks , index):
     if 1 <= index <= len(tasks):
        tasks[index-1] = delete_task
        print("Task is deleted successfully")
     else:
         print("Invalid try")






def save_tasks(file_way , tasks):
      with open(file_way, 'r') as f:
         for task in tasks:
            f.write(f"{task}\n")

def load_tasks_from_file(file_way):
   task = []
   if os.path.exists(file_way):
      with open(file_way , 'r') as f:
         task = f.read().splitlines()
         return task




def main():
    file_way = "todolist.txt"
    tasks = load_tasks_from_file(file_way)

    while True:
      print("This is to do list project")
      print("1. Show Tasks")
      print("2. Add Tasks")
      print("3. Update Tasks")
      print("4. Delete Tasks")
      print("5. Save and Exist")

      choice = int(input("Select any option"))

      if choice == 1:
          Show_task(tasks)
      elif choice == 2:
        new_task = input("Enter the task to add: ")
        add_task(tasks , new_task)
      elif choice == 3:
        index = int(input("Select the task which you want to update: "))
        update = input("Enter the updated task: ")
        update_task(tasks,index,update)
      elif choice == 4:
        index = int(input("Enter the task you want to delete"))
        delete_task(tasks, index)
      elif choice == 5:
        save_tasks(file_way,tasks)
        print("Tasks saved.Existing......!")
        break
      else:
         print("Invalid choice")


if __name__ =="__main__":

 main()