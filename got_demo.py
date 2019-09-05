from pprint import pprint
from characters import characters

# characters_A = []
# characters_Z = []
# characters_deceased = []

# for character in characters:
    # if character['died']:
        # pprint(character['name'])
        # characters_deceased.append(character['name'])
        # characters_Z.append(character['name'])

# print(characters_A)
# print(len(characters_Z))
# print(len(characters_deceased))
    # if character['name'].startswith('A') == True:
        # pprint(character['name'])

# print(len(characters))

# # print out the key names individually
# for title in characters:
    # print(title['name'].sorted('title'))
    # character_titles.append(characters['name'])

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
# print("%s: %s" % (k, jon_snow[k]))

most_titles = 0
# Who has the most titles?
for character in characters:
    num_titles = len(character['titles'])
    if num_titles > most_titles:
        most_titles = num_titles
        # person_with_most_titles = person['name']
        
# print out the names of each person with the same number of titles as 'most_titles'
for character in characters:
    num_titles = len(character['titles'])
    if num_titles == most_titles:
        print("%s has %d titles" % (character['name'], most_titles))
        
print("nope that's it")