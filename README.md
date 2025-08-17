# MadlibsPassphrases

The point of this python script is to evaluate the strength of a user-generated password, then offer easier to remember passphrases that use natural sentence structure to make them memorable.

The program uses two functions to determine password strength: entropy and presence on a list of around a million commonly used passwords. Entropy is determined based on the length of the password, the frequency of characters used, and the probability of each character’s appearance. This is often a better way to determine password strength than through simple character type recognition (upper and lower-case, numeric, special characters). The common passwords list was found online and had nearly one million passwords. I added a few that I encountered in my testing that I know are also common, such as some variations on ‘password123’ and similar.

Natural sentences, like “Justin runs happily toward cats” are much easier to remember than either passwords (like “ardmaiden44961!”) or passphrases that use random words (like “Found-Run-Potato-Blue”). One of the ways to promote password complexity is to create passphrases with special characters and numbers, where the number is fairly short and the passphrase itself is memorable.

The program uses seven different wordlists, each containing a list of words that match particular parts of speech so that natural-sounding sentences can be made.

•	Adjectives: Words that describe nouns (such as fast, long, quiet, orange)

•	Adverbs: Adjectives that describe verbs (such as quickly, shortly, softly, prettily)

•	Names: Proper nouns (such as John, Mary, Lee, Tristan, Blake)

•	Nouns: Things or ideas (such as bananas, kidneys, reports, ideas, threats) – all are plural.

•	Plural verbs: Action words that match a plural noun (run, dance, function, apprehend)

•	Prepositions: Words that describe a relationship between a noun and a verb (onto, toward, around, through)

•	Singular verbs: Action words that match a singular noun (hates, dresses, handles, presides)

The program uses patterns to determine sentence structure. Language is made up of many different kinds of sentences. For simplicity, the patterns in the program only use the seven parts of speech listed above. This provides a finite number of patterns, but it should provide enough flexibility. Patterns can be added, but any additional parts of speech (singular nouns, articles, conjunctions) will need to be added as a separate word list. Articles and conjunctions are not recommended, as there are not many in the English language, and the program should provide an abundance of combinations, not be limited to only a few of any word type. Adding additional parts of speech might also begin to make the passphrases too complex and too long. Some systems restrict the length of a password, so too much complexity can become a liability.

Patterns are chosen randomly, and when a user tells the program how many passphrases they want created, it will iterate through random patterns in a list to provide a variety of passphrases, generally from three to five words long, using a separator between each word and appending a number at the end.

•	Mia-Scrapes-Crafts-1188

•	Austin\Shelters\Pallidly\Beside\Switches\1003

•	Chase_Earns_Showers_9426

•	Spotted.Mixes.Renovate.Northeasterly.But.Trevor.4212

•	Sybil&Utters&Pleasantly&Regarding&Rivers&6840

•	Abe!Strikes!Briefs!4955

•	Brainy^Safes^Scope^Selfishly^Over^Eloise^8195

•	Rotating+Hunts+Hesitate+Formally+Closeby+Juanita+2118

•	Finn\*Does\*Unhealthily\*Considering\*Maps\*400

•	Sonia|Mutates|Squiggly|Friends|7288

•	Pia\`Receives\`Emotionlessly\`Till\`Emphases\`7588

•	Mordecai\~Jousts\~Sparkling\~Bids\~3165

•	Dana=Scales=Uncomfortably=Aboard=Detectives=1901

•	Boundless@Armies@Procure@Gaspingly@Opposite@Ryan@9798

•	Sergei$Enters$Lungs$4577

•	Sniveling#Angles#Bust#Accidentally#Save#Kylie#6773

•	Olympia,Needles,Fondly,Against,Coyotes,5171

•	Anita%Hustles%Proper%Initiatives%224


Users are also able to choose a separator from a list of 18 special characters. Should they enter anything other than one of the choices in the string, the program will choose one randomly to apply to all passphrases created.

This will be an ongoing project that will have some of the following worked on as time goes by:

•	Better exception handling. Some workarounds were done for expediency.

•	Code optimization. Defined functions will be split off into their own file.

•	Better handling of the choice of how many passphrases should be created.

•	Revised text presented to the user for education.

•	Adding a few more pattern types.

•	Potentially adjusting the numbers created to append to the passphrases to exclude anything lower than 4 digits.

•	Allowing truly random separators, so that each generated passphrase uses a different separator unless the user chooses one specifically.

•	Entropy, entropy, entropy!!!


 <img src="https://i.imgur.com/2lKlK5Y.png" alt="Output of code when a common password is entered.">

 
 <img src="https://i.imgur.com/hsHnols.png" alt="Output of code when moderately strong password is entered.">


 <img src="https://i.imgur.com/w0aGyIM.png" alt="Output of code when moderately strong password is entered.">


 <img src="https://i.imgur.com/Jwo0Fhw.png" alt="Error handling.">
