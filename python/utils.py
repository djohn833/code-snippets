import itertools


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
    numSlices = (len(collection) + sliceSize) // sliceSize # round up
    for i in range(numSlices):
        yield collection[i * sliceSize : (i+1) * sliceSize]

