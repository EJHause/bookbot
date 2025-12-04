def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    # convert the text to lowercase
    text = text.lower()
    char_counts = {}

    # Now loop through each charater in the string
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    #convert dictionary
    char_list = [{"char": c, "num": n} for c, n in char_counts.items() if c.isalpha()]
    def get_num(item):
        return item["num"]

    #sort list in place, greatest to least
    char_list.sort(key=get_num, reverse=True)

    return char_list


