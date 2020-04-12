faveLanguage = "Spanish"
faveInstrument = "fiddle"
faveDrink = "iced tea"
faveBook = "Atlas Shrugged"
coolLanguages = ["Afrikaans", "Finnish", "Latin", "American Sign Language"]
coolInstruments = ["didgeridoo", "pan pipes", "church organ", "fiddle"]
coolDrinks = ["civet coffee", "kombucha", "kefir"]
coolBooks = ["The Catcher in the Rye", "Atlas Shrugged", "Anna Karenina", "Hamlet"]
if faveBook in coolBooks:
    print("Nice book choice!")
    if faveLanguage in coolLanguages:
        print("Let's practice together sometime!")
        if faveInstrument in coolInstruments:
            print("I play that, too!")
    else:
        print("You should learn a new language.")
        if faveDrink in coolDrinks or faveInstrument in coolInstruments:
            print("You have good taste!")
        else:
            print("What cool things are you into?")
else:
    print("See you later...")