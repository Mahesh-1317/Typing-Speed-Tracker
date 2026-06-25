import time
import random
import os
import difflib

sentences = [
    "Python is easy to learn",
    "Coding improves logical thinking",
    "Mogembo khush hua",
    "Billo bagge billiya da ki karegi?",
    "Salman Khan wants to smoke cigeratte",
    "Why did Katappa kill Bahubali?"
]

type_text = random.choice(sentences)
print("Type the following sentence: ")
print(type_text)
print()

start_time = time.time()

typed = input("Enter text: ")
print()

#   TIME CALCULATION

end_time = time.time()
time_taken = end_time - start_time
print(f"Time Taken: {round(time_taken,2):>10} sec")


words = len(typed.split())
print(f"Word Typed: {words:>6}")


if time_taken > 0:
    WPM = words / (time_taken / 60)
    print(f"Typing Speed: {round(WPM):>5} WPM")

#   MISTAKES AND ACCURACY

original_words = type_text.split()
typed_words = typed.split()


matcher = difflib.SequenceMatcher(None, type_text, typed)

mistakes = 0

for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    if tag != "equal":
        mistakes += max(i2 - i1, j2 - j1)
print(f"Mistakes: {mistakes:>8}")

correct_words = 0
total_words = 0

for i in range(min(len(original_words), len(typed_words))):
    org_words = original_words[i]
    tpd_words = typed_words[i]

    total_words += max(len(org_words), len(tpd_words))

    for j in range(min(len(org_words), len(tpd_words))):
        if org_words[j] == tpd_words[j]:
            correct_words += 1

for i in range(min(len(original_words),len(typed_words)), max(len(original_words),len(typed_words))):
    if i < len(original_words):
        total_words += len(original_words[i])
    else:
        total_words += len(typed_words[i])

accuracy = (correct_words / total_words) * 100 if total_words > 0 else 0

print(f'Accuracy: {round(accuracy,2):>11}')
print()


#   STORE DATA OF LAST 5 SESSIONS

base_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(base_dir, 'typing_history.csv')

if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write('time,wpm,mistakes,accuracy\n')

with open(file, 'a') as f:
    f.write(f'{round(time_taken,2)}, {round(WPM)}, {mistakes}, {round(accuracy,2)}\n')

with open(file, 'r') as f:
    lines = f.readlines()

header = lines[0]
data = lines[1:]
last5 = data[-5:]

with open(file, 'w') as f:
    f.write(header)
    f.writelines(last5)

print("No. | Time(sec) | WPM | Mistakes | Accuracy")

i = 1
for line in last5:
    t, wpm, mis, acc = line.strip().split(',')
    print(f'{i:<4} |  {t:<10} |  {wpm:<5} |  {mis:<9} |  {acc}%')
    i += 1