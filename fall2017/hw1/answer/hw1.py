def long_words(text, n):
    """Return the words in text that are longer than n.

    Parameters:
    text: str -- the text of interest

    Return: Sequence[int] -- words in text that are longer than n

    Usage Examples:
    >>> long_words('I do not write good', 3)
    ['write', 'good']
    """
    return list(filter(lambda s: len(s) > n, text.split()))

def num_long_words(text, n):
    """Return the number of words in text that are longer than n.

    Parameters:
    text: str -- the text of interest

    Return: int -- the number of words in text that are longer than n

    Usage Examples:
    >>> num_long_words('I do not write good', 3)
    2
    """
    return count_if(text.split(), lambda s: len(s) > n)

def count_if(sequence, predicate):
    """Count the number of elements in sequence that satisfy predicate function.

    Parameters:
    sequence: Sequence -- a sequence of elements of any type
    predicate: Function: Any -> bool -- a function that takes a single parameter and returns a
    bool

    Usage Examples:
    >>> count_if([0, 1, 2, 3, 4], lambda x: x % 2 == 0)
    3
    >>> count_if(['fe', 'fi', 'fo', 'fum'], lambda s: len(s) > 2)
    1
    """
    return len(list(filter(predicate, sequence)))

def make_tups(seq1, seq2):
    """Convert seq1 and seq2 to a list of tuples with corresponding elements of
    seq1 and seq2.

    Parameters:
    seq1: Sequence[Any] -- a sequence of elements of any type
    seq2: Sequence[Any] -- a sequence of elements of any type

    Return: Sequence[(Any, Any)] - a sequence of 2-tuples where the ith tuples
    contain the ith elements of seq1 and seq2. Length of returned list is
    length of shortest input seq

    Usage Examples:
    >>> make_tups(['a', 'b', 'c', 'd'], [1, 2, 3])
    [('a', 1), ('b', 2), ('c', 3)]
    """
    return list(zip(seq1, seq2))
