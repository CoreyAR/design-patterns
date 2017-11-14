from abc import ABCMeta, abstractmethod
from datetime import date

class Daily(object):
    __metaclass__ = ABCMeta

    def start_day(self):
        self.__wake_up()
        self.__eat_breakfast()
        self.__brush_teeth()
        self.get_dressed()
        self.go_to_work()


    def __wake_up(self):
        print('Open you eyes sunshine!')
    
    def __eat_breakfast(self):
        print('Eat something delicious and sustaining.')

    def __brush_teeth(self):
        print('Brush teeth! ✨ 😁 ✨')

    @abstractmethod
    def get_dressed(self):
        pass
    
    def go_to_work(self):
        pass

class WorkDay(Daily):
    def get_dressed(self):
        print('Put on something besides sweatpants.')

    def go_to_work(self):
        print('The bus leaves in 10 minutes!')

class Weekend(Daily):
    def get_dressed(self):
        print('Wear sweatpants.')

if __name__ == '__main__':
    idx= date.strftime(date.today(), '%w')
    if idx != 0 or idx != 6:
        day = WorkDay()
    else:
        day = WeekDay()
    day.start_day()
