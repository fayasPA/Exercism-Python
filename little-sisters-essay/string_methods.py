"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    title_list = title.split()
    word = []
    for each_word in title_list:
        each_word = each_word[0].upper() + each_word[1:len(each_word)]
        word.append(each_word)
    return ' '.join(word)


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    if sentence[-1] == '.':
        return True
    return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    each_word = sentence.split()
    for index,word in enumerate(each_word):
        if word == old_word:
            each_word[index] = new_word
    if each_word[len(each_word)-1][:-1] == old_word:
        each_word[len(each_word)-1] = new_word + '.'
    return ' '.join(each_word)
    