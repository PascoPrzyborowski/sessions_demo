
Sentence=  "Peter and Jane runs in Circles"

def count_letters(string):
    count = 0
    for letter in string:
        count += 1

    return count

# def count_leters(string):
#     count = 0
#     for letter in string:
#         count += 1
    
#     return count

print(count_letters("I love coding"))

#a,e,i,o,u
def count_vowels(string):
    count = 0
    letter = 'aeiou'
    for l in string:
        if l.lower() in letter:
            count += 1
    return count

print(count_vowels("bookae"))

def count_dict_vowels(string):
    count = 0
    letter = 'aeiou'
    dictout = {}
    for letter in string:
        l = letter.lower()
        if l.lower() in 'aeiou':
            if l in dictout:
                dictout[l] += 1
            else:
                dictout[l] = 1
            
            
    return dictout

print(count_dict_vowels("shaban lingoda"))
