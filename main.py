#!/usr/bin/env python3

import random   # Calls the 'random' function
import math     # Calls the 'math' function

xcount = 0      # Sets the count used for how many passphrases will be generated to 0.

# Provides initial context to the user to explain the purpose of the script.
print ("\n\nIn order to prevent account compromise, a strong password should be used. A \nnumber of variables can be used to determine password strength. This script \nevaluates the strength of a user-provided password based on entropy (number, \nfrequency, and type of characters) and checks the password against a file with \naround a million of the most commonly used passwords. Once the strength of the \npassword has been evaluated, you will have the opportunity some easy to \nremember passphrases.\n\n")
upwd = input("Enter the password you would like to check: ")    # Gets the user-generated password.

def calculate_password_entropy(upwd):
   """Calculates the entropy of a upwd.
   Args:
       upwd: The user-defined password to calculate the entropy for.
   Returns:
       The entropy of the password."""

   # Calculate the frequency of each character in the upwd
   char_counts = {}         # Creates an empty dictionary called char_counts. This dictionary will be used to store the counts of each character in the password.
   for char in upwd:        # Iterates through each character in the string stored in the variable upwd, which holds the user generated password.
       char_counts[char] = char_counts.get(char, 0) + 1 # Accounts for characters that haven't been encountered before adds it to the dictionary. If it has been encountered before, adds 1 to the count for each existing
    
    # Calculate the total number of characters in the password.
   total_chars = len(upwd)

   # Calculate the entropy of the password.
   entropy = 0  # Initialize entropy to 0.
   for count in char_counts.values():       # Calculate entropy for each character
       probability = count / total_chars    # Calculate the probability of the character
       entropy -= probability * math.log2(probability)  # Calculate the character's contribution to entropy
   return entropy # Returns the variable from the function

def check_password_in_file(upwd):
    """Checks if a user-inputted password is present in a given file."""
    with open("common_passwords.txt", 'r') as file:     # Opens the common passwords text file for reading.
        common_passwords = file.read().splitlines()     # Read passwords into a list
    if upwd in common_passwords:        # Checks to see if the user-generated password is in the common passwords text file.
        commonpwd = -5                  # If yes, set common password variable to -5 (this makes certain the score is negative)
    else:                               # If the user-generated password is *not* in the file of common passwords...
        commonpwd = 0                   # if not, set the common password variable to 0, insuring this does not impact entropy.
    return commonpwd                    # Returns the value of 'common password' so that it can be used in the rest of the program.


def get_word(file):
    """# Gets a random line from the appropriate text file."""
    with open (file, 'r') as f:                 # Opens the wordlist file assigned to the variable 'file' in patterns for reading and gives it an alias of 'f' and makes certain it closes even if there's an exception.
        word = next(f)                          # Reads the first line of the file and stores it in the variable word.
        for i, line in enumerate(f):            # Iterates through the remaining lines of the file, keeping track of the line number i.
            randomLine = random.randint(0, i)   # Generates a random integer between 0 and the current line number i.
            if randomLine == 0:                 # Checks if the random number is 0.
                word = line.strip()             # If the random line number is 0, updates the word variable with the current line, removing any leading or trailing whitespace.
    return word                                 # Returns the randomly selected value of the word variable

commonpwd = check_password_in_file(upwd)                # Brings the commonpwd variable out of the function
entropy = round(calculate_password_entropy(upwd), 2)    # Brings the entropy variable out of the function and rounds it to two decimal places.
pwdscore = round(float(entropy) + int(commonpwd),2)     # Calculates the password score by adding entropy and common password score

""" The following lines are used for debugging.
print(f"Password: {upwd}, Common: {commonpwd}, Entropy: {entropy:.2f}")  # Formats the variables within a string and presents them to the user.
print("Final password score: ", pwdscore)
"""

if pwdscore < 0:    # if combined password score is less than zero, let the user know that their password was in the common passwords list.
    print("Your password was found in a list of the top one million most common passwords.\n")
elif pwdscore < 2:  # if combined password score is less than two, let the user know that their password is extremely weak (entering 'a' or similar gets this result)
    print("Your password is quite weak, likely due to repeated characters or not using enough character types.\n")
elif pwdscore < 3:  # if combined password score is less than two, let the user know that their password is weak (bcbcbc1111 or similar would get this result)
    print("Your password is weak, likely due to repeated characters or not using enough character types.\n")
elif pwdscore < 4:  # if combined password score is less than two, let the user know that their password is moderately strong (a password like jackrabbit9876 might get this result)
    print("Your password is of moderate strength, something that can be helped with added complexity.\n")
elif pwdscore < 5:  # if combined password score is less than two, let the user know that their password is strong (a password like GitMaster1944! and the generated passphrases from this program would get this response). 
    print("Your password is strong, but may not be that easy to remember.\n")
else:               # If password score is higher than 5, it's a very strong password. Very few passwords hit this number.
    print("Your password is extremely strong. Congratulations! A passphrase may make it easier for you to remember.\n")

