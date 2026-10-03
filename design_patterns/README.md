# Introduction to Design Patterns with Python

## Description

This project introduces common software design patterns and demonstrates how they can be applied in Python to create flexible, maintainable, and extensible object-oriented programs.

The project focuses on three foundational design patterns:

- **Factory Pattern** — centralizes object creation.
- **Observer Pattern** — allows objects to react to events without tight coupling.
- **Decorator Pattern** — extends object behavior through composition without modifying existing classes.

These patterns demonstrate important object-oriented design principles such as the **Open/Closed Principle** and **composition over inheritance**.

## Learning Objectives

By the end of this project, I should be able to:

- Explain what design patterns are and why they are useful.
- Distinguish between creational, behavioral, and structural design patterns.
- Understand how design patterns improve maintainability and extensibility.
- Apply the Factory pattern to centralize object creation.
- Apply the Observer pattern to implement event-based communication.
- Apply the Decorator pattern to extend behavior using composition.
- Understand and apply the Open/Closed Principle.
- Recognize when composition is preferable to inheritance.

## Design Patterns

### Factory Pattern

The Factory pattern is a **creational design pattern**.

It centralizes object creation so that other parts of the program do not need to know which concrete class should be instantiated.

In this project, a vehicle factory uses a registry to create different vehicle types. New vehicle types can be registered without modifying the factory's core creation logic.

### Observer Pattern

The Observer pattern is a **behavioral design pattern**.

It allows one object, called the subject or publisher, to notify multiple observers when an event occurs.

This reduces coupling because the publisher does not need to know the concrete implementation of each observer.

### Decorator Pattern

The Decorator pattern is a **structural design pattern**.

It allows additional behavior to be added to an object dynamically by wrapping it with another object.

This provides a flexible alternative to creating many subclasses for every possible combination of behaviors.

## Key Principles

### Open/Closed Principle

Software components should be:

> Open for extension, but closed for modification.

New functionality should be added whenever possible without changing existing working code.

### Composition Over Inheritance

Instead of creating many subclasses to represent different combinations of behavior, objects can be combined through composition.

This often produces designs that are easier to extend and maintain.

## Requirements

- Python 3.10 or later
- All files must begin with:

```python
#!/usr/bin/env python3
```

- Code must follow PEP 8 style guidelines.
- No external dependencies are required unless explicitly stated.
- Python files can be executed using:

```bash
python3 <filename>
```

## Project Files

| File | Description |
|---|---|
| `0-factory.py` | Demonstrates the Factory pattern using a vehicle registry |
| `1-observer.py` | Demonstrates the Observer pattern by adding subscribers to events |
| `2-decorator.py` | Demonstrates the Decorator pattern by wrapping objects with additional behavior |

