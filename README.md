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
   - **Singleton** - ensure one instance of a class and provide a global access point. Use for central managers or configs.
   - **Factory Method** - define an interface for creating an object, but let subclasses decide which class to instantiate. Use when a class instantiation to subclasses.
   - **Abstract Factory** - provide an interface to create families of related objects without specifying concrete classes. Use for interchangeable product families.
   - **🧱 Builder** - separate construction of a complex object from its representation, allowing step-by-step construction. Use for constructing complex objects with many optional parts.
   - **Prototype** - create new objects by cloning a prototypical instance. Use when creating new instances is expensive or when runtime configuration of types is needed.

2. Structural: compose classes/objects to form larger structures.
   - **Adapter** - convert one interface to another that clients expect. Use to integrate legacy code or third-party libraries.
   - Bridge - separate abstraction from implementation so both can vary independently. Use when you need to vary implementations and abstractions independently.
   - Composite - treat individual objects and compositions uniformly (tree structures). Use for hierarchical data like UI components or file systems.
   - Decorator - add responsibilities to objects dynamically without modifying classes. Use for flexible runtime behavior extension.
   - Facade - provide a simplified interface to a complex subsystem. Use to reduce coupling and simplify client code.
   - Flyweight - share fine-grained, immutable state between many objects to save memory. Use when many similar objects would consume too much memory.
   - Proxy - provide a surrogate or placeholder for another object to control access (lazy init, remote proxy, security).

3. Behavioral: manage algorithms, communication, and responsibilities.
   - Chain of Responsibility
   - Command
   - Interpreter
   - Iterator
   - Mediator
   - Memento
   - Observer
   - State
   - Strategy
   - Template Method
   - Visitor
