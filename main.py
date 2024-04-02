def main():
    path = "books/frankenstein.txt"
    text = read_text_from_book(path)
    
    print(f"--- Count report of {path} ---")

    print(f"This many words occured in the book: {print_wordcount(text)}")
    
    for letter_count in get_letter_counts(text):
        print(f"Letter '{letter_count["letter"]}' occured {letter_count["count"]} times")
        
    print ("--- End of report")
        
    

def get_letter_counts(text):
    letters = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

    letters_sorted = []

    for letter in letters:
        letters_sorted.append({
            "letter": letter, 
            "count": letters[letter]
        })

    letters_sorted.sort(reverse=True, key=sort_on)
    return letters_sorted

def sort_on(dict):
    return dict["count"]

def print_wordcount(text):
    count_of_words = count_words(text)
    return count_of_words

def read_text_from_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

main()