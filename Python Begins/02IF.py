weight = int(input("weight"))
unit = input("(K)g or (l)bs: ")

#Capital letter will signify input value  is in kgs

if unit.upper() == "k" :
    converted = weight / 0.45
    print  ("weight in lbs: " + str(converted))

else:
    converted = weight * 0.45
    print ("weight in kgs: " + str(converted))