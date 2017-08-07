class Router(object):
    class __Router:
        def __init__(self):
            self.history = ['/']
            self.current_route = 0

        def __str__(self):
            return '{} - Current Route: {}'.format(`self`, self.history[self.current_route])

        def back(self):
            if len(self.history) > self.current_route + 2: 
                self.current_route += 1

        def push(self, route):
            self.history = self.history[self.current_route::]
            self.history.insert(0, route)
        
        def get_history(self):
            print(self.history)

    # This is where the singleton reference is kept
    instance = None
    # On creation, check if an instance exists and create one if it doesn't
    def __new__(cls):
        if not Router.instance:
            Router.instance = Router.__Router()
        return Router.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

router_one = Router()
router_one.push('/admin')
router_two = Router()
router_two.push('/dashboard')
router_one.back()
router_two.get_history()
print(router_one)

# Alex Martelli's 'Borg' Singleton

class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class BorgRouter(Borg):
    def __init__(self):
        Borg.__init__(self)
        self.history = ['/']
        self.current_route = 0

    def __str__(self):
        return '{} - Current Route: {}'.format(`self`, self.history[self.current_route])

    def back(self):
        if len(self.history) > self.current_route + 2: 
            self.current_route += 1

    def push(self, route):
        self.history = self.history[self.current_route::]
        self.history.insert(0, route)
    
    def get_history(self):
        print(self.history)

router_one = BorgRouter()
router_one.push('/admin')
router_two = BorgRouter()
router_two.push('/dashboard')
router_one.back()
router_two.get_history()
print(router_one)