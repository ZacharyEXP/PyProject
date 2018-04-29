from tkinter import *
from user import *
from file_handler import *
from log_in import *
from glob import *
from os import *

class Main_GUI:
    def __init__(self, user, file):
        #Sets and initializes default variables
        self.__user = user
        self.__file = file
        self.__file_h = FileHandler(self.__file)
        self.__file_h.openFile()
        self.__check_state = []
        self.__task_check = []
        self.__count = 0
        self.__window = Tk()
        self.__window.title("Company Name Main Page")
        self.__window.geometry("900x900")
        self.__main_frame = Frame(self.__window, width = 500, height = 200)

        self.__title = Label(self.__window, text = "Welcome back " + \
                             str(self.__user.get_name()),\
                             font = ("Arial Bold", 25))
        self.__title.grid(column = 0, row = 0, pady = 10)

        self.__task_label = Label(self.__window, text = "Task List:")
        self.__task_label.grid(column = 0, row = 1, pady = 10)

        #Creates list of check buttons and disables them if they're marked for completion
        for c in range(len(self.__user.get_tasks())):
            self.__check_state.append(BooleanVar())
            self.__check_state[c].set(0)
            self.__task_text = (str(self.__user.get_task(c).get_objective()) \
                                    + ' | ' + str(self.__user.get_task(c).get_urgency()) \
                                    + ' | ' + str(self.__user.get_task(c).get_date_due()) \
                                    + ' | ' + str(self.__user.get_task(c).get_status()))
            if(str(self.__user.get_task(c).get_reported()).strip() == "True"):
                self.__task_text += ' |  Reported Completed'
            elif(str(self.__user.get_task(c).get_reported()).strip() == "False"):
                self.__task_text += ' |  Not Reported Completed'

            self.__task_check.append(Checkbutton(self.__window, text = self.__task_text, \
                                               var = self.__check_state[c]))
            
            if(self.__user.get_task(c).get_reported() == "True"):
                self.__task_check[c].config(state = DISABLED)
            self.__task_check[c].grid(column = 0, row = c + 2, pady = 5)
            self.range = c + 3

        #Initializes buttons based on user type
        if(self.__user.get_occ().strip() == 'Associate' or self.__user.get_occ().strip() == 'Manager' or \
           self.__user.get_occ().strip() == 'Owner'):
            self.__report_button = Button(self.__main_frame, text = "Report Completed Tasks", \
                                     command = self.report_completed, width = 35)
            self.__report_button.grid(column = self.__count, row = 0, padx = 2)
            self.__count += 1

            self.__quit_button = Button(self.__main_frame, text = "Save & Quit", \
                                    command = self.quit_clicked, width = 35)
            self.__quit_button.grid(column = self.__count, row = 0, padx = 2)
            self.__count += 1

        if(self.__user.get_occ().strip() == 'Manager' or self.__user.get_occ().strip() == 'Owner'):
            self.__assign_button = Button(self.__main_frame, text = "Assign Task to Employee", \
                                     command = self.assign_task, width = 35)
            self.__assign_button.grid(column = self.__count, row = 0, padx = 2)
            self.__count += 1

            self.__view_button = Button(self.__main_frame, text = "View Team Task Progress", \
                                     command = self.task_progress, width = 35)
            self.__view_button.grid(column = self.__count, row = 0, padx = 2)
            self.__count = 0

        if(self.__user.get_occ().strip() == 'Owner'):
            self.__remove_button = Button(self.__main_frame, text = "Remove completed tasks", \
                                     command = self.remove_tasks, width = 35)
            self.__remove_button.grid(column = self.__count, row = 1, padx = 2)
            self.__count += 1
            
            self.__manage_button = Button(self.__main_frame, text = "Change Team Member", \
                                     command = self.manage_teams, width = 35)
            self.__manage_button.grid(column = self.__count, row = 1, padx = 2)
            self.__count += 1

            self.__add_button = Button(self.__main_frame, text = "Add Employee", \
                                     command = self.add_employee, width = 35)
            self.__add_button.grid(column = self.__count, row = 1, padx = 2)
            self.__count += 1
            
            self.__fire_button = Button(self.__main_frame, text = "Remove Employee", \
                                     command = self.fire_employee, width = 35)
            self.__fire_button.grid(column = self.__count, row = 1, padx = 2)
            self.__count += 1

        self.__main_frame.grid(column = 0, row = self.__count + 1, pady = 50)
        
        self.__window.mainloop()

    #Saves and quits
    def quit_clicked(self):
        self.__file_h.saveFile(self.__user)
        self.__window.destroy()

    #Marks any checked tasks for completion and updates the buttons
    def report_completed(self):
        for x in range(len(self.__task_check)):
            if(self.__check_state[x].get() == 1):
                self.__user.get_task(x).set_reported("True")
                self.__report_task_text = (str(self.__user.get_task(x).get_objective()) \
                                    + ' | ' + str(self.__user.get_task(x).get_urgency()) \
                                    + ' | ' + str(self.__user.get_task(x).get_date_due()) \
                                    + ' | ' + str(self.__user.get_task(x).get_status()))
                if(str(self.__user.get_task(x).get_reported()).strip() == "True"):
                    self.__report_task_text += ' |  Reported Completed'
                elif(str(self.__user.get_task(x).get_reported()).strip() == "False"):
                    self.__report_task_text += ' |  Not Reported Completed'
                self.__task_check[x].config(state = DISABLED, text = self.__report_task_text)

    #Opens new window and allows input to create a new task for a user
    def assign_task(self):
        self.__assign_window = Tk()
        self.__assign_window.title("Company Name Task Assignment")
        self.__assign_window.geometry("800x300")

        self.__assign_title = Label(self.__assign_window, text = "Task Assignment",\
                             font = ("Arial Bold", 25))
        self.__assign_title.grid(column = 2, row = 0)

        self.__assign_id_entry = Entry(self.__assign_window, width = 40)
        self.__assign_id_entry.grid(column = 2, row = 1)
        self.__assign_id_label = Label(self.__assign_window, text = "Enter ID of Employee to assign task to:")
        self.__assign_id_label.grid(column = 1, row = 1)

        self.__assign_task_entry = Entry(self.__assign_window, width = 60)
        self.__assign_task_entry.grid(column = 2, row = 2)
        self.__assign_task_label = Label(self.__assign_window, text = "Enter task to be completed:")
        self.__assign_task_label.grid(column = 1, row = 2)

        self.__assign_date_entry = Entry(self.__assign_window, width = 20)
        self.__assign_date_entry.grid(column = 2, row = 3)
        self.__assign_date_label = Label(self.__assign_window, text = "Enter task due date:")
        self.__assign_date_label.grid(column = 1, row = 3)

        self.__rb_var = IntVar()

        self.__assign_urgency_label = Label(self.__assign_window, text = "Select task urgency:")
        self.__assign_urgency_label.grid(column = 1, row = 4)
        
        self.__assign_urgency_rb1 = Radiobutton\
                   (self.__assign_window, \
                     text = 'Major', \
                    variable = self.__rb_var,  value = 1, command = self.assign_var1)
        self.__assign_urgency_rb1.grid(column = 2, row = 4)
        
        self.__assign_urgency_rb2 = Radiobutton\
                   (self.__assign_window, \
                     text = 'Minor', \
                    variable = self.__rb_var,  value = 2, command = self.assign_var2)
        self.__assign_urgency_rb2.grid(column = 3, row = 4)

        self.__assign_urgency_rb1.invoke()

        self.__assign_fail_label = Label(self.__assign_window, text = "")
        self.__assign_fail_label.grid(column = 2, row = 5)
        self.__assign_quit_button = Button(self.__assign_window, text = "Submit", \
                                    command = self.assign_quit_clicked)
        self.__assign_quit_button.grid(column = 2, row = 6)

    #Part of assign_task, sets rb values
    def assign_var1(self):
        self.__rb_var.set(1)

    def assign_var2(self):
        self.__rb_var.set(2)

    #Tries to save task, quits if successful, error message if not
    def assign_quit_clicked(self):
        if(self.__rb_var.get() == 1):
            self.__assign_urgency = 'Major'
        if(self.__rb_var.get() == 2):
            self.__assign_urgency = 'Minor'
        try:
            self.__assign_file = FileHandler(str(self.__user.get_org()).strip() + '//' + self.__assign_id_entry.get().strip() + '.txt')
            self.__assign_user = self.__assign_file.openFile()
            if((str(self.__assign_user.get_occ()).strip() == 'Manager' or str(self.__assign_user.get_occ()).strip() == 'Owner') and str(self.__user.get_occ()).strip() == 'Manager'):
                self.__assign_fail_text = "Invalid Clearance! Try again."
                self.__assign_fail_label.configure(text = self.__assign_fail_text)
            else:
                self.__assign_task = Task(str(self.__assign_date_entry.get()), 'UNFINISHED', str(self.__assign_task_entry.get()), self.__assign_urgency, 'False')
                self.__assign_user.add_tasks(self.__assign_task)
                self.__assign_file.saveFile(self.__assign_user)
                self.__assign_window.destroy()
        except Exception as e:
            print(str(e))
            self.__assign_fail_text = "Wrong ID! Please try again."
            self.__assign_fail_label.configure(text = self.__assign_fail_text)

    #Lists tasks of everyone in a team
    def task_progress(self):
        self.__progress_files = []
        self.__progress_users = []
        self.__progress_tasks = []
        self.__path = str(self.__user.get_org()).strip() + '//'

        self.__progress_window = Tk()
        self.__progress_window.title("Company Name Task Progress List")

        self.__progress_title = Label(self.__progress_window, text = "Task List",\
                             font = ("Arial Bold", 25))
        self.__progress_title.grid(column = 2, row = 0)
        
        count = 0
        count2 = 0
        for file in glob(path.join(self.__path, '*.txt')):
            self.__progress_files.append(FileHandler(file))
            self.__progress_users.append(self.__progress_files[count].openFile())
            count += 1
        for x in range(len(self.__progress_users)):
            for y in range(len(self.__progress_users[x].get_tasks())):
                self.__progress_task_text = (str(self.__progress_users[x].get_name()).strip() \
                                + '(' + str(self.__progress_users[x].get_team()).strip() + ')' \
                                + ': ' + str(self.__progress_users[x].get_task(y).get_objective()) \
                                + ' | ' + str(self.__progress_users[x].get_task(y).get_urgency()) \
                                + ' | ' + str(self.__progress_users[x].get_task(y).get_date_due()) \
                                + ' | ' + str(self.__progress_users[x].get_task(y).get_status()))
                if(str(self.__progress_users[x].get_task(y).get_reported()).strip() == "True"):
                    self.__progress_task_text += ' |  Reported Completed'
                elif(str(self.__progress_users[x].get_task(y).get_reported()).strip() == "False"):
                    self.__progress_task_text += ' |  Not Reported Completed'
                self.__progress_tasks.append(Label(self.__progress_window, text = self.__progress_task_text))
                self.__progress_tasks[count2].grid(column = x, row = y + 1)
                count2 += 1

        size = 300 * count
        self.__progress_window.geometry(str(size) + 'x300')
                    
    #Creates a new window, accepts input to change a users team
    def manage_teams(self):
        self.__manage_window = Tk()
        self.__manage_window.title("Company Name Team Management")
        self.__manage_window.geometry("800x300")

        self.__manage_id_entry = Entry(self.__manage_window, width = 40)
        self.__manage_id_entry.grid(column = 2, row = 3)
        self.__manage_id_label = Label(self.__manage_window, text = "Enter ID of Person whose team is being changed:")
        self.__manage_id_label.grid(column = 1, row = 3)

        self.__manage_team_entry = Entry(self.__manage_window, width = 40)
        self.__manage_team_entry.grid(column = 2, row = 4)
        self.__manage_team_label = Label(self.__manage_window, text = "Enter person's new team")
        self.__manage_team_label.grid(column = 1, row = 4)

        self.__manage_fail_label = Label(self.__manage_window, text = "")
        self.__manage_fail_label.grid(column = 2, row = 5)
        self.__manage_quit_button = Button(self.__manage_window, text = "Submit", \
                                    command = self.manage_quit_clicked)
        self.__manage_quit_button.grid(column = 2, row = 6)

    #Saves the new team and closes window
    def manage_quit_clicked(self):
        try:
            self.__manage_file = FileHandler(str(self.__user.get_org()).strip() + '//' + str(self.__manage_id_entry.get()).strip() + '.txt')
            self.__manage_user = self.__manage_file.openFile()
            self.__manage_user.set_team(str(self.__manage_team_entry.get()).strip())
            self.__manage_file.saveFile(self.__manage_user)
            self.__manage_window.destroy()
        except Exception as e:
            print(str(e))
            self.__manage_fail_text = "Wrong ID! Please try again."
            self.__manage_fail_label.configure(text = self.__manage_fail_text)

    #Opens new window, takes input for employee ID
    def remove_tasks(self):
        self.__remove_window = Tk()
        self.__remove_check_state = []
        self.__remove_task_check = []
        self.__remove_window.title("Company Name Task Removal")
        self.__remove_window.geometry("800x300")

        self.__remove_id_entry = Entry(self.__remove_window, width = 40)
        self.__remove_id_entry.grid(column = 2, row = 3)
        self.__remove_id_label = Label(self.__remove_window, text = "Enter ID of Person whose tasks you are removing:")
        self.__remove_id_label.grid(column = 1, row = 3)

        self.__remove_submit_label = Label(self.__remove_window, text = "")
        self.__remove_submit_label.grid(column = 2, row = 5)
        self.__remove_submit_button = Button(self.__remove_window, text = "Submit", \
                                    command = self.remove_submit_clicked)
        self.__remove_submit_button.grid(column = 2, row = 6)

    #Opens another window and closes the previous, creates list of buttons, buttons don't seem to work now however
    def remove_submit_clicked(self):
        self.__remove_task_window = Tk()
        self.__remove_task_window.title("Company Name Task Removal")
        self.__remove_task_window.geometry("800x300")
        try:
            self.__remove_file = FileHandler(str(self.__user.get_org()).strip() + '//' + self.__remove_id_entry.get().strip() + '.txt')
            self.__remove_user = self.__remove_file.openFile()
            self.__remove_window.destroy()
        except Exception as e:
            print(str(e))
            self.__remove_submit_text = 'Invalid ID! Please try again.'
            self.__remove_submit_button.configure(text = self.__remove_submit_text)
            self.__remove_task_window.destroy()

        for c in range(len(self.__remove_user.get_tasks())):
            #self.__remove_check_state.append(IntVar())
            #self.__remove_check_state.append(c)
            self.__remove_rb_val = IntVar()
            self.__remove_rb_val.set(0)
            #self.__remove_check_state[c].set(0)
            self.__remove_task_text = (str(self.__remove_user.get_task(c).get_objective()) \
                                    + ' | ' + str(self.__remove_user.get_task(c).get_urgency()) \
                                    + ' | ' + str(self.__remove_user.get_task(c).get_date_due()) \
                                    + ' | ' + str(self.__remove_user.get_task(c).get_status()))
            if(str(self.__remove_user.get_task(c).get_reported()).strip() == "True"):
                self.__remove_task_text += ' |  Reported Completed'
            elif(str(self.__remove_user.get_task(c).get_reported()).strip() == "False"):
                self.__remove_task_text += ' |  Not Reported Completed'

            #self.__remove_task_check.append(Checkbutton(self.__remove_task_window, text = self.__remove_task_text, var = self.__remove_check_state[c], \
            #                                           command = self.checkbox))

            self.__remove_task_check.append(Radiobutton(self.__remove_task_window, text = self.__remove_task_text, var = self.__remove_rb_val, \
                                                        value = c))
            
            self.__remove_task_check[c].grid(column = 3, row = c )
            self.__remove_range = c + 1

        self.__remove_fail_label = Label(self.__remove_task_window, text = "")
        self.__remove_fail_label.grid(column = 2, row = self.__remove_range)
        self.__remove_quit_button = Button(self.__remove_task_window, text = "Submit", \
                                    command = self.remove_quit_clicked)
        self.__remove_quit_button.grid(column = 2, row = self.__remove_range + 1)

        self.__remove_task_window.mainloop()

    #Removes any tasks click and saves the file
    def remove_quit_clicked(self):
        for x in range(len(self.__remove_task_check)):
            #print(str(self.__remove_check_state[x].get()))
            #print(type(self.__remove_check_state[x].get()))
            if(self.__remove_rb_val == 1):
                print('x')
                self.__remove_user.remove_task(x)

        self.__remove_file.saveFile(self.__remove_user)
        self.__remove_task_window.destroy()

    #Creates new window and takes input for new user
    def add_employee(self):
        self.__add_window = Tk()
        self.__add_window.title("Company Name Add Employee")
        self.__add_window.geometry("800x300")

        self.__add_id_entry = Entry(self.__add_window, width = 40)
        self.__add_id_entry.grid(column = 2, row = 3)
        self.__add_id_label = Label(self.__add_window, text = "Enter ID of new Employee:")
        self.__add_id_label.grid(column = 1, row = 3)

        self.__add_pass_entry = Entry(self.__add_window, width = 40)
        self.__add_pass_entry.grid(column = 2, row = 4)
        self.__add_pass_label = Label(self.__add_window, text = "Enter person's password")
        self.__add_pass_label.grid(column = 1, row = 4)

        self.__add_name_entry = Entry(self.__add_window, width = 40)
        self.__add_name_entry.grid(column = 2, row = 5)
        self.__add_name_label = Label(self.__add_window, text = "Enter person's name")
        self.__add_name_label.grid(column = 1, row = 5)
        
        self.__add_team_entry = Entry(self.__add_window, width = 40)
        self.__add_team_entry.grid(column = 2, row = 6)
        self.__add_team_label = Label(self.__add_window, text = "Enter person's new team")
        self.__add_team_label.grid(column = 1, row = 6)
        
        #self.__add_occ_entry = Entry(self.__add_window, width = 40)
        #self.__add_occ_entry.grid(column = 2, row = 7)
        #self.__add_occ_label = Label(self.__add_window, text = "Enter person's occupation")
        #self.__add_occ_label.grid(column = 1, row = 7)

        self.__add_rb_var = IntVar()

        self.__add_occ_rb1 = Radiobutton\
                   (self.__add_window, \
                     text = 'Owner', \
                    variable = self.__add_rb_var,  value = 1)
        self.__add_occ_rb1.grid(column = 1, row = 7)
        
        self.__add_occ_rb2 = Radiobutton\
                   (self.__add_window, \
                     text = 'Manager', \
                    variable = self.__add_rb_var,  value = 2)
        self.__add_occ_rb2.grid(column = 2, row = 7)

        self.__add_occ_rb3 = Radiobutton\
                   (self.__add_window, \
                     text = 'Associate', \
                    variable = self.__add_rb_var,  value = 3)
        self.__add_occ_rb3.grid(column = 3, row = 7)

        self.__add_occ_rb1.invoke()
        self.__add_occ_entry = ''

        self.__add_fail_label = Label(self.__add_window, text = "")
        self.__add_fail_label.grid(column = 2, row = 8)
        self.__add_quit_button = Button(self.__add_window, text = "Submit", \
                                    command = self.add_quit_clicked)
        self.__add_quit_button.grid(column = 2, row = 9)

        self.__add_window.mainloop()

    #Should check for existing users then save
    def add_quit_clicked(self):
        try:
            if(self.__add_rb_var == 1):
                self.__add_occ_entry = 'Owner'
            elif(self.__add_rb_var == 2):
                self.__add_occ_entry = 'Manager'
            elif(self.__add_rb_var == 3):
                self.__add_occ_entry = 'Associate'
            self.__add_user = User(str(self.__add_id_entry.get()).strip(), str(self.__add_pass_entry.get()).strip(), str(self.__add_name_entry.get()).strip(), str(self.__add_team_entry.get()).strip(), \
                               str(self.__add_occ_entry).strip(), str(self.__user.get_org()).strip(), '0', [])
            self.__add_file = FileHandler(str(self.__user.get_org()).strip() + '//' + str(self.__add_id_entry.get()).strip() + '.txt')
            self.__add_file.saveFile(self.__add_user)
            self.__add_window.destroy()
        except Exception as e:
            print(str(e))
            self.__add_fail_text = "Something went wrong! Please try again."
            self.__add_fail_label.configure(text = self.__add_fail_text)

    #Opens new window, accepts input for user to be removed
    def fire_employee(self):
        self.__fire_window = Tk()
        self.__fire_window.title("Company Name Fire Employee")
        self.__fire_window.geometry("800x300")

        self.__fire_id_entry = Entry(self.__fire_window, width = 40)
        self.__fire_id_entry.grid(column = 2, row = 3)
        self.__fire_id_label = Label(self.__fire_window, text = "Enter ID of Employee to be removed:")
        self.__fire_id_label.grid(column = 1, row = 3)

        self.__fire_fail_label = Label(self.__fire_window, text = "")
        self.__fire_fail_label.grid(column = 2, row = 4)
        self.__fire_quit_button = Button(self.__fire_window, text = "Submit", \
                                    command = self.fire_quit_clicked)
        self.__fire_quit_button.grid(column = 2, row = 5)

    #Tries to remove user, error if failed
    def fire_quit_clicked(self):
        try:
            if(str(self.__fire_id_entry.get()).strip() == str(self.__user.get_e_id()).strip()):
                self.__fire_fail_text = "Cannot remove yourself! Please try again."
                self.__fire_fail_label.configure(text = self.__fire_fail_text)
            else:
                remove(str(self.__user.get_org()).strip() + '//' + str(self.__fire_id_entry.get()).strip() + '.txt')
                self.__fire_window.destroy()
        except Exception as e:
            print(str(e))
            self.__fire_fail_text = "User not found! Please try again."
            self.__fire_fail_label.configure(text = self.__fire_fail_text)


def main():
    log_in = Log_In_GUI()
    while(log_in.log_in_success() == False):
        var = 0

    user = log_in.get_user()
    file = log_in.get_file()
    main = Main_GUI(user, file.get_file_path())

main()
    
        
            

        
        
    
