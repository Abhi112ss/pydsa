METADATA = {
    "id": 1801,
    "name": "Number of Orders in the Backlog",
    "slug": "number-of-orders-in-the-backlog",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Match buy and sell orders using priority queues to find the remaining backlog.",
}

import heapq

def solve(orders: list[list[int]]) -> list[int]:
    """
    Processes a list of buy and sell orders and returns the remaining backlog.

    Args:
        orders: A list of lists where each inner list is [type, price, quantity].
            type is 0 for buy orders and 1 for sell orders.

    Returns:
        A list of two integers: [remaining_buy_quantity, remaining_sell_quantity].

    Examples:
        >>> solve([[0, 10, 5], [1, 12, 5]])
        [5, 5]
        >>> solve([[0, 10, 5], [1, 8, 5]])
        [0, 0]
    """
    # Max-heap for buy orders (we want the highest price first).
    # Python's heapq is a min-heap, so we store negative prices.
    buy_orders: list[tuple[int, int]] = []
    
    # Min-heap for sell orders (we want the lowest price first).
    sell_orders: list[tuple[int, int]] = []

    for order_type, price, quantity in orders:
        if order_type == 0:  # Buy order
            if sell_orders and sell_orders[0][0] <= price:
                # Match with the cheapest available sell order
                while quantity > 0 and sell_orders and sell_orders[0][0] <= price:
                    sell_price, sell_qty = heapq.heappop(sell_orders)
                    if sell_qty > quantity:
                        heapq.heappush(sell_orders, (sell_price, sell_qty - quantity))
                        quantity = 0
                    else:
                        quantity -= sell_qty
            if quantity > 0:
                heapq.heappush(buy_orders, (-price, quantity))
        
        else:  # Sell order
            if buy_orders and (-buy_orders[0][0]) >= price:
                # Match with the most expensive available buy order
                while quantity > 0 and buy_orders and (-buy_orders[0][0]) >= price:
                    neg_buy_price, buy_qty = heapq.heappop(buy_orders)
                    buy_price = -neg_buy_price
                    if buy_qty > quantity:
                        heapq.heappush(buy_orders, (neg_buy_price, buy_qty - quantity))
                        quantity = 0
                    else:
                        quantity -= buy_qty
            if quantity > 0:
                heapq.heappush(sell_orders, (price, quantity))

    # Calculate total remaining quantities in the heaps
    remaining_buy_qty = sum(qty for price, qty in buy_orders)
    remaining_sell_qty = sum(qty for price, qty in sell_orders)

    return [remaining_buy_qty, remaining_sell_qty]
