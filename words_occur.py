def words_occur():
    file_name = input("Enter the name of the file: ")
    with open(file_name, 'r') as file:
        word_list = file.read().split()
        file.close()
        occurs_dict = {}
        for word in word_list:
            occurs_dict[word] = occurs_dict.get(word, 0) + 1
        print(f"File {file_name} has {len(word_list)}, {len(occurs_dict)} are unique")
        print(occurs_dict)


words_occur()

# Enter the name of the file: NoMan
# File NoMan has 81, 62 are unique
# {'No': 1, 'man': 2, 'is': 3, 'an': 1, 'island,': 1, 'Entire': 1, 'of': 5, 'itself,': 1, 'Every': 1, 'a': 4, 'piece': 1, 'the': 5, 'continent,': 1, 'A': 1, 'part': 1, 'main.': 1, 'If': 1, 'clod': 1, 'be': 1, 'washed': 1, 'away': 1, 'by': 1, 'sea,': 1, 'Europe': 1, 'less.': 1, 'As': 2, 'well': 2, 'as': 2, 'if': 2, 'promontory': 1, 'were.': 1, 'manor': 1, 'thy': 1, 'friend’s': 1, 'Or': 1, 'thine': 1, 'own': 1, 'were:': 1, 'Any': 1, 'man’s': 1, 'death': 1, 'diminishes': 1, 'me,': 1, 'Because': 1, 'I': 1, 'am': 1, 'involved': 1, 'in': 1, 'mankind,': 1, 'And': 1, 'therefore': 1, 'never': 1, 'send': 1, 'to': 1, 'know': 1, 'for': 2, 'whom': 1, 'bell': 1, 'tolls;': 1, 'It': 1, 'tolls': 1, 'thee.': 1}
#
# Process finished with exit code 0