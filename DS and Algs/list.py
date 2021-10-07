word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
   for a_letter in a_word:
        letter_list.append(a_letter)

#print(letter_list)

##print(letter_list)
letter_list.remove('a')
letter_list.remove('b')
letter_list.remove('t')
letter_list.sort()
print(letter_list)
