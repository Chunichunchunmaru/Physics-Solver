import re
import math

def neatFunction (equation):
    terms = []
    coefficients = []
    exponents = []
    signs = []
    isX = []
    
    equation = equation.upper().replace(" ", "")
    
    split = re.split(r'((?<!\^)[+-])', equation)
    for items in split:
        if items == "-" or items == "+":
            signs.append(items)
    # print(signs)
    
    terms.append(split[0])
    for i in range(1, len(split), 2):
        terms.append(str(split[i] + split[i+1]))
    terms = [item for item in terms if item.strip()]
    # print(terms)
    
    for i in range(len(terms)):
        if terms[i].startswith("-X") or terms[i].startswith("X") or terms[i].startswith("+X"):
            coefficients.append(float("1.0"))
            isX.append(1)
            try:
                exponents.append(float(terms[i][terms[i].find("^")+1:len(terms[i])]))
            except:
                exponents.append(1.0)
        elif "X" in terms[i] or "^" in terms[i]:
            coefficients.append(float(terms[i][:terms[i].find("X")]))
            isX.append(1)
            try:
                exponents.append(float(terms[i][terms[i].find("^")+1:len(terms[i])]))
            except:
                exponents.append(1.0)
        else:
            coefficients.append(float(terms[i]))
            isX.append(0)
            exponents.append(0)
    # print(coefficients, exponents)
    
    return(coefficients, exponents, signs, isX)

def findDerivative1 (coef, exponents, xvalue):
    derivative = ""
    derivativeValue = 0
    
    # if len(signs) != len(coef):
    #     signs.insert(0, "+")
    
    for i in range(len(coef)):
        if exponents[i] != 0:
            
        # if isX[i] == 1:
        #     if exponents[i] != 1.0:
        #         derivative += signs[i] + " " + str(abs(coef[i]*exponents[i])) + "x^" + str(exponents[i]-1) + " "
        #     elif exponents[i]-1 == 0:
        #         derivative += signs[i] + " " + str(abs(coef[i])) + " "
          
            derivativeValue += coef[i] * exponents[i] * (xvalue**(exponents[i]-1))
            
    return derivativeValue

def findfuncval (coef, exponents, xvalue):
    value = 0
    for i in range(len(coef)):
        value += coef[i] * ((xvalue)**exponents[i])
    return value

def newtonmethod (initialGuess, coef, exponents, maxiter=100):
    for i in range(maxiter):
        funcval = findfuncval(coef, exponents, xvalue=initialGuess)
        derivativeval = findDerivative1(coef, exponents, xvalue=initialGuess)
        
        if math.isclose(funcval, 0.0, abs_tol=1e-6):
            return initialGuess
        
        initialGuess = initialGuess - (funcval/derivativeval)
        

equation = input("Enter equation: ") # "-3x^21 - 2x^-3 - x + X^0.5 - 3x + 0.5x^0.5 + 1"
initialGuess = float(input("Initial Guess?: "))

coef, exponents, signs, isX = neatFunction(equation)
print(f"X value is equals to {newtonmethod(initialGuess, coef, exponents)}") 
