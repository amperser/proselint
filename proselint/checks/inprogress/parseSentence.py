"""General-purpose tools shared across linting checks."""
import os
import shelve
import inspect
import functools
import re
import ipdb
from pattern.en import parsetree


def grab_sentence(text, word_list, ignore_case=True,unicode = False):


    if ignore_case and unicode:
        flags = re.IGNORECASE | re.UNICODE
    elif ignore_case:
        flags = re.IGNORECASE
    elif unicode:
        flags = re.UNICODE
    else:
        flags = 0


    sentences = []
    for w in word_list:
        for s in re.finditer(ur'([^.]*{}[^.]*)'.format(w), text, flags=flags):
            sentences.append(s.group(0))
            print s.group(0)

            # txt = m.group(0).strip()
            # errors.append((m.start()+1, m.end(), err, msg.format(txt)))
    return sentences

def parsing_sentence(sentence_list):

    for s in sentence_list:
        parsed_sentence = parsetree(s)
        for sentence in parsed_sentence:
            for chunk in sentence.chunks:
                for word in chunk.words:
                    print word,
                print

        # s = parsetree(s, relations=True, lemmata=True)
        # print(s)



if __name__ == '__main__':
    texts = "This is a sentence with there. This is this sentences zepplin. This is their sentence. They aren't going to be easy to detect. They're going to be hard to detect."
    sentence_list = grab_sentence(texts,["there","their","they're"])
    parsing_sentence(sentence_list)
