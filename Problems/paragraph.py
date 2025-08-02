
sentence = input(str("Enter Your Paragraph here : "))

# total_len = len(sentence)

# print(new_sen)
sentence_without_spaces = ""
for _ in sentence:
    if _ != " ":
        sentence_without_spaces += _

print(len(sentence_without_spaces))
