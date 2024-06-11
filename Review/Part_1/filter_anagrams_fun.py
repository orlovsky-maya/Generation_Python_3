def convert_to_dict(word):
    word_dict = {}
    for l in word:
        word_dict[l] = word_dict.get(l, 0) + 1

    return word_dict


def filter_anagrams(word, words):
    result = list(filter(lambda w: convert_to_dict(w) == convert_to_dict(word), words))
    return result



# INPUT DATA:

# TEST_1:
word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))

# TEST_2:
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

# TEST_3:
print(filter_anagrams('tommarvoloriddle',
                      ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))

# TEST_4:
print(filter_anagrams('стекло', []))

# TEST_5:
print(filter_anagrams('крона', ['кротко', 'укроп', 'норка']))

# TEST_6:
print(filter_anagrams('чулки', ['лучик', 'чутко', 'кочка']))

# TEST_7:
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))

# TEST_8:
word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
print(filter_anagrams(word, anagrams))



# # OUTPUT DATA:
#
# # TEST_1:
# ['aabb', 'bbaa']
#
# # TEST_2:
# ['сеточка', 'стоечка', 'тесачок', 'чесотка']
#
# # TEST_3:
# ['iamlordvoldemort']
#
# # TEST_4:
# []
#
# # TEST_5:
# ['норка']
#
# # TEST_6:
# ['лучик']
#
# # TEST_7:
# ['кулон', 'уклон']
#
# # TEST_8:
# []