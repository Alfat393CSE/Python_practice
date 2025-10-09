class MyComplexNumber :
    # constructor method
    def __init__(self, real=0, imag=0) :
        print("MyComplexNumber constructor executing...")
        self.real = real
        self.imag = imag

    def displayComplex(self) :
        print("{0} + {1}i".format(self.real, self.imag))

# create an object against the class
cmplx1 = MyComplexNumber(40, 50)

# call the method using the object
cmplx1.displayComplex() # Output: 40 + 50i

cmplx2 = MyComplexNumber() # default values will be assigned
cmplx2.displayComplex() # Output: 0 + 0i

# Create another object against the class
# and create a new attribute 'new_attribute' 
cmplx3 = MyComplexNumber(10,20)
cmplx3.new_attribute = 80 # new attribute

cmplx3.displayComplex() # Output: 10 + 20i

print((cmplx3.real, cmplx3.imag, cmplx3.new_attribute)) # Output: 10 20 80

# print((cmplx1.real, cmplx1.imag, cmplx1.new_attribute)) # AttributeError: 'MyComplexNumber' object has no attribute 'new_attribute'

# Deleting object attributes and object

print(cmplx2) # Output: <__main__.MyComplexNumber object at 0x7f8b8c2e1d60>

del cmplx2.real # delete attribute 'real' of object cmplx2
# print(cmplx2.real) # AttributeError: 'MyComplexNumber' object has

del cmplx2.imag # delete attribute 'imag' of object cmplx2
# print(cmplx2.imag) # AttributeError: 'MyComplexNumber' object has no attribute 'imag'

del cmplx2 # delete object cmplx2
# print(cmplx2) # NameError: name 'cmplx2' is not defined