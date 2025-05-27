from collections import Counter
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)


def count_words(text):
    split_word = text.split()

    count=len(split_word)
    print(f"{count} words found in the document")


def count_chars(text):
    
    counted_text = Counter(text.lower())
    print(counted_text)

            
        
        
        
    

counted_book = get_book_text("books/frankenstein.txt")
# count_words(text)
count_chars(counted_book)

