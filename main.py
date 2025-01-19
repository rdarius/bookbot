chars = {}
filename = 'books/frankenstein.txt'

with open(filename) as f:
    print(f"--- Begin report of {filename} ---")
    file_contents = f.read()

    words = len(file_contents.split())
    print(f"{words} words found in the document\n")

    for char in file_contents:
        lower = char.lower()
        if 'a' <= lower and lower >= '<':
            if lower not in chars:
                chars[lower] = 0
            chars[lower] += 1

    sorted_dict = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

    for char in sorted_dict:
        print(f"The '{char}' character was found {chars[char]} times")

    print('--- End report ---')
