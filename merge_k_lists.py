import heapq

class MergeListsError(Exception):
    """Користувацький виняток для помилок у процесі злиття списків."""
    pass

def merge_k_lists(lists):
    """
    Зливає k відсортованих списків в один відсортований список.

    :param lists: Список відсортованих списків.
    :return: Відсортований список.
    :raises MergeListsError: Якщо вхідні дані некоректні.
    """
    if not isinstance(lists, list):
        raise MergeListsError("Вхідні дані мають бути списком списків.")

    for lst in lists:
        if not isinstance(lst, list):
            raise MergeListsError("Кожен елемент має бути списком.")
        if not all(isinstance(x, (int, float)) for x in lst):
            raise MergeListsError("Усі елементи списків мають бути числами.")

    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged_list = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list
