class LogEvent:
    def __init__(self, role, id, command, lines, time, details = None):
        self.details = details
        self.time = time
        self.lines = lines
        self.command = command
        self.id = id
        self.role = role

    def role(self):
        return self.role

    def id(self):
        return self.id

    def command(self):
        return self.command

    def crash(self):
        return self.crash

    def lines(self):
        return self.lines

    def time(self):
        return self.time

    def details(self):
        return self.details

    def toJSON(self):
        return self.__dict__
