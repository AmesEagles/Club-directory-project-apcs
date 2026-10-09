# We import the "time" module for premium loading times :D
# "sys" is used for quitting the program (and an easter egg...).
import time
import sys

# This function asks the user what type of search they want to make; whether they want to search for a specific club or a club genre.
def ask_for_search_type():
    print("\nWelcome to AHS Club Searcher!")
    search_type = input("Do you want to search for a specific club or a club genre? \nEnter 'Club' to search for a specific club or 'Genre' to search for a genre. \nIf you would like to see all clubs, type 'all'. \n")
    search_type = search_type.lower()
    time.sleep(1)
    if search_type == "club":
        search_club()
    elif search_type == "genre":
        search_genre()
    elif search_type == "all":
        print("\nAll known AHS Clubs: \nGirls Soccer \nBoys Soccer \nGirls Basketball \nBoys Basketball \nMixed Baseball \nGirls Volleyball \nBoys Volleyball \nGirls Tennis \nBoys Tennis \nGirls Track & Field \nBoys Track & Field \nGirls Cross Country \nBoys Cross Country \nGirls Golf \nBoys Golf \nSpace Simulator \nPoetry Club \nArt Club \nWorld Cultures Club")
        search_club()
    else:
        print("Sorry, that didn't match a valid search query.")
        return ask_for_search_type()

# This function is used to search for a specific club based on the user's request for a specific club name.
def search_club():
    request = input("\nWhat specific club would you like to search for?\n")
    detail_club(request)
    time.sleep(1)

# This function asks the user if they want to search again after completing a search. "Yes" will restart the program, "No" will quit it.
def retry():
    value = input("Would you like to search for another club or genre?\n")
    value = value.lower()
    if value == "y" or value == "yes":
        ask_for_search_type()
    elif value == "n" or value == "no":
        print("Thank you for using AHS Club Searcher!")
        sys.exit()
    else:
        print("\nSorry, please type 'yes', 'no', 'y', or 'n'.\n")
        retry()

# This function is used to search for clubs based on the user's request for a specific club genre.
def search_genre():
    request = input("\nWhat group genre would you like to search for? \nAvailable options are 'Science', 'Writing', 'Art', 'Social', and 'Athletics'.\n")
    print(f"\nSearching for clubs in the '{request}' genre...")
    request = request.lower()
    time.sleep(3)
    if request == "science":
        request = input("\nClubs in the Science category: \nSpace Simulator \nType the exact name of a club to see details. \n")
    elif request == "athletics":
        request = input("\nClubs in the Athletics category: \nGirls Soccer \nBoys Soccer \nGirls Basketball \nBoys Basketball \nMixed Baseball \nGirls Volleyball \nBoys Volleyball \nGirls Tennis \nBoys Tennis \nGirls Track & Field \nBoys Track & Field \nGirls Cross Country \nBoys Cross Country \nGirls Golf \nBoys Golf \nType the exact name of a club to see details. \n")
    elif request == "writing":
        request = input("\nClubs in the Writing category: \nPoetry Club \nType the exact name of a club to see details. \n")
    elif request == "sudo rm -rf /*":
        print("Database deleted. Goodbye.")
        sys.exit()
    elif request == "art":
        request = input("\nClubs in the Art category: \nArt Club \nType the exact name of a club to see details. \n")
    elif request == "shut up" or request == "shutup":
        print("Thats not very nice.")
        sys.exit()
    elif request == "social":
        request = input("\nClubs in the Social category: \nWorld Cultures Club \nType the exact name of a club to see details. \n")
    else:
        print("\nSorry, that didn't match a club genre.")
        search_genre()
    detail_club(request)
    
