from cable_connection import min_cost_to_connect_cables, CableConnectionError
from merge_k_lists import merge_k_lists, MergeListsError

def main():
    # Тестуємо з'єднання кабелів
    try:
        cables = [4, 3, 2, 6]
        print("Мінімальна вартість з'єднання кабелів:", min_cost_to_connect_cables(cables))
    except CableConnectionError as e:
        print("Помилка:", e)

    # Тестуємо злиття відсортованих списків
    try:
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        merged_list = merge_k_lists(lists)
        print("Відсортований список:", merged_list)
    except MergeListsError as e:
        print("Помилка:", e)

if __name__ == "__main__":
    main()
