# data.py
# Ultimate Movie Database: Bollywood + Hollywood + South + Anime

MOVIES = [
    # A
    "Avatar", "Avengers Endgame", "Avengers Infinity War", "Alien", "Annabelle", "Airlift", "Article 15", "Andhadhun", "Aashiqui 2", "Aladdin", "Andaz Apna Apna", "Anjaana Anjaani", "A Wednesday", "Aamir", "Agneepath", "Animal", "Akira", "Attack", "Azhar", "Ankur Arora Murder Case", "Angrezi Medium", "Ant Man", "Aquaman", "Assassins Creed", "A Quiet Place", "After Earth", "Alita Battle Angel", "Attack on Titan", "Ashoka the Great", "Anand", "Angoor", "Aradhana", "Amar Akbar Anthony", "Arjun Reddy", "Aarya", "A Wednesday", "Ahimsa", "Atrangi Re", "Ajnabee", "Aapko Pehle Bhi Kahin Dekha Hai", "Ankush", "Anari", "Anari No 1",

    # B
    "Batman Begins", "Black Panther", "Bajrangi Bhaijaan", "Bajirao Mastani", "Barfi", "Bahubali The Beginning", "Bahubali 2", "Brahmastra", "Baby", "Baaghi", "Baaghi 2", "Baaghi 3", "Blade Runner", "Bodyguard", "Bang Bang", "Bhool Bhulaiyaa", "Badhaai Ho", "Bharat", "Bhool Bhulaiyaa 2", "Baadshah", "Bhoot", "Blue", "Bodyguard", "Badlapur", "Blade", "Ben-Hur", "Blood Diamond", "Break Ke Baad", "Baby Driver", "Bastard", "Baar Baar Dekho", "Bala", "Bombay Talkies", "Batti Gul Meter Chalu", "Batla House", "Bhavesh Joshi Superhero", "Blackmail", "Brothers", "Bhavesh Joshi", "Beast", "Bombay", "Border", "Bhaag Milkha Bhaag", "Boxer", "Boss", "Black", "Bunty Aur Babli", "Bunty Aur Babli 2", "Business Man", "Bejawada", "Balupu", "Bharat Ane Nenu",

    # C
    "Captain America Civil War", "Captain America Winter Soldier", "Coco", "Conjuring", "Chennai Express", "Chak De India", "Cinderella", "Catch Me If You Can", "Casino", "Cast Away", "Coolie No 1", "Chandni Chowk To China", "Cocktail", "Chhichhore", "CityLights", "Commando", "Cheeni Kum", "Chalte Chalte", "Carry On Jatta", "Chup", "Champion", "Captain Phillips", "Cellular", "Chennai 600028", "Chalo", "Champion Champion", "Criminal", "Chor Nikal Ke Bhaga", "Coolie", "Chehra", "Chhoti Si Baat", "Champion", "Chandni", "Charlie and the Chocolate Factory", "Clash of the Titans", "Constantine", "Conan the Barbarian", "Cinderella Man", "Chicago",

    # D
    "Dark Knight", "Dark Knight Rises", "Drishyam", "Drishyam 2", "Dangal", "Dilwale Dulhania Le Jayenge", "Dil Chahta Hai", "Don", "Don 2", "Dhoom", "Dhoom 2", "Dhoom 3", "Devdas", "Doctor Strange", "Deadpool", "Django Unchained", "Dabangg", "Dabangg 2", "Dabangg 3", "Dilwale", "Dear Zindagi", "Dostana", "Delhi Belly", "Dunki", "Dream Girl", "Drive", "Deewaar", "Dil Se", "Dil To Pagal Hai", "Dil Hai Ke Manta Nahin", "Daawat E Ishq", "Desi Boyz", "Double Dhamaal", "Dil Maange More", "Darling", "Dosti", "Dushman", "Devdas", "Desperate Measures", "Dragonball Evolution", "Dune", "Deadpool 2", "Dumb and Dumber", "Die Hard", "Dasara", "DJ Tillu", "Dangerous Khiladi", "Dilwale Dulhania Le Jayenge", "Dilwale", "Devdas",

    # E
    "Eega", "Entertainment", "Exorcist", "Enthiran", "Edge of Tomorrow", "English Vinglish", "Ek Tha Tiger", "Ek Villain", "Ek Main Aur Ekk Tu", "Extraordinary Measures", "Ek Chhotisi Love Story", "Elite", "Escape Plan", "Erin Brockovich", "Eight Mile", "Enemy", "Ek Tha Raja", "Ek Doctor Ki Maut", "Everything Everywhere All At Once", "El Camino", "Eagle", "Endgame", "Evil Dead", "Extraction", "Enola Holmes", "Eternals", "Encanto", "Eddie the Eagle", "Empire Strikes Back", "Entourage", "Enchanted",

    # F
    "Forrest Gump", "Fast and Furious", "Furious 7", "Fast Five", "Finding Nemo", "Frozen", "Frozen 2", "Fan", "Fifty Shades of Grey", "Fanaa", "Fukrey", "Fukrey Returns", "Fight Club", "Fantastic Beasts", "Fantastic Four", "Fireproof", "Field of Dreams", "Final Destination", "First Blood", "Fly Away", "Fida", "Family", "Faltu", "Free Guy", "Fitoor", "Falaknuma Das", "Fidaa", "F2 Fun and Frustration", "F3 Fun and Frustration", "Freeway", "Footloose", "Flight", "Fright Night", "Fright Night 2", "Fist of Fury",

    # G
    "Gladiator", "Gandhi", "Gangs of Wasseypur", "Gully Boy", "Guardians of the Galaxy", "Gravity", "Green Mile", "Golmaal", "Golmaal Again", "Gangubai Kathiawadi", "Ghayal", "Gadar", "Gadar 2", "Gangs of Wasseypur 2", "Gippi", "Good Newwz", "Gunday", "Gangster", "Garam Masala", "God Tussi Great Ho", "Golmaal Fun Unlimited", "Ghulam", "Ghost", "Grand Masti", "Great Grand Masti", "Go Goa Gone", "Gangs of London", "Godzilla", "Get Out", "Green Lantern", "Ghostbusters", "Gentlemen", "Geetha Govindam", "Guntur Talkies", "Goodachari", "Geetha",

    # H
    "Harry Potter Sorcerers Stone", "Harry Potter Chamber Secrets", "Harry Potter Prisoner Azkaban", "Harry Potter Goblet Fire", "Harry Potter Order Phoenix", "Harry Potter Half Blood Prince", "Harry Potter Deathly Hallows", "Home Alone", "Hunger Games", "Housefull", "Housefull 2", "Housefull 3", "Housefull 4", "Heropanti", "Hero", "Hum", "Hera Pheri", "Hulchul", "Hungama", "Hey Ram", "Haider", "Haseena Maan Jaayegi", "Humpty Sharma Ki Dulhania", "Happy New Year", "Hate Story", "Hate Story 2", "Hate Story 3", "Hate Story 4", "Holiday", "Heroine", "Haqeeqat", "Hum Saath Saath Hain", "Hum Tum", "Hum Dil De Chuke Sanam", "Hello Brother", "Hit", "Honest", "Honesty", "Homecoming", "Half Girlfriend", "Hera Pheri 3", "Hanuman", "Hulk", "Hollywood", "Hostel", "How I Met Your Mother",

    # I
    "Inception", "Interstellar", "Iron Man", "Iron Man 2", "Iron Man 3", "Independence Day", "Insidious", "Inside Out", "India", "I Hate Luv Storys", "Ishq Vishk", "Iqbal", "Ikiru", "Incredibles", "Incredibles 2", "Identity", "In Time", "In the Line of Fire", "Inglourious Basterds", "In Good Company", "Ice Age", "Idiots", "Ittefaq", "Ishqiya", "Islands in the Stream", "Indra", "Insaan", "Ishq", "Inteha", "India Lockdown", "Inception", "Intestines", "Ishqzaade", "Ishq Actually", "Indian", "It", "It Chapter Two", "In the Heights", "Invisible Man", "Infinity War",

    # J
    "Joker", "Jumanji", "Jaws", "Jab We Met", "Jawan", "Jodha Akbar", "Jurassic Park", "Jab Harry Met Sejal", "Jab Tak Hai Jaan", "Jhankaar Beats", "Jazbaa", "Jhms", "Jaan-E-Mann", "Jeet", "Jeetenge Hum", "Jism", "Jism 2", "Johnny Gaddaar", "John Wick", "John Wick 2", "John Wick 3", "Judwaa", "Judwaa 2", "Jungle", "Jungle Book", "Joker 2019", "Joy", "Julius Caesar", "Jugjugg Jeeyo", "Jhund", "Jersey", "Jail", "Junglee", "Jai Ho", "Jazbaa", "Jagame Janthara", "Jil", "Jai Lava Kusa", "Julayi", "Jalsa",

    # K
    "Kabhi Khushi Kabhie Gham", "Kuch Kuch Hota Hai", "Kal Ho Na Ho", "Kabir Singh", "Kantara", "KGF Chapter 1", "KGF Chapter 2", "Kill Bill", "Kingsman", "Kick", "Krish", "Krrish 3", "Lagaan", "Life of Pi", "Kaho Naa Pyaar Hai", "Kabhi Haan Kabhi Naa", "Kaminey", "Karwaan", "Kabul Express", "Kismat Konnection", "Koyla", "Kaabil", "Khichdi", "Khiladi", "Khiladi 786", "Koi Mil Gaya", "Kya Kool Hain Hum", "Kya Super Kool Hain Hum", "Kshanam", "Kaafila", "Kashmir Files", "Karthikeya", "Krishna Cottage", "Kites", "Khiladi 420", "Kismat", "Kick", "Khosla Ka Ghosla", "Kashmir Ki Kali", "Khamoshi", "Khal Nayak", "Karz", "Krishna", "King", "Khakee", "Khalnayak",

    # L
    "Lagaan", "Life of Pi", "La La Land", "Lion King", "Love Aaj Kal", "Lootera", "Lage Raho Munna Bhai", "Lord of the Rings Fellowship", "Lion", "Logan", "Laxmii", "Love Aaj Kal 2", "London Paris New York", "Lunchbox", "Lakshya", "Lover", "Lust Stories", "Life Partner", "London Dreams", "Looteri", "Luv Shuv Tey Chicken Khurana", "Long Live Lagaan", "Last Emperor", "Life is Beautiful", "Loot", "Little", "Leo", "Love Mocktail", "Love Mocktail 2", "Liger", "Legend", "Liar Liar", "Lucy", "Lake Placid",

    # M
    "Mission Impossible", "Mission Impossible Fallout", "Matrix", "Matrix Reloaded", "Matrix Revolutions", "Mardaani", "Munna Bhai MBBS", "Moana", "My Name is Khan", "Mughal E Azam", "Mad Max", "Mad Max Fury Road", "Maleficent", "Mary Kom", "Manjhi The Mountain Man", "Mela", "Masti", "Mumbai Meri Jaan", "Madras Cafe", "Masaan", "M.S. Dhoni", "Madamji", "Mukkabaaz", "Mimi", "Made in China", "Malang", "Mela 2", "Mere Brother Ki Dulhan", "Mere Yaar Ki Shaadi Hai", "Mom", "Mughal-e-Azam", "Mujhse Dosti Karoge", "Munnabhai", "Masaan", "Mukkabaaz", "Mimi", "Malang", "Mela 2", "Mardaani 2", "Mickey Virus", "Meri Pyaari Bindu", "Mumbai Saga", "Maine Pyar Kiya", "Mughal E Azam", "Mughal", "Maine Gandhi Ko Nahin Mara", "Mystery", "Monster", "Madagascar", "Minions", "Maleficent 2",

    # N
    "Night at the Museum", "Neerja", "Notting Hill", "No Time To Die", "Nayak", "Na Tum Jaano Na Hum", "Nayak The Real Hero", "Newton", "No One Killed Jessica", "Nishabd", "Namastey London", "New York", "No Entry", "No Problem", "No Smoking", "Nautanki Saala", "Ninja Assassin", "Now You See Me", "Now You See Me 2", "Nebraska", "Nil Battey Sannata", "Neru", "NH10", "Namaste England", "Nishabdham", "Naqaab", "Nikamma", "Nautanki", "Nautanki Saala", "Nanak Shah Fakir", "Namak Halaal", "Naagin", "Naya Daur", "Naya Zamana", "Neecha Nagar",

    # O
    "Om Shanti Om", "Oppenheimer", "Oldboy", "October", "Ok Jaanu", "Oh My God", "Oye Lucky Lucky Oye", "Once Upon A Time In Mumbai", "Once Upon A Time In Mumbai Dobaara", "Once Upon A Time In America", "Outsourced", "Open Season", "Office Space", "Our Family Wedding", "Outbreak", "One Night At McCools", "Only You", "Out of the Furnace", "Ocean's Eleven", "Ocean's Twelve", "Ocean's Thirteen", "O Brother Where Art Thou", "On the Waterfront", "Ordinary People", "Other Guys", "Omkara", "Okkadu", "Oopiri", "Ong Bak",

    # P
    "Pathaan", "PK", "Padmaavat", "Pirates of the Caribbean", "Pulp Fiction", "Pushpa The Rise", "Pushpa 2", "Pink", "Queen", "Quantum of Solace", "Paan Singh Tomar", "Piku", "Parmanu", "Parzania", "Patiala House", "Pyar Ka Punchnama", "Pyar Ka Punchnama 2", "Panipat", "Prasthanam", "Phir Hera Pheri", "Phata Poster Nikhla Hero", "Page 3", "Partner", "Professor", "Pyaar Impossible", "Pyaar Ke Side Effects", "Pyaar To Hona Hi Tha", "Prem Granth", "Prem Ratan Dhan Payo", "Popcorn", "Penguins of Madagascar", "Pari", "Paltan", "Parinda", "Parinda", "Paris", "Parzania", "Panipat", "Project K", "Pokiri", "Parijatham", "Premam", "Pelli Choopulu", "Phir Hera Pheri",

    # Q
    "Qayamat Se Qayamat Tak", "Queen of Katwe", "Quantum of Solace", "Quest for Camelot", "Quarantine", "Quick Change", "Quills", "Quiz Show", "Quo Vadis", "Question Mark", "Qissa", "Quicksand", "Quatermass",

    # R
    "Rockstar", "Rang De Basanti", "Raazi", "Raees", "Rambo", "Rocky", "RRR", "Robot", "Ready", "Race", "Race 2", "Race 3", "Raid", "Raja Hindustani", "Raja Natwarlal", "Raja Ki Aayegi Baraat", "Rangoon", "R...Rajkumar", "Rustom", "Rab Ne Bana Di Jodi", "Rehnaa Hai Terre Dil Mein", "Raat", "Raja", "Raja Hindustani", "Rocky Handsome", "Rann", "Rocket Singh Salesman", "Roja", "Rog", "Run", "Rudaali", "Rush", "Rush Hour", "Rush Hour 2", "Rush Hour 3", "Robot 2.0", "Romeo Akbar Walter", "Rocky 2", "Rocky 3", "Rocky 4", "Rustom", "Red", "Ra One", "Roohi", "Radhe", "Raksha Bandhan", "Ratsasan", "Rangasthalam", "Rangula Ratnam", "Ratsasan",

    # S
    "Sholay", "Singham", "Singham Returns", "Simmba", "Sooryavanshi", "Sultan", "Stree", "Sanju", "Swades", "Shutter Island", "Skyfall", "Spider Man Homecoming", "Spider Man No Way Home", "Spider Man Far From Home", "Saving Private Ryan", "Scream", "Satyameva Jayate", "Special 26", "Swades", "Sarkar", "Sarkar 2", "Sarkar 3", "Sonu Ke Titu Ki Sweety", "Sonchiriya", "Super 30", "Shubh Mangal Saavdhan", "Saheb Biwi Aur Gangster", "Saheb Biwi Aur Gangster Returns", "Saand Ki Aankh", "Shubh Mangal Zyada Saavdhan", "Sanam Teri Kasam", "Sadak", "Sadak 2", "Shararat", "Shaadi Se Pehle", "Shaadi Ke Side Effects", "Shaadi Mein Zaroor Aana", "Student of the Year", "Student of the Year 2", "Sui Dhaaga", "Suryavanshi", "Surya", "Satya", "Saudagar", "Sir", "Sarbjit", "Sanam Teri Kasam", "Silsila", "Satyameva Jayate", "Shiva", "Shiva The Superhero", "Shivaay", "Surya The Soldier", "Saaho", "Sarileru Neekevvaru", "Sita Ramam", "Superstar",

    # T
    "Titanic", "Terminator", "Terminator 2", "The Avengers", "Thor", "Thor Ragnarok", "Taare Zameen Par", "Tamasha", "Top Gun Maverick", "Twilight", "Toy Story", "Uri The Surgical Strike", "Up", "Us", "Three Idiots", "Talaash", "Tashan", "Tanhaji", "Tees Maar Khan", "Tum Bin", "Tum Bin 2", "Tumhari Sulu", "Tu Chor Main Sipahi", "Tum Mile", "Tum Milo Toh Sahi", "Tumhari Sulu", "Twilight Saga New Moon", "Twilight Saga Eclipse", "Twilight Saga Breaking Dawn", "The Lion King", "The Jungle Book", "The Sky Is Pink", "The Zoya Factor", "The White Tiger", "The Kashmir Files", "The Family Man", "The Trial", "Total Dhamaal", "Thappad", "Tuesdays and Fridays", "Tokyo Trial", "Tanu Weds Manu", "Tanu Weds Manu Returns", "Tashan", "Te3n", "Table No 21", "Taxi No 9211", "Tere Naam", "Tera Intezaar", "Tera Chehra", "Teesri Manzil", "Time Machine", "Teenage Mutant Ninja Turtles", "Tenet",

    # U
    "Uri The Surgical Strike", "Up", "Us", "Udaan", "Ugly", "Ugly Aur Pagli", "Udayananu Tharam", "Unfreedom", "United Six", "Ugly", "Udaan", "U Turn", "Uttama Villain", "Udaan", "Uncharted", "Upgrade", "Unstoppable", "United 93", "Up in the Air", "UglyDolls", "Uncut Gems", "Uncle Drew",

    # V
    "Vikram", "Vikram Vedha", "Veer Zara", "Vivah", "War", "Whiplash", "Wolf of Wall Street", "Wonder Woman", "Wake Up Sid", "Veer-Zaara", "Vicky Donor", "Veer", "Veerappan", "Vettai", "Vikramarkudu", "Vishwaroopam", "Vishwaroopam 2", "Varanasi A Love Story", "Vastadu Naa Raju", "Vedam", "Vidya", "Viraasat", "Vikram", "Villain", "Village Rockstars", "Vinnaithaandi Varuvaaya", "Vedha", "Vikrant Rona", "Vaccine", "Vastu Shastra", "Vande Mataram", "Vande Mataram 2", "Vardi", "Vajra", "Vachitbad",

    # W
    "War", "Whiplash", "Wolf of Wall Street", "Wonder Woman", "Wake Up Sid", "Welcome", "Welcome Back", "Wanted", "Wasseypur", "Wedding Pullav", "What Women Want", "We Are Family", "Waqt The Race Against Time", "Water", "Wanted Dead or Alive", "Watchmen", "Wreck-It Ralph", "Wrong Turn", "Who Am I", "White House Down", "World War Z", "Wazir", "Warrior", "Wedding Season", "Wrestling", "Wild Wild West", "Woman in the Dunes", "Wonder",

    # X
    "X Men", "X Men Origins", "X Men Days of Future Past", "X Men First Class", "X Men Last Stand", "X Men Apocalypse", "X Men Dark Phoenix", "X Ray", "XXx", "XXx State of the Union", "XXx Return of Xander Cage",

    # Y
    "Yeh Jawaani Hai Deewani", "Youngistaan", "Zindagi Na Milegi Dobara", "Yuva", "Yes Boss", "Yeh Dil", "Yeh Dillagi", "Yaadien", "Yatra", "Yaraana", "Yamla Pagla Deewana", "Yaadein", "Yaariyan", "Yeh Hai Jalwa", "Yeh Khula Aasmaan", "Yuvvraaj", "Yeh Silli Zindagi", "Yakeen", "Yeh Jo Mohabbat Hai", "Yuva",

    # Z
    "Zindagi Na Milegi Dobara", "Zero", "Zootopia", "Zakhm", "Zinda", "Zanjeer", "Zinda Bhaag", "Zokkomon", "Zilla Ghaziabad", "Zoom", "Zubeidaa", "Zor Ka Jhatka", "Zameen", "Zakhm", "Zor Lagaa Ke... Haiya", "Zulmi", "Zilla", "Zindagi Na Milegi Dobara", "Zindagi 50 50", "Zombie Reddy",

    # Edge Cases & Specific Requests
    "Godfather", "Tere Naam", "Dil", "Hum Aapke Hain Koun", "Deewana", "Dhadkan", "Ghajini", "Ajay", "Khiladi 420", "With Love", "One Two Three", "Tik Tik Tik", "Half Girlfriend", "Jimmy", "Badrinath", "Warning", "Tubelight", "Thank You Dear", "Love in Vietnam", "Karate Kid", "Shahid", "My Fault", "Your Fault", "Our Fault", "Teri Baaton Mein Aisa Uljha Jiya", "Love Khichdi", "Khiladi 786", "Boss", "Mafia", "School Boy", "Singh Is Kinng", "Sky Force", "Andolan", "Yamla Pagla Deewana", "Raaz", "Raaz 2", "Sanam Re", "Azhar", "Sanam Re Part 2", "MS Dhoni The Untold Story", "Hate Story", "Sanam Teri Kasam", "Imtihan", "Maharaja", "Happy New Year", "Island City", "Attack", "Ashoka", "Akira", "A Wednesday", "Andhadhun", "Badla", "Baby", "Drishyam", "Drishyam 2", "Article 15", "Mulk", "Manto", "Sir", "Super 30", "Chichhore", "Dangal", "Pink", "Mardaani", "NH10", "Piku", "English Vinglish", "Tumhari Sulu", "Queen", "Neerja", "Mary Kom", "Paan Singh Tomar", "Bhaag Milkha Bhaag", "Shahid", "M.S. Dhoni", "Sanju", "Manjhi", "Neerja", "Sarbjit"
]

# --- FAST LOOKUP SET (case-insensitive) ---
MOVIE_SET = set(m.lower() for m in MOVIES)

def group_by_letter():
    grouped = {}
    for m in MOVIES:
        letter = m.strip()[0].upper()
        grouped.setdefault(letter, []).append(m)
    return grouped

def is_valid_movie(name):
    return name.strip().lower() in MOVIE_SET
