# Template Method

The template method pattern creates a base class that subclasses can use to implement and customize and algorithm. The template method pattern builds the base class with three types of methods. Abstract methods, concrete methods and hooks. 
    - Concrete methods are implemented in full and are not changed
    - Abstract methods are implemented by the subclasses.
    - Hooks are provided to allow the sub class to optionally respond to different steps in the algorithm.