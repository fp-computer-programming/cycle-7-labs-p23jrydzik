# author: JHR 11/09/22

# defining variable
l1 = [3000, 78, 99, 1002]
sortaroonie = sorted (l1)

# length
if len(l1) <2:
    print ("error: list does not meet specifications")
# no if not unique
elif sortaroonie [0] == sortaroonie[-1]:
    print ("error: list does not meet specifications")
# printing results
else:
    print ("high: " + str(sortaroonie[-1]))
    print ("low: " + str(sortaroonie[0]))

