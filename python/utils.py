def slices(collection, sliceSize):
    """Iterate over a collection, sliceSize items at a time.

    >>> for s in slices('abcdefgh', 3):
    ...     print(s)
    abc
    def
    gh

    Args:
        collection: collection to loop over.
        sliceSize: size of each slice.

    Returns:
        A generator for iterating over the slices.
    """
    for i in range(0, len(collection), sliceSize):
        yield collection[i:i + sliceSize]
