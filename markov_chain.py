import random
from colors import bcolors

# --------------------------- functions ---------------------------
def gen_table(text):
    text = text.split(" ")
    table = {}

    for i, word in enumerate(text):
        if word not in table:
            table[word] = [] # list to store words that come after the current one
        
        if i+1 < len(text):
            table[word].append(str(text[i+1]))

    return table

def bi_gram(text):
    """Split text into a bunch of bi grams"""
    table = {}
    text = text.split(' ')

    for i in range(len(text)):
        if i + 4 < len(text):
            word = text[i] + ' ' + text[i+1] # gets bigram
            if word not in table:
                table[word] = [] # list to store words that come after the current one
            
            table[word].append(str(text[i+2] + ' ' + text[i+3])) # adds next two words 

    return table

def n_gram(text, n):
    """Split text into a bunch of phrases size n"""
    table = {}
    text = text.split(' ')

    for i in range(len(text)):
        if i + n*2 < len(text):
            # get current phrase and next phrase
            phrase = ""
            next_phrase = ""
            for word_count in range(n):
                phrase += text[i+word_count] + " "
                next_phrase += text[i+word_count+n] + " "

            phrase = phrase.strip()
            next_phrase = next_phrase.strip()
            
            # put in table if not already
            if phrase not in table:
                table[phrase] = []

            # add next phrase to table as value
            table[phrase].append(next_phrase) # adds next two words 

    return table

def find_garbage(table):
    """Prints the most common ngrams / finds titles / garbage"""
    largest_values = []
    for value in table.values():
        if len(value) > 2:
            largest_values.append(value)

    largest_values.sort(key=len)
    for i in largest_values:
        print(i)

def markov_chain(table, sentence_len, seed):
    """Generate a random string of words based on probabiltiy table markov style"""
    seed = seed
    sentence = seed + ' '
    for i in range(sentence_len):
        pos_words = table[seed]
        if len(pos_words) > 0:
            word = random.choice(pos_words)
            
            sentence += word + ' '
            seed = word

        else:
            break

    return sentence


# --------------------------- input and text generation ---------------------------
data = '' # load formatted text
with open("formatted.txt", "r") as f:
    data = f.read()

n_length = str(input("What gram : ")) # process text markov chain style table
table = n_gram(data, int(n_length))
text_length = int(input("Text length: "))

autokeys = list(set([x.lower() for x in table.keys()]))


autoseed = False
while True:
    # finds a word in the table keys
    if not autoseed:
        seed = str(input("Seed (Type three exclamation marks to exit) : ")) # seed word to start generation
    
    if seed == "!!!":
        break

    # find possible keys
    print("Finding keys...")
    possible_keys = []
    for tkey in table.keys():
        if seed.lower() in tkey.lower():
            possible_keys.append(tkey)

    print("Generating...")
    print("-"*80)
    # generate text
    if len(possible_keys) > 0:
        output = markov_chain(table, text_length, random.choice(possible_keys))
        print(f"{bcolors.OKCYAN}{output}{bcolors.ENDC}")

