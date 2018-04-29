from tkinter import *
from tkinter.ttk import *
from user import *
from file_handler import *
from os import *
 
class Log_In_GUI:  
    def __init__(self):
        self.__log_in_succ = False
        self.__window = Tk()
        self.__fail_text = ""
        self.__window.title("Company Name Log-In")
        self.__window.geometry("750x200")

        self.__title = Label(self.__window, text = "Welcome to Company Name",\
                             font = ("Arial Bold", 25))
        self.__title.grid(column = 2, row = 1)

        self.__org_entry = Entry(self.__window, width = 40)
        self.__org_entry.grid(column = 2, row = 2)
        self.__org_entry.focus()
        self.__org_label = Label(self.__window, text = "Organization ID:")
        self.__org_label.grid(column = 1, row = 2)

        self.__id_entry = Entry(self.__window, width = 40)
        self.__id_entry.grid(column = 2, row = 3)
        self.__id_label = Label(self.__window, text = "Personal ID:")
        self.__id_label.grid(column = 1, row = 3)
        
        self.__pass_entry = Entry(self.__window, width = 40)
        self.__pass_entry.grid(column = 2, row = 4)
        self.__pass_label = Label(self.__window, text = "Password:")
        self.__pass_label.grid(column = 1, row = 4)

        self.__fail_label = Label(self.__window, text = "")
        self.__fail_label.grid(column = 2, row = 5)

        self.__enter_button = Button(self.__window, text = "Log-In", \
                                     command = self.log_in)
        self.__enter_button.grid(column = 2, row = 6)

        self.__quit_button = Button(self.__window, text = "Quit", \
                                    command = self.quit_clicked)
        self.__quit_button.grid(column = 2, row = 7)

        self.__new_button = Button(self.__window, text = "New Organization", \
                                    command = self.add_org)
        self.__new_button.grid(column = 3, row = 7)

        self.__window.mainloop()

    def quit_clicked(self):
        self.__window.destroy()

    def log_in(self):
        #For easier testing
        self.__org = str(self.__org_entry.get()).strip()
        self.__id = str(self.__id_entry.get()).strip()
        self.__pass = str(self.__pass_entry.get()).strip()
        #self.__org = '2255'
        #self.__id = '100123'
        #self.__pass = 'password'
        try:
            self.__file = FileHandler(self.__org + '//' + self.__id + '.txt')
            self.__user = self.__file.openFile()
            if(self.__pass.strip() == self.__user.get_password().strip()):
                self.__log_in_succ = True
                self.__fail_text = ""
                self.log_in_failed()
                self.quit_clicked()
            else:
                self.__fail_text = "Wrong Password!"
                self.log_in_failed()
        except:
            self.__fail_text = "Wrong Organization or Personal ID!"
            self.log_in_failed()

    def log_in_success(self):
        return self.__log_in_succ

    def log_in_failed(self):
        self.__fail_label.configure(text = self.__fail_text)

    def get_user(self):
        return self.__user

    def get_file(self):
        return self.__file

    def add_org(self):
        self.__add_window = Tk()
        self.__add_window.title("Company Name Add Organization")
        self.__add_window.geometry("800x300")

        self.__add_org_entry = Entry(self.__add_window, width = 40)
        self.__add_org_entry.grid(column = 2, row = 2)
        self.__add_org_label = Label(self.__add_window, text = "Enter new organization ID:")
        self.__add_org_label.grid(column = 1, row = 2)
        
        self.__add_id_entry = Entry(self.__add_window, width = 40)
        self.__add_id_entry.grid(column = 2, row = 3)
        self.__add_id_label = Label(self.__add_window, text = "Enter ID of new Owner:")
        self.__add_id_label.grid(column = 1, row = 3)

        self.__add_pass_entry = Entry(self.__add_window, width = 40)
        self.__add_pass_entry.grid(column = 2, row = 4)
        self.__add_pass_label = Label(self.__add_window, text = "Enter owner password")
        self.__add_pass_label.grid(column = 1, row = 4)

        self.__add_name_entry = Entry(self.__add_window, width = 40)
        self.__add_name_entry.grid(column = 2, row = 5)
        self.__add_name_label = Label(self.__add_window, text = "Enter owner name")
        self.__add_name_label.grid(column = 1, row = 5)
        
        self.__add_team_entry = Entry(self.__add_window, width = 40)
        self.__add_team_entry.grid(column = 2, row = 6)
        self.__add_team_label = Label(self.__add_window, text = "Enter owner's new team")
        self.__add_team_label.grid(column = 1, row = 6)

        self.__add_fail_label = Label(self.__add_window, text = "")
        self.__add_fail_label.grid(column = 2, row = 7)
        self.__add_quit_button = Button(self.__add_window, text = "Submit", \
                                    command = self.add_quit_clicked)
        self.__add_quit_button.grid(column = 2, row = 8)

    def add_quit_clicked(self):
        try:
            self.__add_user = User(str(self.__add_id_entry.get()).strip(), str(self.__add_pass_entry.get()).strip(), str(self.__add_name_entry.get()).strip(), str(self.__add_team_entry.get()).strip(), \
                               'Owner', str(self.__add_org_entry.get()).strip(), '0', [])
            if not path.exists(str(self.__add_org_entry.get()).strip()):
                makedirs(str(self.__add_org_entry.get()).strip())
            self.__add_file = FileHandler(str(self.__add_org_entry.get()).strip() + '//' + str(self.__add_id_entry.get()).strip() + '.txt')
            self.__add_file.saveFile(self.__add_user)
            self.__add_window.destroy()
        except Exception as e:
            print(str(e))
            self.__add_fail_text = "Something went wrong! Please try again."
            self.__add_fail_label.configure(text = self.__add_fail_text)
