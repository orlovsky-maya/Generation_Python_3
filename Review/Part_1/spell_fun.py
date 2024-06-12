def spell(*args):
    first_letters = list(map(lambda word: (word[0].lower(), len(word)), args))
    result = {}
    for tup in first_letters:
        num = result.setdefault(tup[0], tup[1])
        if num < tup[1]:
            result[tup[0]] = tup[1]
        else:
            continue

    return result



# # TEST_9:
# words = ['aaaaaa',"aaaa"]
# print(spell(*words))



# INPUT DATA:

# TEST_1:
words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))

# TEST_2:
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

# TEST_3:
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

# TEST_4:
print(spell())

# TEST_5:
words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
print(spell(*words))

# TEST_6:
words = ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
print(spell(*words))

# TEST_7:
words = ['a']
print(spell(*words))

# TEST_8:
words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))


# # OUTPUT DATA:
#
# # TEST_1:
# {'р': 7, 'а': 9, 'у': 10, 'к': 5}
#
# # TEST_2:
# {'м': 10, 'и': 11, 'х': 5, 'б': 8}
#
# # TEST_3:
# {'f': 8}
#
# # TEST_4:
# {}
#
# # TEST_5:
# {'a': 5}
#
# # TEST_6:
# {'a': 5}
#
# # TEST_7:
# {'a': 1}
#
# # TEST_8:
# {'a': 4, 'б': 2, 'а': 19, 'ё': 4}