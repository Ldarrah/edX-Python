mystery_string = "Aello! What a fine day it is today."
mystery_character = "a"

#-----------------------------------------------------------
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write some code below that will count and print how many
#times mystery_character appears in mystery_string. You may
#not use the string class's .count method.
#
#With the original values for mystery_string and
#mystery_character, your code should initially print 4. Only
#count characters with the same case as mystery_character
#(in other words, here you would ignore capital A).


#Add your code here!
nummc = 0
for currentCharacter in mystery_string:
    if currentCharacter == mystery_character:
        nummc += 1
print(nummc)





