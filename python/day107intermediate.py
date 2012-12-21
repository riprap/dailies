"""
Verify the Infinite Monkey Theorem
[http://en.wikipedia.org/wiki/Infinite_monkey_theorem]. Well that's a bit hard,
so let's go with this. Using any method of your choice, generate a random string
of space-separated words. (The simplest method would be to randomly choose, with
equal probability, one of the 27 characters including letters and space.) Filter
the words using a word list[2] of your choice, so that only words in the word
list are actually output.
That's all you need for the basic challenge. For extra points, run your program
for a few minutes and find the most interesting string of words you can get. The
longer the better. For style, see if you can "train your monkey" by modifying
either the random character generator or the word list to output text that's
more Shakespearean in less time.
"""
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
word_list = []
word_lengths = []

f = open('txt/day107wordlist.txt', 'r')
for line in f:
    line = line.replace("\r\n", "").strip()
    word_list.append(line)
    word_lengths.append(len(line))

max_word_length = max(word_lengths)

iteration_count = 0
word_count = 0
word = ""
while word_count < 20:
    iteration_count+=1
    random_letter = letters[random.randint(0,len(letters)-1)]
    if random_letter ==  " ":
        for x in word_list:
            if x == word:
                #prints if random word matches a word in the word list
                print word
                word_count+=1
        #start new word
        word = ""
    else:
        #word is longer than the max word length, start a new word (saves time)
        if len(word)>max_word_length:
            word = ""
        else:
            #concatenate letter to word
            word += random_letter