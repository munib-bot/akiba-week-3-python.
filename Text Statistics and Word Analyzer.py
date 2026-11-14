
def count_words(text):
    words = text.split()
    return len(words)

def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
def count_how_many_times_word_appears(text, word):
    words = text.split()
    return words.count(word)
def repeated_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    repeated = {word: count for word, count in word_count.items() if count > 1}
    return repeated
def count_characters(text):
    return len(text)
text = input("Enter the text: ")
print("Number of words:", count_words(text))
print("Number of characters:", count_characters(text))
print("Number of vowels and consonants:", count_vowels_consonants(text))
print("Longest word:", longest_word(text))
print("Repeated words:", repeated_words(text))
word_to_count = input("Enter a word to count its occurrences: ") 
print(f"The word '{word_to_count}' appears {count_how_many_times_word_appears(text, word_to_count)} times.")
