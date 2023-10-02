#!/usr/bin/python3
"""text_indentation function definition"""


def text_indentation(text):
    """function that prints a text with 2 new lines
        after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text_lst = list(text)
        final_lst = []
        delimters = [".", "?", ":"]
        for i in range(len(text_lst)):
            if (text_lst[i] in delimters):
                final_lst.append(text_lst[i])
                final_lst.append("\n")
                final_lst.append("\n")
            else:
                if (text_lst[i] == " " and final_lst == []):
                    continue
                elif (text_lst[i] == " " and
                        final_lst[len(final_lst) - 1] == "\n"):
                    continue
                else:
                    final_lst.append(text_lst[i])
    new_text = "".join(final_lst)
    print(new_text, end="")
