story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#In Bryan Cranston's autobiography, he describes how after
#his success on Breaking Bad, he developed a scoring system
#for evaluating new scripts that he received.
#
#First, he would assign the script a grade -- A, B, C, D, or
#F -- in each of five categories: Story, Text, Role, Director,
#and Cast.
#
#Then, he would tally those grades into a total score for the
#script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
#For example: an A story, B text, C role, D directory, and
#F cast would get a score of 12: +6 for the story, +4 for the
#text, +2 for the role, +0 for the director, and +0 for the
#cast.
#
#Then, based on that score, the script would be assigned a
#category (note these are slightly different from the image
#because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
#The variables above give the letter grades assigned to each
#of the five components. Write a program that calculates the
#total score he would assign to the script represented by
#these variables. Then on the next line, print the category
#he would assign to that script. For example, for the values
#above, this program would print:
#
#12
#Pass
#
#HINT: This is a *long* program. It's not particularly
#complex -- you're doing the same thing over and over, However,
#that 'same thing' required 4-8 lines each time you do it. Our
#answer is 46 lines long! So, don't think you're off-track just
#because you're writing a lot of lines.


#Add your code here!
#sv = Story Value
sv = 0
#tv = Text Value
tv = 0
#scs = Script Score
scs = 0
#rv = Role value
rs = 0
#dv = Director Value
dv = 0
#cv = Cast/ misc
cv = 0
#For Grading the story
if story == 'A':
    sv = 6
elif story == 'B':
    sv = 5
elif story == 'C':
    sv = 4
elif story == 'D':
    sv = 2
elif story == 'F':
    sv = 0
#For Grading the text
if text == 'A':
    tv = 5
elif text  == 'B':
    tv = 4
elif text  == 'C':
    tv = 3
elif text  == 'D':
    tv = 1
elif story == 'F':
    tv = 0
#For Grading the role
if role == 'A':
    rv = 4
elif role  == 'B':
    rv = 3
elif role  == 'C':
    rv = 2
elif role  == 'D':
    rv = 1
elif role == 'F':
    rv = 0
#For Grading the director
if director == 'A':
    dv = 3
elif director  == 'B':
    dv = 2
elif director  == 'C':
    dv = 1
else:
    dv = 0
#For Grading the cast
if cast == 'A':
    cv = 2
elif cast  == 'B':
    cv = 1
else:
    cv = 0
scs = (sv + tv + rv + dv + cv)
if scs == 20:
    category = 'Perfect score'
elif scs < 20 and scs >= 17:
    category = 'Must do'
elif scs < 17 and scs >= 14:
    category = 'Seriously consider'
elif scs < 14 and scs > 11:
    category = 'On the bubble'
else:
    category = 'Pass'
print (scs)
print (category)
