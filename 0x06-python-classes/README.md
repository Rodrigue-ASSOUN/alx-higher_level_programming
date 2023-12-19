1. **OOP (Object-Oriented Programming):**
   - OOP is a way of writing code that revolves around objects, which represent real-world entities. It brings together data (attributes) and the operations that can be performed on that data (methods) into a single unit called a class.

2. **"First-Class Everything":**
   - In Python, everything is an object. This means you can treat functions, classes, and data as objects, allowing you to manipulate them just like any other object.

3. **Class:**
   - A class is a blueprint or template for creating objects. It defines the attributes and behaviors that its objects will have.

4. **Object and Instance:**
   - An object is an instance of a class. It's a concrete occurrence of the class, representing a specific entity. Instance and object are often used interchangeably.

5. **Difference Between Class and Object/Instance:**
   - A class is like a recipe, describing how to create objects. An object is a specific instance created from that recipe.

6. **Attribute:**
   - Attributes are characteristics or properties that describe the object. For example, a `Car` class might have attributes like color, model, and year.

7. **Public, Protected, and Private Attributes:**
   - Public attributes can be accessed from anywhere, protected attributes (single underscore) should be accessed within the class and its subclasses, and private attributes (double underscore) are accessible only within the class.

8. **self:**
   - `self` is a reference to the instance of the class. It's a convention to use `self` as the first parameter in methods to refer to the instance on which the method is called.

9. **Method:**
   - A method is a function associated with an object. It defines the behavior of the object.

10. **__init__ Method:**
    - The `__init__` method is a special method in Python classes. It's called when an object is created and is used for initializing the object's attributes.

11. **Data Abstraction, Data Encapsulation, and Information Hiding:**
    - Data Abstraction is about representing only essential features without including implementation details. Data Encapsulation involves bundling data and methods into a single unit. Information Hiding restricts access to certain details and exposes only what is necessary.

12. **Property:**
    - A property is a special attribute that allows controlled access to an object's attributes. It is implemented using the `@property` decorator.

13. **Difference Between Attribute and Property in Python:**
    - An attribute is a characteristic of an object, while a property is an attribute with added functionality, often used to control access.

14. **Pythonic Way to Write Getters and Setters:**
    - Use the `@property` decorator for getters and `@<attribute_name>.setter` decorator for setters.

15. **Dynamically Creating Arbitrary New Attributes:**
    - You can dynamically create attributes using the dot notation or the `setattr()` function.

16. **Binding Attributes to Objects and Classes:**
    - Attributes are bound to objects by assigning values to them or by using methods that modify them.

17. **__dict__ of a Class/Instance:**
    - `__dict__` is a dictionary containing a class or instance's attributes and their values.

18. **How Python Finds Attributes:**
    - Python searches for attributes first in the instance, then in the class, and finally in the inheritance hierarchy.

19. **Using getattr Function:**
    - `getattr(obj, 'attribute_name')` is used to get the value of an attribute dynamically.

