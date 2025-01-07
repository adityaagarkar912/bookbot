def main():
    book_path = "books/frankenstein.txt"
    character_count = {}
    text = get_book_text(book_path)   
    total_words_in_book = get_num_words_in_book(text)
    character_count = get_character_count_in_book(text, character_count)
    character_count_dict_list = convert_dict_to_sorted_list(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words_in_book} words found in the document \n")
    print_character_count(character_count_dict_list)
    print("--- End report ---")

def get_num_words_in_book(book_text):
    words = book_text.split()
    return len(words)

def get_character_count_in_book(book_text, character_count):
    words = book_text.split()
    for word in words:
        for c in word:
            c = c.lower()
            if c in character_count:
                new_count = character_count[c] + 1
                character_count[c] = new_count
            else:
                character_count[c] = 1
    return character_count

def convert_dict_to_sorted_list(character_count):
    character_count_dict_list = []
    for c in character_count:
        new_dict = {}
        new_dict["char"] = c
        new_dict["count"] = character_count[c]
        character_count_dict_list.append(new_dict)
    character_count_dict_list.sort(reverse = True, key = sort_def)
    return character_count_dict_list

def sort_def(dict):
    return dict["count"]


def print_character_count(character_count_dict_list):
    for dict in character_count_dict_list:
        if dict["char"].isalpha():
            print(f'The \'{dict["char"]}\' character was found {dict["count"]} times')


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
