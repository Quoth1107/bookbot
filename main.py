#def get_book_text(filepath):
#    with open(filepath) as f:
#        file_contents = f.read()
#    return file_contents

# print(get_book_text("books/frankenstein.txt"))

import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import (
    get_num_words,
    count_characters,
    convert_dict,
    sort_on,
)

address = sys.argv[1]

character_list = count_characters(address)
sorted_list = convert_dict(character_list)

print(f"""

============ BOOKBOT ============
Analyzing book found at {address}...
----------- Word Count ----------
Found {get_num_words(address)} total words
--------- Character Count -------""")

for item in sorted_list:
    if item["char"].isalpha() == True:
        print(f"{item['char']}: {item['num']}")

print("""============= END ===============

""")
