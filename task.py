class Task:
    def __init__(self, date_due, status, objective, urgency, reported):
        self.__date_due = date_due
        self.__status = status
        self.__objective = objective
        self.__urgency = urgency
        self.__reported = reported

    def set_date_due(self, date):
        self.__date_due = date

    def set_status(self, status):
        self.__status = status

    def set_objective(self, objective):
        self.__objective = objective

    def set_urgency(self, urgency):
        self.__urgency = urgency

    def set_reported(self, reported):
        self.__reported = reported
        
    def get_date_due(self):
        return self.__date_due

    def get_status(self):
        return self.__status

    def get_objective(self):
        return self.__objective

    def get_urgency(self):
        return self.__urgency

    def get_reported(self):
        return self.__reported
