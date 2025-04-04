 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# HIGA_Conditionals.v5.py shows how to use conditional statements and comparison operators in python.
#
# Created by Scott Higa, 2025-03-10
# Last edit: 2025-04-03
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


try:
    var1 = float(input("Enter a number: "))  ### User input saved as a float to check if number is an integer
    try:
        var2 = str(var1)  ### Try to change the probable integer to a string so we can check the last character in the text
        if var2[-1] != "0":   ###  If the last character in the string is not a zero, the number must be a decimal.
            print ("That's a number but could you please enter a whole number")  ### If the user enters a decimal, this print function will run and the code will skip this scope and jump to the next try:
        else: print("Whole Number")  ###  We need to put something here for the if/else catch.  If the user input is a whole number and not text, the program will continue to the next line for the even/odd, > 10, and prime checks

        var3 = int(var1)  #  Setting var3 to the integer value of var1
        # if the user inputs a decimal, it will round to the nearest whole number for the following checks in this scope

        if var3 % 2 == 0:  ### 1st conditional: If the modulus of var1 when divided by 2 equals zero, the whole number must be even
            print("Your number is even")   ### If var1 passes the first check, it must be even
        else: print ("Your number is odd")   ### If var 1 doesn't pass the first check, it must be odd

        if var3 > 10:   ### 2nd conditional: Check to see if var1 is greater than 10.  In most cases, var1 should be greater than 10.  If true, program would just need to run next line and can finish.
            print ("Your number greater than 10")   ### Most cases, this will print to console and end program
        else: print ("Your number is less than 10")   ###  If var1 doesn't pass this second conditional, it's either less than 10 or equal to 10.  The former is more likely to happen so we will check to see if it's prime in the next conditional.

        if var3 == 2 or var3 == 3 or var3 == 5 or var3 == 7:   ### 3rd conditional: Since var1 is now <= 10, we can check if its prime.  Checking each number individually, guessing this is the 'hammer approach.'
            print ("Your number is prime")   ### var1 passed the 3rd conditional and is prime
        else: print ("Your number is not prime")   ### var1 did not pass the 3rd conditional so it's not prime.  This only works on prime numbers less than 10.  If user inputs a prime number larger than 10, the console will still spit out "Your number is not prime"

        if var3 == 10:   ### 4th conditional:  If var1 is not less than or greater than 10, var1 must be equal to 10.  This is the most unlikely case, so we should make it the last conditional.
            print("Your number is 10")  ### Since we've eliminated all other integers, we don't need an else statement here.

    except:
        print("decimal") ### this catch is for the second try.  I'm not sure what function I should put here and it doesn't seem to catch anything...

except ValueError:  ### This catch is for just in case the user enters text and so our program doesn't die
    print("I told you to enter a number")  ### Gentle reminder

try:
    var4 = float(input("Enter another number: "))  ### Asking the user for another input, hopefully it's an integer :(
    print("Sum:",float(var3 + var4))  ###  Print the sum of both numbers

except ValueError:  ### Catch if user inputs text instead of numbers
    print("I told you to enter a number")  ### Response to user if they don't input a whole number (including a whole number with a decimal on the end, ie. 1.0 or 10.0)

print ("")
print("Done!")