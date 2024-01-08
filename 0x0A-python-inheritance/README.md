**Inheritance in Object-Oriented Programming (OOP):**

**1. Superclass/Base Class/Parent Class:**
   - A superclass, base class, or parent class is a class that is extended or inherited by another class.
   - It provides common attributes and methods that can be reused by its subclasses.
   - Example: 
     ```python
     class Animal:
         def __init__(self, species):
             self.species = species
         
         def make_sound(self):
             print("Some generic animal sound")
     ```

**2. Subclass:**
   - A subclass is a class that inherits attributes and methods from another class, known as its superclass.
   - It can also have additional attributes and methods or override inherited ones.
   - Example:
     ```python
     class Dog(Animal):
         def __init__(self, breed):
             super().__init__('Dog')
             self.breed = breed
         
         def make_sound(self):
             print("Woof! Woof!")
     ```

**3. Listing Attributes and Methods:**
   - To list all attributes and methods of a class or instance, you can use `dir()` or `vars()` functions.
     ```python
     print(dir(Dog))  # List all attributes and methods of the Dog class
     ```

**4. Adding New Attributes:**
   - Instances can have new attributes assigned dynamically.
     ```python
     my_dog = Dog('Labrador')
     my_dog.age = 3  # Adding a new attribute 'age' to the instance
     ```

**5. Inheriting from Another Class:**
   - To inherit from another class, include the superclass in the parentheses after the subclass name.
     ```python
     class LabradorDog(Dog):
         def __init__(self, color):
             super().__init__('Labrador')
             self.color = color
     ```

**6. Multiple Base Classes:**
   - You can inherit from multiple classes by separating them with commas.
     ```python
     class HybridDog(Dog, LabradorDog):
         def __init__(self, breed, color):
             super().__init__(breed)
             LabradorDog.__init__(self, color)
     ```

**7. Default Class Inheritance:**
   - In Python, every class inherits from the `object` class by default.
     ```python
     class MyClass:
         # Implicitly inherits from 'object'
         pass
     ```

**8. Method/Attribute Override:**
   - To override a method or attribute from the base class, re-implement it in the subclass.
     ```python
     class Cat(Animal):
         def make_sound(self):
             print("Meow!")
     ```

**9. Inherited Attributes/Methods:**
   - All public attributes and methods of the superclass are available to subclasses.
   - Use `super()` to access and call methods from the superclass.

**10. Purpose of Inheritance:**
    - Code reuse: Avoid duplication of code by sharing common functionality.
    - Extensibility: Easily add or modify features without affecting existing code.
    - Polymorphism: Allows objects of different classes to be treated as objects of a common base class.

**11. Built-in Functions:**
   - `isinstance(obj, class_or_tuple)`: Checks if an object is an instance of a class or a tuple of classes.
   - `issubclass(class, classinfo)`: Checks if a class is a subclass of another class.
   - `type(obj)`: Returns the type of an object.
   - `super(subclass, instance)`: Returns a temporary object of the superclass, used to call its methods.

Understanding and using inheritance is fundamental to building scalable and maintainable code in OOP. It promotes code organization, reusability, and abstraction.
