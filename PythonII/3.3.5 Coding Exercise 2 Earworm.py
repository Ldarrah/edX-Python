lyrics = ["I can't do this all on my own, no I know", "I'm no superman"]
lines_of_sanity = 12

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you have a song stuck in your head. Worse, you have
#only a few lines from a song stuck in your head. They just
#keep repeating over and over. The specific lines you have
#stuck in your head are stored in the variable lyrics.
#
#You can only stay sane so long while doing this.
#Specifically, you can only listen to lines_of_sanity lines
#before going crazy. Once you've reached lines_of_sanity,
#your brain will finish out the current list, then crumble.
#
#Write some code that will print the lyrics that run through
#your head. It should keep repeating each line one-by-one
#until you've reached lines_of_sanity lines. Then, it should
#keep going to finish out the current verse. After that, print
#"MAKE IT STOP" in all caps (without the quotes).
#
#HINT: Remember, we can iterate through items in a list using
#this syntax:
#
#  for item in list_of_items:
#
#HINT 2: You'll probably need a counter to count how many lines
#have been printed so far.


#Add your code here! Using the initial inputs from above, this
#should print 9 lines: all 4 lines of the list twice, followed
#by MAKE IT STOP
item = 0
count = 0
for i in range(lines_of_sanity):
    while count < lines_of_sanity:
        for item in lyrics:
            print(item)
            count += 1
print('MAKE IT STOP')












