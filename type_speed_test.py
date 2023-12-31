import random
import time
def calculate_typing_speed(text, elapsed_time):
    words = text.split()
    total_words = len(words)
    words_per_minute = (total_words / elapsed_time) * 60

    return words_per_minute
def main():
    text = "python is an experiment in how much freedom programmers needed"
    print("Welcome to Typing Speed Test!")
    input("Press enter to start..")

    print("Type the following text:")
    print(text)

    input("press enter to start typing...")
    

    start_time = time.time()

    user_input = input("Start typing here: ")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nTyping Test Result:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    speed = calculate_typing_speed(text, elapsed_time)
    print(f"Your typing speed: {speed:.2f} words per minute")

if __name__ == "__main__":
    main()
    