# Provides information to the user about passphrases and why they're used.
print ("A strong password is instrumental in security. One way to have a strong,\nmemorable password is to use a passphrase instead. A passphrase is a group of\nwords that are joined by a special character like '.', '-', or '_'. While a\npassphrase can contain random words, using natural structure to build memorable\nsentence can help. This script creates memorable passphrases with a four-digit\nnumber for additional strength.\n")
# Sets up the possibilities for how many passphrases can be created and adds them to a list. There is a better way to do this, but there were debugging issues.
xnumlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
# Asks the user how many passphrases should be created and stores the number as a string in a variable.
xnum = input ("How many passphrases would you like to produce? Enter an integer between 1 and 20, anything else to quit: ")
if xnum in xnumlist:    # Checks to make certain the 'number' provided by the user is in the list. If yes, continues. If not, ends the program.
    # Creates a list of separators to compare user input against.
    seplist = ["-", "_", "/", "!", ".", "^", "&", ",", "\\", "|", "@", "#", "$", "%", "*", "=", "+", "~"]
    # Takes the input of the user to choose a separator.
    sep = input("If you would like to choose a separator, choose from one of the following. Otherwise, press enter:\n - _ / ! . ^ & , \\ | @ # $ % * = + ~ \nWhat separator would you like to use? ")
    if sep in seplist:              # Checks if user inputed separator is in the list of available characters.
        sep = sep                   # Leaves the variable as-is when the character is present.
        print()                     # Adds a blank line for readability.
    else:                           # If the user input is not in the list of choices...
        sep = random.choice(seplist)    # Assigns a random character from the list to the separator variable.
        print("\nYour random separator is:", sep, "\n") # Informs the user of the random character chosen as a separator.
else:   # If the user did not choose a number from the list of possible choices for how many passphrases should be created...
    pass    # Passes to the exception.
try:
    while xcount < int(xnum):    # Sets up the while loop so that the script iterates through 5 passphrases.
        adj = 'adjectives.txt'                  # Assigns the list of adjectives to the variable 'adj'
        adv = 'adverbs.txt'                     # Assigns the list of adverbs to the variable 'adv'
        name = 'names.txt'                      # Assigns the list of proper names to the variable 'name'
        noun = 'nouns.txt'                      # Assigns the list of nouns to the variable 'noun'
        prep = 'prepositions.txt'               # Assigns the list of prepositions to the variable 'prep'
        pverb = 'plural-verbs.txt'              # Assigns the list of plural verbs to the variable 'pverb'
        sverb = 'singular-verbs.txt'            # Assigns the list of singular verbs to the variable 'sverb'
        num = str(random.randint(0000,9999))    # Chooses a random number from 0 to 9999 and turns it into a string for appending to the passphrase

        # Creates the pattern for determining sentence structure
        patterns = [
            ['a', 'n', 'v', 'd', 'p', 'm', 'u' ],   # adjective noun pluralVerb adverb preposition name number
            ['m', 's', 'd', 'p', 'n', 'u' ],        # name singularVerb adverb preposition noun number
            ['m', 's', 'a', 'n', 'u' ],             # name singularVerb adverb noun number
            ['m', 's', 'n', 'u']                    # name singularVerb noun number
        ]

        # Iterates through each pattern to create the proper order of words and adds it to the phrase variable.
        phrase = []                             # Creates an empty list to store the generated phrase.
        for p in random.choice(patterns):       # Randomly selects one pattern from a list called patterns and iterates over its characters.
            p = p                               # Initializes the variable that will hold the generated word.
            if p == 'a':                        # If the next item in the pattern is an adjective...
                phrase.append(get_word(adj))    # Calls the get_word function to retrieve a random word from the adjectives.txt text file.
            elif p == 'd':                      # If the next item in the pattern is an adverb...
                phrase.append(get_word(adv))    # Calls the get_word function to retrieve a random word from the adverbs.txt text file.
            elif p == 'm':                      # If the next item in the pattern is a name...
                phrase.append(get_word(name))   # Calls the get_word function to retrieve a random word from the names.txt text file.
            elif p == 'n':                      # If the next item in the pattern is a noun...
                phrase.append(get_word(noun))   # Calls the get_word function to retrieve a random word from the nouns.txt text file.
            elif p == 'p':                      # If the next item in the pattern is a preposition...
                phrase.append(get_word(prep))   # Calls the get_word function to retrieve a random word from the prepositions.txt text file.
            elif p == 's':                      # If the next item in the pattern is a singular verb...
                phrase.append(get_word(sverb))  # Calls the get_word function to retrieve a random word from the singular-verbs.txt text file.
            elif p == 'v':                      # If the next item in the pattern is a plural verb...
                phrase.append(get_word(pverb))  # Calls the get_word function to retrieve a random word from the verbs.txt text file.
            elif p == 'u':                      # If the next item in the pattern is a number...
                phrase.append(num)              # Appends the num variable to the phrase.
            else:                               # If the pattern has been fully iterated through...
                pass                            # Does nothing since the pattern has been fully iterated through so that the program can move to the next bit of code.

        phrase = sep.join(phrase)       # Creates the formatting for the passphrase.
        xcount += 1                     # Adds 1 to the count of xcount for displaying the proper number of passphrases.
        print('\t{}'.format(phrase))    # Prints the passphrase.
    # Lets the user know the program has ended and says how many passphrases were created.
    print("\nDone! You created", xnum, "memorable passphrases with Madlibs Passphrases!\n")
except:
    print("\nDone!\n")
