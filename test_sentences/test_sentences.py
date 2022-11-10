from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", 'cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman', 'taco', 'duck', 'potato', 'tent', 'cow', 'bone', 'toe', 'student', 'robot', 'sandwich', 'spider', 'gorilla', 'pickle', 'pumpkin']
    for _ in range(5):
        assert get_noun(1) in single_nouns

    plural_nouns = ["birds", "boys", "cars", 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women', 'tacos', 'ducks', 'potatoes', 'tents', 'cows', 'bones', 'toes', 'students', 'robots', 'sandwiches', 'spiders', 'gorillas', 'pickles', 'pumpkins']
    for _ in range(5):
        assert get_noun(2) in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(5):
        assert get_verb(1, 'past') in past_verbs
        assert get_verb(1, 'present') in present_single_verbs
        assert get_verb(2, 'present') in present_plural_verbs
        assert get_verb(1, 'future') in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "over", "past", "to", "under", "with", "without"]

    for _ in range(5):
        assert get_preposition() in prepositions

def test_get_prepositional_phrase():
    for _ in range(5):
        assert get_prepositional_phrase(1).count(' ') == 2
        assert get_prepositional_phrase(2).count(' ') == 2
        assert get_prepositional_phrase(1,has_adverb=True).count(' ') == 3
        assert get_prepositional_phrase(1,has_adjective=True).count(' ') == 3
        assert get_prepositional_phrase(1,True,True).count(' ') == 4

def test_get_adjective():
    adjectives = ['big', 'popular', 'ancient', 'evil', 'salty', 'rich', 'blind', 'fuzzy', 'slimy', 'rough', 'slippery', 'small', 'annoying', 'young', 'beautiful', 'poor', 'prickly', 'cold', 'hot', 'unrecognizable', 'goth', 'new', 'metal', 'bionic', 'spoiled', 'tasty', 'hairy', 'shiny']
    for _ in range(5):
        assert get_adjective() in adjectives

def test_get_adverb():
    adverbs = ['awkwardly', 'slowly', 'insanely', 'hotly', 'possibly', 'nearly', 'understandably', 'incessantly', 'smugly', 'warmly', 'unnecessarily', 'ordinarily', 'abnormaly', 'adventurously', 'cheerfully', 'carelessly', 'briskly', 'arrogantly', 'zestily']
    for _ in range(5):
        assert get_adverb() in adverbs



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])