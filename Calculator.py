
class Calculator:

    def add(self,first,second):
        if (not(isinstance(first,float)) and not(isinstance(first,int))) or (not(isinstance(second,float)) and not(isinstance(second,int))):
            raise TypeError("You've entered a variable that's not integer or double.")
        else:
            return round(first+second,20)


    def subtract(self,first,second):
        if (not(isinstance(first,float)) and not(isinstance(first,int))) or (not(isinstance(second,float)) and not(isinstance(second,int))):
            raise TypeError("You've entered a variable that's not integer or double.")
        else:
            return round(first-second,20)


    def multiply(self,first,second):
        if (not(isinstance(first,float)) and not(isinstance(first,int))) or (not(isinstance(second,float)) and not(isinstance(second,int))):
            raise TypeError("You've entered a variable that's not integer or double.")
        else:
            return round(first*second,20)


    def divide(self,first,second):
        if (not(isinstance(first,float)) and not(isinstance(first,int))) or (not(isinstance(second,float)) and not(isinstance(second,int))):
            raise TypeError("You've entered a variable that's not integer or double.")
        if second == 0:
            print("second is 0!")
            raise TypeError("Can't divide by 0!")
        else:
            return round(first/second,20)

