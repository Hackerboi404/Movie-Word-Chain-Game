# data.py
# Expanded Dataset ensuring >= 5 movies per letter (A-Z)

MOVIES = [
    # A
    "Avatar", "Avengers Endgame", "Avengers Infinity War", "Alien", "Annabelle", "Airlift", "Article 15", "Andhadhun", "Aashiqui 2", "Aladdin", "Andaz Apna Apna", "Anjaana Anjaani", "A Wednesday", "Aamir", "Akira", "Agneepath", "Anaarkali of Aarah", "Animal", "Ankhon Dekhi", "Azaad",
    
    # B
    "Batman Begins", "Black Panther", "Bajrangi Bhaijaan", "Bajirao Mastani", "Barfi", "Bahubali The Beginning", "Bahubali 2", "Brahmastra", "Baby", "Baaghi", "Baaghi 2", "Baaghi 3", "Blade Runner", "Bodyguard", "Bang Bang", "Bhool Bhulaiyaa", "Badhaai Ho", "Bharat", "Batti Gul Meter Chalu", "Batla House", "Bhavesh Joshi Superhero", "Blackmail", "Bhavesh Joshi", "Bombay Talkies", "Badlapur", "Blood Diamond", "Break Ke Baad", "Badshaah",
    
    # C
    "Captain America Civil War", "Captain America Winter Soldier", "Coco", "Conjuring", "Chennai Express", "Chak De India", "Cinderella", "Catch Me If You Can", "Casino", "Cast Away", "Coolie No 1", "Chandni Chowk To China", "Cocktail", "Chhichhore", "Chennai 600028", "CityLights", "Commando", "Cheeni Kum", "Chalte Chalte", "Carry On Jatta", "Chhello Divas", "Chup", "Champion", "Chandni", "Captain Phillips", "Cellular",
    
    # D
    "Dark Knight", "Dark Knight Rises", "Drishyam", "Drishyam 2", "Dangal", "Dilwale Dulhania Le Jayenge", "Dil Chahta Hai", "Don", "Don 2", "Dhoom", "Dhoom 2", "Dhoom 3", "Devdas", "Doctor Strange", "Deadpool", "Django Unchained", "Dabangg", "Dabangg 2", "Dabangg 3", "Dilwale", "Dear Zindagi", "Dostana", "Delhi Belly", "Dunki", "Dream Girl", "Drive", "Deewaar", "Dil Se", "Dil To Pagal Hai", "Dil Hai Ke Manta Nahin", "Daawat E Ishq", "Desi Boyz", "Double Dhamaal", "Dil Maange More",
    
    # E
    "Eega", "E T", "Exorcist", "Enthiran", "Edge of Tomorrow", "English Vinglish", "Ek Tha Tiger", "Ek Villain", "Ek Main Aur Ekk Tu", "Extraordinary Measures", "Ek Chhotisi Love Story", "English Babu Desi Mem", "Elite", "Escape Plan", "Erin Brockovich", "Eight Mile", "Enemy", "Ek Tha Raja", "Ek Doctor Ki Maut", "Everything Everywhere All At Once",
    
    # F
    "Forrest Gump", "Fast and Furious", "Furious 7", "Fast Five", "Finding Nemo", "Frozen", "Frozen 2", "Fan", "Fifty Shades of Grey", "Fanaa", "Fukrey", "Fukrey Returns", "Fight Club", "Fantastic Beasts", "Fantastic Four", "Fireproof", "Field of Dreams", "Final Destination", "First Blood", "Forrest Gump", "Fly Away", "Fida", "Family", "Faltu", "Free Guy", "Fitoor",
    
    # G
    "Gladiator", "Gandhi", "Gangs of Wasseypur", "Gully Boy", "Guardians of the Galaxy", "Gravity", "Green Mile", "Golmaal", "Golmaal Again", "Gangubai Kathiawadi", "Ghayal", "Gadar", "Gadar 2", "Gangs of Wasseypur 2", "Gippi", "Gippi", "Good Newwz", "Gippi", "Gunday", "Gangster", "Garam Masala", "God Tussi Great Ho", "Golmaal Fun Unlimited", "Ghulam", "Ghost", "Gravity", "Grand Masti", "Great Grand Masti", "Go Goa Gone",
    
    # H
    "Harry Potter Sorcerers Stone", "Harry Potter Chamber Secrets", "Harry Potter Prisoner Azkaban", "Harry Potter Goblet Fire", "Harry Potter Order Phoenix", "Harry Potter Half Blood Prince", "Harry Potter Deathly Hallows", "Home Alone", "Hunger Games", "Housefull", "Housefull 2", "Housefull 3", "Housefull 4", "Heropanti", "Hero", "Hum", "Hera Pheri", "Hulchul", "Hungama", "Hey Ram", "Haider", "Haseena Maan Jaayegi", "Humpty Sharma Ki Dulhania", "Happy New Year", "Hate Story", "Hate Story 2", "Hate Story 3", "Hate Story 4", "Holiday", "Heroine", "Haqeeqat", "Hum Saath Saath Hain", "Hum Tum", "Hum Dil De Chuke Sanam",
    
    # I
    "Inception", "Interstellar", "Iron Man", "Iron Man 2", "Iron Man 3", "Independence Day", "Insidious", "Inside Out", "India", "I Hate Luv Storys", "Ishq Vishk", "Iqbal", "Ikiru", "Incredibles", "Incredibles 2", "Identity", "In Time", "In the Line of Fire", "Inglourious Basterds", "In Good Company", "Ice Age", "Idiots", "Ittefaq", "Ishqiya", "Islands in the Stream", "Indra", "Insaan", "Ishq", "Inteha", "India Lockdown",
    
    # J
    "Joker", "Jumanji", "Jaws", "Jab We Met", "Jawan", "Jodha Akbar", "Jurassic Park", "Jab Harry Met Sejal", "Jab Tak Hai Jaan", "Jhankaar Beats", "Jab We Met", "Jazbaa", "Jhms", "Jaan-E-Mann", "Jeet", "Jeetenge Hum", "Jism", "Jism 2", "Johnny Gaddaar", "John Wick", "John Wick 2", "John Wick 3", "Judwaa", "Judwaa 2", "Jazbaa", "Jungle", "Jungle Book", "Joker 2019", "Joy", "Julius Caesar",
    
    # K
    "Kabhi Khushi Kabhie Gham", "Kuch Kuch Hota Hai", "Kal Ho Na Ho", "Kabir Singh", "Kantara", "KGF Chapter 1", "KGF Chapter 2", "Kill Bill", "Kingsman", "Kick", "Krish", "Krrish 3", "Lagaan", "Life of Pi", "Kaho Naa Pyaar Hai", "Kabhi Haan Kabhi Naa", "Kaminey", "Karwaan", "Kabul Express", "Kismat Konnection", "Koyla", "Kaabil", "Khichdi", "Khiladi", "Khiladi 786", "Koi Mil Gaya", "Kya Kool Hain Hum", "Kya Super Kool Hain Hum", "Kshanam", "Kaafila", "Kashmir Files", "Karthikeya", "Krishna Cottage",
    
    # L
    "Lagaan", "Life of Pi", "La La Land", "Lion King", "Love Aaj Kal", "Lootera", "Lage Raho Munna Bhai", "Lord of the Rings Fellowship", "Lion", "Logan", "Laxmii", "Love Aaj Kal 2", "London Paris New York", "Lunchbox", "Lakshya", "Lover", "Lust Stories", "Life Partner", "London Dreams", "Looteri", "Luv Shuv Tey Chicken Khurana", "Long Live Lagaan", "Last Emperor", "Life is Beautiful",
    
    # M
    "Mission Impossible", "Mission Impossible Fallout", "Matrix", "Matrix Reloaded", "Matrix Revolutions", "Mardaani", "Munna Bhai MBBS", "Moana", "My Name is Khan", "Mughal E Azam", "Mad Max", "Mad Max Fury Road", "Maleficent", "Mary Kom", "Manjhi The Mountain Man", "Mela", "Masti", "Mumbai Meri Jaan", "Madras Cafe", "Masaan", "M.S. Dhoni", "Madamji", "Mukkabaaz", "Mimi", "Made in China", "Malang", "Mela 2", "Mere Brother Ki Dulhan", "Mere Yaar Ki Shaadi Hai", "Mom", "Mughal-e-Azam", "Mujhse Dosti Karoge", "Munnabhai",
    
    # N
    "Night at the Museum", "Neerja", "Notting Hill", "No Time To Die", "Nayak", "Na Tum Jaano Na Hum", "Naan Aanaiyittal", "Nayak The Real Hero", "Newton", "No One Killed Jessica", "Nishabd", "Namastey London", "New York", "No Entry", "No Problem", "No Smoking", "Nautanki Saala", "Ninja Assassin", "Now You See Me", "Now You See Me 2", "Nebraska", "Nil Battey Sannata", "Neru", "NH10", "Namaste England", "Nishabdham",
    
    # O
    "Om Shanti Om", "Oppenheimer", "Oldboy", "October", "Ok Jaanu", "Oh My God", "Oye Lucky Lucky Oye", "Once Upon A Time In Mumbai", "Once Upon A Time In Mumbai Dobaara", "Once Upon A Time In America", "Outsourced", "Open Season", "Office Space", "Our Family Wedding", "Outbreak", "One Night At McCools", "Only You", "Out of the Furnace", "Ocean's Eleven", "Ocean's Twelve", "Ocean's Thirteen", "O Brother Where Art Thou", "On the Waterfront", "Ordinary People", "Other Guys",
    
    # P
    "Pathaan", "PK", "Padmaavat", "Pirates of the Caribbean", "Pulp Fiction", "Pushpa The Rise", "Pushpa 2", "Pink", "Queen", "Quantum of Solace", "Paan Singh Tomar", "Piku", "Parmanu", "Parzania", "Patiala House", "Pyar Ka Punchnama", "Pyar Ka Punchnama 2", "Panipat", "Prasthanam", "Phir Hera Pheri", "Phata Poster Nikhla Hero", "Page 3", "Partner", "Professor", "Pyaar Impossible", "Pyaar Ka Punchanama", "Pyaar Ke Side Effects", "Pyaar To Hona Hi Tha", "Prem Granth", "Prem Ratan Dhan Payo", "Popcorn", "Penguins of Madagascar",
    
    # Q
    "Qayamat Se Qayamat Tak", "Queen of Katwe", "Quantum of Solace", "Quest for Camelot", "Quarantine", "Quick Change", "Quills", "Quiz Show", "Quo Vadis", "Question Mark", "Qissa", "Quicksand",
    
    # R
    "Rockstar", "Rang De Basanti", "Raazi", "Raees", "Rambo", "Rocky", "RRR", "Robot", "Ready", "Race", "Race 2", "Race 3", "Raid", "Raja Hindustani", "Raja Natwarlal", "Raja Ki Aayegi Baraat", "Rangoon", "R...Rajkumar", "Rustom", "Rab Ne Bana Di Jodi", "Rehnaa Hai Terre Dil Mein", "Raat", "Raja", "Raja Hindustani", "Rocky Handsome", "Rann", "Rocket Singh Salesman", "Roja", "Rog", "Run", "Rudaali", "Rush", "Rush Hour", "Rush Hour 2", "Rush Hour 3", "Robot 2.0", "Romeo Akbar Walter",
    
    # S
    "Sholay", "Singham", "Singham Returns", "Simmba", "Sooryavanshi", "Sultan", "Stree", "Sanju", "Swades", "Shutter Island", "Skyfall", "Spider Man Homecoming", "Spider Man No Way Home", "Spider Man Far From Home", "Saving Private Ryan", "Scream", "Sultan", "Satyameva Jayate", "Special 26", "Swades", "Sarkar", "Sarkar 2", "Sarkar 3", "Sonu Ke Titu Ki Sweety", "Sonchiriya", "Super 30", "Shubh Mangal Saavdhan", "Stree", "Saheb Biwi Aur Gangster", "Saheb Biwi Aur Gangster Returns", "Saand Ki Aankh", "Shubh Mangal Zyada Saavdhan", "Sanam Teri Kasam", "Sadak", "Sadak 2", "Shararat", "Shaadi Se Pehle", "Shaadi Ke Side Effects", "Shaadi Mein Zaroor Aana", "Shubho Druto", "Student of the Year", "Student of the Year 2", "Sui Dhaaga", "Suryavanshi", "Surya", "Satya", "Saudagar", "Sir", "Sarbjit", "Sanam Teri Kasam", "Silsila", "Satyameva Jayate",
    
    # T
    "Titanic", "Terminator", "Terminator 2", "The Avengers", "Thor", "Thor Ragnarok", "Taare Zameen Par", "Tamasha", "Top Gun Maverick", "Twilight", "Toy Story", "Uri The Surgical Strike", "Up", "Us", "Three Idiots", "Talaash", "Tashan", "Tashan", "Tanhaji", "Tashan E Ishq", "Tees Maar Khan", "Tum Bin", "Tum Bin 2", "Tumhari Sulu", "Tu Chor Main Sipahi", "Tum Mile", "Tum Milo Toh Sahi", "Tumhari Sulu", "Twilight", "Twilight Saga New Moon", "Twilight Saga Eclipse", "Twilight Saga Breaking Dawn", "The Lion King", "The Dark Knight", "The Jungle Book", "The Sky Is Pink", "The Zoya Factor", "The White Tiger", "The Kashmir Files", "The Family Man", "The Trial", "Total Dhamaal", "Thappad", "Tuesdays and Fridays", "Tokyo Trial",
    
    # U
    "Uri The Surgical Strike", "Up", "Us", "Udaan", "Ugly", "Ugly Aur Pagli", "Udayananu Tharam", "Ugly", "Unfreedom", "United Six", "Ugly",
    
    # V
    "Vikram", "Vikram Vedha", "Veer Zara", "Vivah", "War", "Whiplash", "Wolf of Wall Street", "Wonder Woman", "Wake Up Sid", "Veer-Zaara", "Vicky Donor", "Veer", "Veerappan", "Vettai", "Veerah", "Vishwaroopam", "Vishwaroopam 2", "Varanasi A Love Story", "Veerapandiya Kattabomman", "Vastadu Naa Raju", "Vedam", "Vicky Donor", "Vidya", "Viraasat", "Virasat", "Vikramarkudu", "Villain", "Village Rockstars", "Vinnaithaandi Varuvaaya",
    
    # W
    "War", "Whiplash", "Wolf of Wall Street", "Wonder Woman", "Wake Up Sid", "Welcome", "Welcome Back", "Wanted", "Wasseypur", "Wedding Pullav", "What Women Want", "We Are Family", "Waqt The Race Against Time", "Water", "Wanted Dead or Alive", "Watchmen", "Wreck-It Ralph", "Wrong Turn", "Who Am I", "White House Down", "World War Z", "Wazir", "Warrior", "Wedding Season", "Wrestling",
    
    # X
    "X Men", "X Men Origins", "X Men Days of Future Past", "X Men First Class", "X Men Last Stand", "X Men Apocalypse", "X Men Dark Phoenix", "X Ray",
    
    # Y
    "Yeh Jawaani Hai Deewani", "Youngistaan", "Zindagi Na Milegi Dobara", "Yuva", "Yes Boss", "Yeh Dil", "Yeh Dillagi", "Yeh Jawaani Hai Deewani", "Yakeen", "Yaadien", "Yatra", "Yaraana", "Yamla Pagla Deewana", "Yaadein", "Yaariyan", "Yeh Hai Jalwa", "Yeh Khula Aasmaan", "Yeh Rishta Kya Kehlata Hai", "Yeh Saali Zindagi", "Yeh Silli Zindagi", "Yuvvraaj", "Yeh Jo Mohabbat Hai",
    
    # Z
    "Zindagi Na Milegi Dobara", "Zero", "Zootopia", "Zakhm", "Zinda", "Zanjeer", "Zinda Bhaag", "Zokkomon", "Zilla Ghaziabad", "Zoom", "Zubeidaa", "Zinda", "Zor Ka Jhatka", "Zameen", "Zakhm", "Zor Lagaa Ke... Haiya", "Zulmi",
    
    # Extra & Edge cases
    "Godfather", "Tere Naam", "Dil", "Hum Aapke Hain Koun", "Deewana", "Dhadkan", "Ghajini", "Ajay", "Khiladi 420", "With Love", "One Two Three", "Tik Tik Tik", "Half Girlfriend", "Jimmy", "Badrinath", "Warning", "Tubelight", "Thank You Dear", "Love in Vietnam", "Karate Kid", "Shahid", "My Fault", "Your Fault", "Our Fault", "Teri Baaton Mein Aisa Uljha Jiya", "Love Khichdi", "Khiladi 786", "Boss", "Mafia", "School Boy", "Singh Is Kinng", "Sky Force", "Andolan", "Yamla Pagla Deewana", "Raaz", "Raaz 2", "Sanam Re", "Azhar", "Sanam Re Part 2", "MS Dhoni The Untold Story", "Hate Story", "Sanam Teri Kasam", "Imtihan", "Maharaja", "Happy New Year", "Island City"
]

# --- FAST LOOKUP SET (case-insensitive) ---
# This converts everything to lowercase so 'golmaal' matches 'Golmaal'
MOVIE_SET = set(m.lower() for m in MOVIES)

def group_by_letter():
    grouped = {}
    for m in MOVIES:
        letter = m.strip()[0].upper()
        grouped.setdefault(letter, []).append(m)
    return grouped

def is_valid_movie(name):
    return name.strip().lower() in MOVIE_SET
