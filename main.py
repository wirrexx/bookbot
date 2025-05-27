def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

def count_words(text):
    split_word = text.split()

    count=len(split_word)
    print(f"{count} words found in document")

text = get_book_text("books/frankenstein.txt")
count_words(text)
