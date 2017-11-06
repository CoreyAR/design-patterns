from abc import ABCMeta, abstractmethod


class Command(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light(Command):
    def __init__(self, switch):
        if switch == 'on':
            self.execute = self.on()
            self.undo = self.off()
        else if switch == 'off':
            self.execute = self.off()
            self.undo = self.on()
        else:
            raise ValueError("Commands can only be registerd as 'on' or 'off'")

    def on(self):
        print ('turned light on')

    def off(self):
        print ('turned light off')

    def execute(self):
        self.execute()
    
    def undo(self):
        self.undo()