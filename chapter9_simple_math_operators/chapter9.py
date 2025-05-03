"""Numerical types and their metaclasses
The numbers module contains the abstract metaclasses for the numerical types:
subclasses numbers.Number numbers.Integral numbers.Rational numbers.Real numbers.Complex
bool ✓ ✓ ✓ ✓ ✓
int ✓ ✓ ✓ ✓ ✓
fractions.Fraction ✓ ― ✓ ✓ ✓
float ✓ ― ― ✓ ✓
complex ✓ ― ― ― ✓
decimal.Decimal ✓ ― ― ― ―
Python does common mathematical operators on its own, including integer and float division, multiplication,
exponentiation, addition, and subtraction. The math module (included in all standard Python versions) offers
expanded functionality like trigonometric functions, root operations, logarithms, and many more."""