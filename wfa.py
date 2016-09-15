

open_file = open("sample.txt")
contents = open_file.read()
contents= contents.replace (".", " ")
contents= contents.replace ("!"," ")
contents= contents.replace (" "" "," ")
contents= contents.split()
my_counter_dictionary = {}
for x in contents:
    if x in my_counter_dictionary.keys():
        my_counter_dictionary[x] += 1
    else:
        my_counter_dictionary[x] = 1
open_file.close()
print(contents)
print(sorted(my_counter_dictionary.items(), key=lambda x: x[1]))
