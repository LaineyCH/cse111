"""
Generates English sentences, containing a determiners, adjectives, nouns, prepositional phrases, an adverb, and a verb;
using a list of sentence characteristics to determine plurality and tense.
"""
import random

def main():
    # list of sets of sentence characteritics
    sentence_characteristics = [
        [1, "past"], 
        [1, "present"],
        [1, "future"],
        [5, "past"],
        [3, "present"],
        [4, "future"],
    ]
    # for each set of sentence characteristics, create and print a sentence.
    for characteristics in sentence_characteristics:
        sentence = make_sentence(characteristics[0], characteristics[1])
        print(sentence)

def make_sentence(quantity, tense):
    """
    Return a sentence constructed from:
    {Determiner} {adjective} {noun} {prepositional_phrase} {adverb} {verb} {determiner} {adjective} {noun} {prepositional_phrase}.
    Parameters
        quantity: an integer.
        tense: "past", "present" or "future"
    Return
        sentence: a correctly constructed sentence
    """
    determiner_1 = get_determiner(quantity)
    adjective_1 = get_adjective()
    noun_1 = get_noun(quantity)
    prepositional_phrase_1 = get_prepositional_phrase(quantity)
    adverb = get_adverb(tense)
    verb = get_verb(quantity, tense, True)
    determiner_2 = get_determiner(quantity)
    adjective_2 = get_adjective()
    noun_2 = get_noun(quantity)
    prepositional_phrase_2 = get_prepositional_phrase(quantity)
    sentence = determiner_1.capitalize() + " " + adjective_1 + " " + noun_1 + " " + prepositional_phrase_1 + " " + adverb + " " + verb + " " + determiner_2 + " " + adjective_2 + " " + noun_2 + " " + prepositional_phrase_2 + "."
    return sentence

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a "ingle noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a noun.
    word = random.choice(words)
    return word
    
def get_verb(quantity, tense, leading_adverb=True):
    """Return a randomly chosen verb. If tense is "past", this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Unless, there is an adverb before the verb, then the "will" is dropped.
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
        leading_adverb: boolean. If true "will" is dropped from the future tense verb phrase.
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    if tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        if leading_adverb:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        else:
            words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner, and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = preposition + " " + determiner + " " + noun
    return prepositional_phrase

def get_adverb(tense):
    """Return a randomly chosen adverb from this list of adverbs:
        "quickly", "sweetly", "calmly", "noisily", "slowly", "carefully"
    Parameter: tense - if "future" will is added before the adverb (for the verb conjugation)
    Return: a randomly chosen adverb.
    """
    if tense == "future":
        words = ["will quickly", "will sweetly", "will calmly", "will noisily", "will slowly", "will carefully"]
    else:
        words = ["quickly", "sweetly", "calmly", "noisily", "slowly", "carefully"]
    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_adjective():
    """Return a randomly chosen adjective from this list of adjectives:
        "red", "busy", "tiny", "blue", "large", "fluffy", "shiny", "tall", "smart", "fast"
    Return: a randomly chosen adjective.
    """
    words = ["red", "busy", "tiny", "blue", "large", "fluffy", "shiny", "tall", "smart", "fast"]
    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

main()