import heapq

class CableConnectionError(Exception):
    """Користувацький виняток для помилок у процесі з'єднання кабелів."""
    pass

def min_cost_to_connect_cables(cables):
    """
    Знаходить мінімальну вартість з'єднання мережевих кабелів.

    :param cables: Список довжин кабелів.
    :return: Мінімальна вартість з'єднання.
    :raises CableConnectionError: Якщо вхідні дані некоректні.
    """
    if not isinstance(cables, list):
        raise CableConnectionError("Вхідні дані мають бути списком.")

    if not all(isinstance(x, (int, float)) and x > 0 for x in cables):
        raise CableConnectionError("Усі довжини кабелів мають бути додатніми числами.")

    if len(cables) == 0:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost
