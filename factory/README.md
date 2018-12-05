# Factory Pattern

"Define an interface for creating an object, but let subclasses decide which class to instantiate. The Factory method lets a class defer instantiation it uses to subclasses." 

[Gang Of Four](https://en.wikipedia.org/wiki/Design_Patterns)

In this example, we have a pizza Store class that can create a New York store or a Chicago store. Each store in turn has a base ingredient class that it creates pizza classes with depending on the type of pizza ordered.

You can run `PlaceOrder.py` to see the example in action. 