def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return len(file_contents.split())

# print(f"{get_num_words("books/frankenstein.txt")} words found in the document")


def count_characters(filepath):
    with open(filepath) as f:
        file_contents = f.read().lower()
        letter_list = list(file_contents)

        characters = {}

        for letter in letter_list:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1

        return characters

# print(count_characters("books/frankenstein.txt"))


def convert_dict(dictionary):
    list_of_dict = [{"char": k, "num" :v} for k, v in dictionary.items()]
    sorted_list = list_of_dict.sort(reverse = True, key = sort_on)
    return list_of_dict

def sort_on(items):
    return items["num"]
    
