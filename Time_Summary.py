while True:
    try:
        text = input("Enter your text \n")
        amount = len(text)
        print(f"Total Characters: {amount}")
        seperate_words = text.split()
        total_words = len(seperate_words)
        print(f"Total words: {total_words}")
        total_sentences = text.count('.') + text.count('!') + text.count('?')
        print(f"Total sentences: {total_sentences}")
        longest_word = ""
        for i in seperate_words:
            if len(i) > len(longest_word):
                longest_word = i
        print(f"Longest Word: {longest_word}")
        repeat_words = []
        for i in seperate_words:
            if i not in repeat_words:
                repeat_words.append(i)
            else:
                print(f"Repeat words: {i}")
        letter = 0
        for i in seperate_words:
            letter += len(i)

        average = letter/total_words
        print(f"Average words: {average:.02f}")
    except ZeroDivisionError:
        print("Total words is 0!, please try again.")
    play_again = input("Do you want to play again? Yes/No").lower()
    if play_again != "yes":
        break