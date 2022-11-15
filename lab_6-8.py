# author: JHR 11/10/22

# defining inputs and empty list
one = int(input("Would you be so kind as to input a number?"))
two = int(input("Would you be so kind as to input a number?"))
three = int(input("Would you be so kind as to input a number?"))
four = []

# appending list
four.append(one)
four.append(two)
four.append(three)

# if else statements if all are even
if one % 2 == 0 and two % 2 == 0 and three % 2 == 0:
    print ("EVEN")
elif one % 2 != 0 and two % 2 == 0:
    print ("MIXED")
elif one % 2 == 0 and two % 2 != 0:
    print ("MIXED")
elif one % 2 == 0 and two % 2 == 0 and three % 2 != 0:
    print ("MIXED")
elif one % 2 != 0 and two % 2 != 0 and three % 2 == 0:
    print ("MIXED")
else:
    print ("ODD")