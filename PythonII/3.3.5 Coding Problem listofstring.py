mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above is a list of strings. Don't worry if this syntax is a
#little unfamiliar, we'll talk you through it and then cover
#it more in chapter 4.3.
#
#Write some code that will count the number of instances of
#the letter 't' in the list of strings. Count both capital
#'T' and lower-case 't'. Then, print the number of instances
#of the letter 't'.
#
#For example, with the list declared above, you would print
#6: two in the first string, three in the second, one in the
#third.
#
#Because we haven't used lists very extensively, we've
#gotten you started. The loop below will iterate through each
#string in the list. Next, you want to iterate through each
#letter in the current string, check if it's a t, and
#increment a counter if so.


#You'll want to add some code before the loop here.
totalt=0
for string in mystery_list:
    nummc = 0
    for currentCharacter in string:
        if currentCharacter == 'T':
            nummc += 1
        if currentCharacter == 't':
            nummc += 1
    else:
        totalt += nummc
print(totalt)

#Add some code here to print the final tally!





