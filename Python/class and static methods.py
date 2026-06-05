class College:
    # Class attribute (shared)
    total_students = 0
    
    def __init__(self, name, students):
        self.name = name
        self.students = students
        College.total_students += students  # Updates class attribute
    
    # Instance method (non-static)
    def display_info(self):
        return f"{self.name} has {self.students} students"
    
    # Class method
    @classmethod
    def get_total(cls):
        return f"Total students across all {cls.__name__}: {cls.total_students}"
    
    # Static method (from your notes)
    @staticmethod
    def college():
        return "ABC College"

# Usage
c1 = College("ABC", 100)  # Creates instance, updates total_students
c2 = College("XYZ", 200)  # Updates to 300

# Call class method on class
print(College.get_total())  # Output: Total students across all College: 300

# Call on instance (still works, cls is the class)
print(c1.get_total())      # Same output

# Static method (no cls or self)
print(College.college())   # Output: ABC College

# Instance method (needs self)
print(c1.display_info())   # Output: ABC has 100 students