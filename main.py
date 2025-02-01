def count_words(text):
    # Split the text into words and return the word count
    words = text.split()
    return len(words)

def count_characters(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the text
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
    return char_count

def print_report(word_count, char_count):
    # Start the report
    print("--- Begin report of books/frankenstein.txt ---")
    
    # Print the word count
    print(f"{word_count} words found in the document")
    
    # Print the character counts for only alphabetic characters
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in char_count:
            print(f"The '{char}' character was found {char_count[char]} times")
    
    # End the report
    print("--- End report ---")

def main():
    # Open the file (use the correct path)
    with open("books/frankenstein.txt", "r") as file:
        # Read the contents of the book
        book_text = file.read()
    
    # Call the count_words function to count the words in the book
    word_count = count_words(book_text)
    
    # Call the count_characters function to count the characters in the book
    character_count = count_characters(book_text)
    
    # Print the report
    print_report(word_count, character_count)

# Run the main function
if __name__ == "__main__":
    main()