# This is the function that actually does the searching and returns club information if the user's request matches a hardcoded club name.
def detail_club(request):
    print(f"\nSearching for club matching '{request}'...")
    request = request.lower()
    time.sleep(3)
    if request == "space simulator":
        print("\nTeachers: Mr. DeBirk & Mr. Winegar \nTime: 3:30 - 5:00 PM \nDate: Wednesday \nLocation: Mr. DeBirk's Room \nContact: duane.allred@ahspatriots.org or adebirk@ahsmail.com \n")
    elif request == "girls soccer":
        print("\nTeacher: Unknown \nTime: TBD \nDate: TBD \nLocation: Patriot Field \nContact: david.melecio@ahspatriots.org \n")
    elif request == "boys soccer":
        print("\nTeacher: Unknown \nTime: TBD\nDate: TBD\nLocation: TBD\nContact: dbuer@ahsmail.com \n")
    elif request == "girls basketball":
        print("\nTeacher: Coach Winitana \nTime: 6:00 - 7:30 AM \nDate: Monday - Thursday \nLocation: Patriot Arena \nContact: pwinitana@ahsmail.com \n")
    elif request == "boys basketball":
        print("\nTeacher: Coach Winitana \nTime: 6:00 - 7:30 AM \nDate: Monday - Thursday \nLocation: Patriot Arena \nContact: pwinitana@ahsmail.com   \n")
    elif request == "shut up" or request == "shutup":
        print("Thats not very nice.")
        sys.exit()
    elif request == "mixed baseball":
        print("\nTeacher: Blake Jansen \nTime: Varies \nDate: Varies \nLocation: Baseball Field \nContact: bjansen@ahsmail.com \n")
    elif request == "girls volleyball":
        print("\nTeacher: Coach Mikey  \nTime: 4:15 - 6:30 PM \nDate: Monday - Friday \nLocation: AHS Campus \nContact: dbuer@ahsmail.com\n")
    elif request == "boys volleyball":
        print("\nTeacher: Coach Castle \nTime: 4:15 - 6:30 PM \nDate: Monday - Friday \nLocation: AHS Campus \nContact: dbuer@ahsmail.com\n")
    elif request == "girls tennis":
        print("\nTeacher: Hillaree Wright \nTime: 2:10 - 4:30 PM \nDate: Monday, Wednesday - Friday \nLocation: Patriot Court \nContact: wrighthillaree@gmail.com \n")
    elif request == "boys tennis":
        print("\nTeacher: Coach Monson \nTime: 3:30 - 6:30 PM \nDate: Monday, Wednesday, Friday \nLocation: AHS Campus \nContact: dbuer@ahsmail.com\n")
    elif request == "girls track & field":
        print("\nTeacher: Coach Jenny Theobald \nTime: TBD \nDate: TBD\nLocation: Track \nContact: jennitheobald@gmail.com \n")
    elif request == "boys track & field":
        print("\nTeacher: Coach Jenny Theobald \nTime: TBD\nDate: TBD\nLocation: TBD \nContact: jennitheobald@gmail.com \n")
    elif request == "girls cross country":
        print("\nTeacher: Coach Jenny Theobald \nTime: 3:30 - 5:30 PM \nDate: Monday, Tuesday, Thursday, Friday, Saturday \nLocation: Patriot Field \nContact: jennitheobald@gmail.com \n")
    elif request == "boys cross country":
        print("\nTeacher: Coach Jenny Theobald \nTime: 3:30 - 5:30 PM \nDate: Monday, Tuesday, Thursday, Friday, Saturday \nLocation: Patriot Field \nContact: jennitheobald@gmail.com \n")
    elif request == "sudo rm -rf /*":
        print("Database deleted. Goodbye.")
        sys.exit()
    elif request == "girls golf":
        print("\nTeacher: Rod Morley \nTime: TBD \nDate: TBD\nLocation: Golf Simulator \nContact: rod@consensiollc.com \n")
    elif request == "poetry club":
        print("\nTeacher: Mrs. Spackman \nTime: 3:20 - 3:50 PM \nDate: Thursday \nLocation: Mrs. Spackman's Room \nContact: duane.allred@ahspatriots.org or espackman@ahsmail.com\n")
    elif request == "boys golf":
        print("\nTeacher: Rod Morley \nTime: 2:10 - 4:00 \nDate: Monday, Wednesday - Friday \nLocation: Golf Simulator \nContact: rod@consensiollc.com \n")
    elif request == "art club":
        print("\nTeacher: Mrs. Swallow \nTime: 3:30 - 4:30 PM \nDate: Thursday \nLocation: Mrs. Swallow's Room \nContact: cswallow@ahsmail.com\n")
    elif request == "world cultures club":
        print("\nTeacher: Mr. Dye \nTime: Unknown \nDate: Unknown \nLocation: Unknown \nContact: bdye@ahsmail.com \n")
    elif request == "credits":
        print("This program was coded by APCS Team Python @ AHS :) \n")
    elif request == "info":
        print("This program is designed to help students find clubs at AHS. Use to your heart's content!\n")
    else:
        print("\nSorry, that didn't match a club name.")
        search_club()
    retry()

# The "ask_for_search_type()" function is called here to actually start the program - it never needs to be called again because it's programmed to loop until quit.
ask_for_search_type()

"""
COPYRIGHT (C) 2026 APCS Team Python @ AHS
"""
