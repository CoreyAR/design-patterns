# Singleton

This example contains two implementations of a Singleton in python. The first is called `Router`. Everytime the class is created it checks to see if it had been previously created and if so it uses that instance of the class.

The second implementation is called `BorgRouter` and uses an inherited shared state. This allows for multiple classes to inherit and use the same state which achieves the goal of a Singleton in that multiple objects reference the same state.