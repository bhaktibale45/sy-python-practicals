
paragraph = input("Enter a paragraph:\n")
target_word = "python"


words = paragraph.lower().split()


target_count = 0
for word in words:
    cleaned_word = word.strip(".,!?;:\"'()[]{}")
    if cleaned_word == target_word:
        target_count += 1


substring_count = paragraph.lower().count(target_word)

print("\n" + "=" * 50)
print(f"{'WORD COUNTER UTILITY REPORT':^50}")
print("=" * 50)
print(f" Target Word           : '{target_word}'")
print(f" Exact Word Matches    : {target_count}")
print(f" Total Substring Count : {substring_count}")
print("=" * 50)