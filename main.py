import random


def get_wordlist(filename: str) -> list:
    wordlist = []
    with open(filename, 'r') as file:
        for line in file:
            wordlist.append(line)
        return wordlist


def generate_phrase(wordlist: list) -> list:
    result = []
    for i in range(12):
        rand_elem = random.randint(0, len(wordlist))
        if wordlist[rand_elem] not in result:
            result.append(wordlist[rand_elem])
    return result


def save_phrase(phrase: list, filename='phrase.txt') -> None:
    with open(filename, 'w') as file:
        for word in phrase:
            file.write(word)


def main():
    wordlist = get_wordlist('english.txt')
    phrase = generate_phrase(wordlist)
    save_phrase(phrase)

if __name__ == '__main__':
    main()