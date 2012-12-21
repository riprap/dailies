import time

word_list = []
f = open('txt/day107wordlist.txt', 'r')
for line in f:
    line.replace("\r\n", "").strip()
    word_list.append(line)
print word_list

"""
iteration_count = 0
word_count = 0
word = "zyme"
for x in word_list:
    x.replace('\n','')
    print "%s" %x
    print "%s" %word
    time.sleep(1)
"""