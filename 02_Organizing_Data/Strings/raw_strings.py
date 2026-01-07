''' --- Double Quotes --- '''
# Use back slashes to use double quotes inside a print function 
print("I said, \"Let's go!\"")
print('I said, "Let\'s go!"')

''' --- Raw Strings --- '''
# Functin: Adding an r before the string makes it so that backslashes doesn't do anything 
# Note: Backslashes are used to allow for the use of double quotes or quotes in a print function

path1 = "C:\\Documents\\code\\data1.csv" # Normal String
path2 = r"C:\Documents\code\data2.csv" # Raw String 

latex1 = "$\\cos \\theta = \\drafc{\\sqrt{3}}{2}$" # Normal String
latex2 = r"$\cos \theta = \drafc{\sqrt{3}}{2}$" # Raw String