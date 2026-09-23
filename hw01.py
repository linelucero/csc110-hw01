# ------------------------------------------------------
#        Name: Aline Valenzuela-Lucero
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------


def main():
    """
    This is a Docstring for the main function. This is the short description.

    Here, after a blank line, you can add a longer paragraph description.
    Docstrings are like long comments that we put right under the function definition.
    The Docstring goes from one set of "opening" three double-quotes to
    another set of "closing" three double-quotes. We also try to keep the lines short.
    The Docstring has 4 sections:
      - the short one-line description
      - the paragraph description
      - the Params section that indicates input parameters and return values
      - the "how to run" section called "Example Use".

    PARAMS:
        - None. If the function took an input int of "apples" called num, we would
                indicate it like this: - num: int with number of apples
    RETURNS:
        - None. If the function returned something (like the integer half of num),
                we would indicate it like this: int : integer half of num
    """

    # ========== Setup for HW. DO NOT MODIFY ======
    x=0
    y=0
    a=0
    b=0
    c=0
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    result5 = 0
    # End of Setup code ---------------------------



    # Part 1: Basic Operations
    # =============================================
    # Your code for part 1 under this line and before the print statements
   
    x = 27 #assign 27 to variable x
    y = 1 #assign 1 to variable y
    a = 1.5 #assign 1.5 to variable a
    b = 7 #assign 7 to variable b
    c = -1 #assign -1 to variable c
    
    result1 = (3*float(x) - 9*float(y))/(2*a*(float(b)-float(c)))
    #assign the arithmetic expression of (3x-9y)/(2a(b-c)) to result1

    #Part 1 ; x =27
    print("Part 1: x =", x) #print variable x and its value
    print("Part 1: y =", y) #print variable y and its value
    print("Part 1: a =", a) #print variable a and its value
    print("Part 1: b =", b) #print variable b and its value
    print("Part 1: c =", c) #print variable c and its value
    print("Part 1: result =", result1) #print the result and its value
    
    # End of Part 1 ----------------------


    # Part 2: Power
    # =============================================
    # Your code for part 2 under this line and before the print statements
    
    x = 5 #assign the value of 5 to x
    y = -3 #assign the value of -3 to y
    result2 = (x**2)*(y**4)
    #compute x^2 times y^4 and assign it to result2
    
    print("Part 2: x =", x) #print x and its value
    print("Part 2: y =", y) #print y and its value
    print("Part 2: result =", result2) #print the result and its value
    
    # End of Part 2 ----------------------



    # Part 3: Integer divide
    # =============================================
    # Your code for part 3 under this line and before the print statements
    
    a = 100 #total number of treats
    b = 13 #total number of dogs
    result3 = int(a/b) #total number of whole treats each dog gets
    
    print("Part 3: a =", a) #print the value of a
    print("Part 3: b =", b) #print the value of b
    print("Part 3: result =", result3) #print the value of the result
    
    # End of Part 3 ----------------------


    # Part 4: Modulo
    # =============================================
    # Your code for part 4 under this line and before the print statements
    
    result4 = a%b #compute the leftover value of the division from part 3
    
    print("Part 4: result =", result4) #print the value of the result
    
    # End of Part 4 ----------------------

if __name__ == "__main__":
    main()
