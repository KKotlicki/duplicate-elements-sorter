from collections import Counter


def get_ordered_duplicates(lst):
    """
    Finds all duplicate elements in a list and returns them in the order of their first occurrence.

    Args:
        lst (list): The input list to check for duplicates. Can contain elements of any hashable type.

    Returns:
        list: A list of elements that appear more than once in the original list, 
              sorted in the order of their first appearance.
    """
    
    ### Imperative approach:
    
    if False:
        seen = {}
        result = []

        for i, item in enumerate(lst):
            if item in seen:
                if seen[item] == 1:
                    result.append(item)
                seen[item] += 1
            else:
                seen[item] = 1

        result.sort(key=lambda x: lst.index(x))
        return result
    
    ### Declarative approach:
    
    if True:
        counts = Counter(lst)
        return [item for item in counts if counts[item] > 1]
