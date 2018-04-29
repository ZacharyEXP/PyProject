class User:
    def __init__(self, e_id, password, name, team, occ, org, strikes, tasks):
        self.__e_id = e_id
        self.__password = password
        self.__name = name
        self.__team = team
        self.__occ = occ
        self.__org = org
        self.__strikes = strikes
        self.__tasks = []
        self.__tasks.extend(tasks)

    def set_e_id(self, e_id):
        self.__e_id = e_id

    def set_password(self, password):
        self.__password = password

    def set_name(self, name):
        self.__name = name

    def set_team(self, team):
        self.__team = team

    def set_occ(self, occ):
        self.__occ = occ

    def set_org(self, org):
        self.__org = org

    def set_strikes(self, strikes):
        self.__strikes = strikes

    def set_tasks(self, tasks):
        self.__tasks = tasks

    def set_task(self, task, x):
        self.__tasks[x] = task

    def add_tasks(self, tasks):
        self.__tasks.append(tasks)

    def get_e_id(self):
        return self.__e_id

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def get_team(self):
        return self.__team

    def get_occ(self):
        return self.__occ

    def get_org(self):
        return self.__org

    def get_strikes(self):
        return self.__strikes

    def get_tasks(self):
        return self.__tasks

    def get_task(self, x):
        return self.__tasks[x]

    def remove_task(self, x):
        self.__tasks.remove(self.__tasks[x])
