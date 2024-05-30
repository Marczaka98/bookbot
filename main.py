def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    #print(text)
    word_count = count_words(text)
    print(f"WORD COUNT: {word_count}")
    print(count_letters(text))

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
    print(letters)

main()