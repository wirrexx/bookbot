from collections import Counter
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    split_word = text.split()
    count=len(split_word)
    return count

def count_chars(text):
    
    char_counts = Counter(char.lower() for char in text if char.isalpha())
    return char_counts.most_common()

            
        
def sort_on(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    text = get_book_text(filepath)
    
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    
    print("--------- Character Count -------")
    for char, count in count_chars(text):
        print(f"{char}: {count}")
    
    print("============= END ===============")


sort_on("books/frankenstein.txt")