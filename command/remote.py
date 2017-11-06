from Commands import command


class Remote(object):
    def __init__(self):
        self.onCommands = []
        self.offCommands = []
        self.undoCommand = Command

        for i in range(0,7):
            self.onCommands[i] = Command
            self.offCommands[i] = Command

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    
    def onButtonWasPushed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]
    
    def offButtonWasPushed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]
    

    def undoButtonWasPushed(self):
        self.undoCommand.undo()

    def toString(self):
        pass


universal_remote = Remote()