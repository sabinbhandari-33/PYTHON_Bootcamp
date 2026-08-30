class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overloading the + operator
    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    # Display the complex number
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Create two complex number objects
c1 = Complex(4, 5)
c2 = Complex(3, 2)

# Add the two complex numbers
c3 = c1 + c2

# Display the result
print("First Complex Number :", c1)
print("Second Complex Number:", c2)
print("Sum of Complex Numbers:", c3)