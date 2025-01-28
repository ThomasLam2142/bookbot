with open("books/frankenstein.txt") as f:
    file_contents = f.read()

lowered_string = ''.join(char for char in file_contents if char.isalpha())
lowered_string = lowered_string.lower()

alphabet_map = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}

for i in lowered_string:
    alphabet_map[i] += 1

print("--- Begin report of books/frankenstein.txt ---")
print(len(file_contents.split()))
for i in alphabet_map:
    print("The '" + i + "' character was found " + str(alphabet_map[i]) + " times")
