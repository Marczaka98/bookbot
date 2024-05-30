def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = count_words(text)
    letter_counts = count_letters(text)
    converted_list = convert_letter_dict_to_list(letter_counts)
    converted_list.sort(reverse=True, key=sort_on)
    print_report(book_path, word_count, converted_list)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_name):
    words = file_name.split()
    return len(words)

def count_letters(file_name):
    letters = {}
    lowercase_file = file_name.lower()
    for letter in lowercase_file:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def convert_letter_dict_to_list(letter_dict):
    letter_list = []
    for letter in letter_dict:
        if letter.isalpha():
            letter_list.append(
                {"letter": letter, "count": letter_dict[letter]}
            )
    return letter_list

def sort_on(dict):
    return dict["count"]

def print_report(path, word_count, letters_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for i in range(0, len(letters_list)):
        print(f"The {letters_list[i]["letter"]} character was found {letters_list[i]["count"]} times")
    print("--- End report ---")

main()