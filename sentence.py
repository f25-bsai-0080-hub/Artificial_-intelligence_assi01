
def count_words(sentence):
    words = sentence.split()
    return len(words)


def count_characters(sentence):
    return len(sentence)


def find_longest_word(words):
    return max(words, key=len)


def find_shortest_word(words):
    return min(words, key=len)


def count_vowels(sentence):
    count = 0

    for ch in sentence.lower():
        if ch in "aeiou":
            count += 1

    return count


def analyze_sentence():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    total_words = count_words(sentence)
    total_characters = count_characters(sentence)

    if len(words) == 0:
        print("Please enter a valid sentence.")
        return

    longest_word = find_longest_word(words)
    shortest_word = find_shortest_word(words)
    vowels = count_vowels(sentence)

    unique_words = set(word.lower() for word in words)

    alphabetical_words = sorted(unique_words)

    print("\nWord Analysis")
    print("Total Words:", total_words)
    print("Total Characters:", total_characters)
    print("Longest Word:", longest_word)
    print("Shortest Word:", shortest_word)
    print("Total Vowels:", vowels)
    print("Unique Words:", unique_words)
    print("Alphabetical Order:", alphabetical_words)

    with open("word_analysis.txt", "w") as file:
        file.write("Word Analysis\n")
        file.write("Total Words: " + str(total_words) + "\n")
        file.write("Total Characters: " + str(total_characters) + "\n")
        file.write("Longest Word: " + longest_word + "\n")
        file.write("Shortest Word: " + shortest_word + "\n")
        file.write("Total Vowels: " + str(vowels) + "\n")
        file.write("Unique Words: " + str(unique_words) + "\n")
        file.write("Alphabetical Order: " + str(alphabetical_words) + "\n")

    print("\nAnalysis saved in word_analysis.txt")


analyze_sentence()
