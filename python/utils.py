#!/usr/bin/env python

def chunks(collection, chunkSize):
    """Iterate over a collection, chunkSize items at a time.

    >>> for s in chunks('abcdefgh', 3):
    ...     print(s)
    abc
    def
    gh

    Args:
        collection: collection to loop over.
        chunkSize: size of each chunk.

    Returns:
        A generator for iterating over the chunks.
    """
    
    for i in range(0, len(collection), chunkSize):
        yield collection[i:i + chunkSize]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
