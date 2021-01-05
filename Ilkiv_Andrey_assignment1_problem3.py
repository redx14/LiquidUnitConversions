#Andrey Ilkiv 9/30/2020 section 01 baker helper mL --> fl oz full conversion

#---------You can use this code it works--------
#quantity = float(input('Please enter the amount of mL you wish to convert : '))
#ml = quantity
#---------Delete ml variable down below, these comments, and then run----------


#variables and conversions for 250 ml
ml = 250.0
tsp = 0.202884 * ml
tbsp = tsp/3
cup = tbsp/16
pint = cup/2
quart = pint/2
gallon = quart/4
floz = tsp/6



print('-------------------------------------------' , '       mL to US Fluid Volume Units' , '-------------------------------------------' , sep='\n')
#prints string header for asthetics and uses \n in place of commas to print next line

print('mL:         ' + str(ml))
#prints "ml:" with spaces, converts ml variable from float to string and adds it to the string being printed
#in this case ml is converted from float to string and equals "250.0"

print('tsp:        ' + str(tsp))
#prints "tsp:" with spaces, converts tsp variable from float to string and adds it to the string being printed

print('tbsp:       ' + str(tbsp))
#prints "tbsp:" with spaces, converts tbsp variable from float to string and adds it to the string being printed

print('cup(s):     ' + str(cup))
#prints "cup(s):" with spaces, converts cup variable from float to string and adds it to the string being printed

print('pint(s):    ' + str(pint))
#prints "pint(s):" with spaces, converts pint variable from float to string and adds it to the string being printed

print('quart(s):   ' + str(quart))
#prints "quart(s):" with spaces, converts quart variable from float to string and adds it to the string being printed

print('gallon(s):  ' + str(gallon))
#prints "gallon(s):" with spaces, converts gallon variable from float to string and adds it to the string being printed

print('fl oz:      ' + str(floz))
#prints "fl oz:" with spaces, converts floz variable from float to string and adds it to the string being printed


print('-------------------------------------------')
#printed for asthetics
