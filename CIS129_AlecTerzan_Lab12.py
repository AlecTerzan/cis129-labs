# Create new class
class Pet:
    # Declare variables for class
    __name: str
    __type: str
    __age: int
    # Create constructor
    def __init__(self, n, t, a):
        self.__name = n
        self.__type = t
        self.__age = a
    # Create mutators and functions
    def setName(self, n):
        self.__name = n
    def setType(self, t):
        self.__type = t
    def setAge(self, a):
        self.__age = a
    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    def getAge(self):
        return self.__age
    
def main():
    # Declare necessary variables
    inputName: str
    inputType: str
    inputAge: int
    Animal: Pet
    # Declare new object
    Animal = Pet
    # Get pet name from user
    print("Enter a pet name:\n")
    inputName = input()
    Animal.setName(Animal, inputName)
    # Get pet type from user
    print("Enter a pet type:\n")
    inputType = input()
    Animal.setType(Animal, inputType)
    # Get pet age from user
    print("Enter a pet age:\n")
    inputAge = input()
    Animal.setAge(Animal, inputAge)
    # Display Animal information
    print("The pet name is ", Animal.getName(Animal))
    print("The pet type is ", Animal.getType(Animal))
    print("The pet age is ", Animal.getAge(Animal))
# Run program
main()
