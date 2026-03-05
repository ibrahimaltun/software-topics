# General Software Topics

## 0- Common Topics

- A. Thread-safe
- B. Metaclass
- C. Inversion of Control - IoC
- D.

## 1- Design Patterns

- Reusable solutions for common software design problems

### Categories grouped by purpose

1. Creational: control object creation and composition.
   - Singleton - ensure one instance of a class and provide a global access point. Use for central managers or configs.
   - Factory Method - define an interface for creating an object, but let subclasses decide which class to instantiate. Use when a class instantiation to subclasses.
   - Abstract Factory - provide an interface to create families of related objects without specifying concrete classes. Use for interchangeable product families.
   - Builder - seperate construction of a complex object from its representation, allowing step-by-step construction. Use for constructing complex objects with many optional parts.
   - Prototype - create new objects by cloning a prototypical instance. Use when creating new instances is expensive or when runtime configuration of types is needed.

2. Structural: compose classes/objects to form larger structures.
   - Adapter
   - Facade
   - Decorator
   - Proxy
   - Composite
   - Bridge

3. Behavioral: manage algorithms, communication, and responsibilities.
   - Strategy
   - Observer
   - Command
   - Chain of Responsibility
   - Template Method
   - State
