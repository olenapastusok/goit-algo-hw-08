import heapq

def minimize_connection_costs(cables):
    if not cables:
        return 0    
    if len(cables) == 1:
        return cables[0]

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6]
print("Minimum connection cost:", minimize_connection_costs(cables))