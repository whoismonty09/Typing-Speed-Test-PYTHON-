import time
import random

sentences = [
    "Python is a powerful programming language",
    "Practice makes a person perfect",
    "Typing speed improves with regular practice",
    "Learning coding is fun and useful",
    "Consistency is the key to success"
]

sentence = random.choice(sentences)

print("Typing Speed Test")
print("Type the following sentence:")
print(sentence)

input("Press Enter when you are ready...")

start_time = time.time()
typed_text = input()
end_time = time.time()

time_taken = end_time - start_time

words = len(sentence.split())
speed = (words / time_taken) * 60

if typed_text == sentence:
    accuracy = 100
else:
    correct_chars = 0
    for i in range(min(len(sentence), len(typed_text))):
        if sentence[i] == typed_text[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(sentence)) * 100

print("Time taken:", round(time_taken, 2), "seconds")
print("Typing speed:", round(speed, 2), "words per minute")
print("Accuracy:", round(accuracy, 2), "percent")
