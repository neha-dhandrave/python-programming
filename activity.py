def lists_are_equal(list1, list2):
    """
    Compare two lists and return True if they are equal (same elements in the same order),
    otherwise return False.
    """
    return list1 == list2

# Example usage
if __name__ == "__main__":
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = [3, 2, 1]
    list_d = [1, 2]

    print(f"Are {list_a} and {list_b} equal? -> {lists_are_equal(list_a, list_b)}")  # True
    print(f"Are {list_a} and {list_c} equal? -> {lists_are_equal(list_a, list_c)}")  # False
    print(f"Are {list_a} and {list_d} equal? -> {lists_are_equal(list_a, list_d)}")  # False
