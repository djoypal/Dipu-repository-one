#try:
#	value=int(input("Age: "))
#	print("Age: ",value)
#except Exception as e:
#	print("Some error\n",e)




#try:
#	age=int(input("Age: "))
#	if age<1:
#		raise ValueError
#	else:
#		print("Age: ",value)
#except Exception as e:
#	print("enter numerical value----",e)
#except ValueError:
#	print("Some error\n")




# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while number==10:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        
print()
print("Congratulations! You guessed it correctly.")
