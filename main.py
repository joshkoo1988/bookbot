def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    alpha_count = letter_counts(text)
    for letter,count in alpha_count.items():
            print(f"{letter}: {count}")

def word_count(text):
    count = text.split()
    return len(count)

def letter_counts(text):
    lower_text = text.lower()
    alphabet_count = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in alphabet_count:
                alphabet_count[letter] += 1
            else:
                alphabet_count[letter] = 1
    sorted_alphabet_count = dict(sorted(alphabet_count.items()))
    return sorted_alphabet_count



def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()
