import pandas as pd

def generate_blacklist_bad_words(corpus_file):
    data = pd.read_json(corpus_file)

    uppercase_bad_words = []
    lowercase_bad_words = []
    swapcase_bad_words = []

    for word in data[0]:
        # convert corpus to uppercase
        uppercase_bad_words.append(word.upper())

        # convert corpus to lowercase
        lowercase_bad_words.append(word.lower())

        # convert corpus to swapcase
        swapcase_bad_words.append(word.swapcase())

    # convert it to DataFrame
    df_uppercase = pd.DataFrame(uppercase_bad_words)
    df_lowercase = pd.DataFrame(lowercase_bad_words)
    df_swapcase = pd.DataFrame(swapcase_bad_words)

    # concat master corpus with converted corpus
    final_data = pd.concat([data, df_uppercase, df_lowercase, df_swapcase], ignore_index = True)

    # convert to Trakteer format bad words filter
    final_data.to_csv("bad_words_trakteer.txt", index = False, header = False, lineterminator = ', ')

    # convert to Saweria format bad words filter
    final_data.to_csv("bad_words_saweria.txt", index = False, header = False, lineterminator = ' ')


if __name__ == "__main__":
    print("Start Generate Blacklist Words!")
    generate_blacklist_bad_words(corpus_file = "corpus_bad_words.json")
    print("End of Process~")