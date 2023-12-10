def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    total, letters = get_total_words_chars(text)
    report = make_report(letters)
    print_funct(book_path, total, report)

def get_total_words_chars(text):
    words = text.split()
    total = 0
    letters = {}
    for word in words:
        total += 1
        for char in word:
            little_char = char.lower()
            if little_char not in letters:
                letters[little_char] = 1
            else:
                letters[little_char] += 1
    return total, letters

def print_funct(book, number, list):
    print(f"--- Begin report of {book} ---")
    print(f"{number} words found in the document")
    for i, j in list:
        print(f"The '{j}' character was found {i} times")
    print("--- End report ---")

def make_report(dict):
    report = list()
    for key, val in dict.items():
        if key.isalpha():
            report.append([val, key])
        report.sort(reverse=True)
    return report

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()