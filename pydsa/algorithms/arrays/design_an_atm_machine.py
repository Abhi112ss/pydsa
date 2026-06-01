METADATA = {
    "id": 2241,
    "name": "Design an ATM Machine",
    "slug": "design-an-atm-machine",
    "category": "Design",
    "aliases": [],
    "tags": ["simulation", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design an ATM machine that supports depositing money and withdrawing money using specific denominations.",
}

class ATM:
    def __init__(self, banknotes: list[int]):
        """
        Initializes the ATM with the given denominations.
        
        Args:
            banknotes: A list of integers representing the initial count of each denomination.
                      banknotes[i] is the count of the (i+1)-th denomination.
                      The denominations are always [10, 50, 100, 500, 1000].
        """
        # The problem guarantees denominations are [10, 50, 100, 500, 1000]
        self.denominations = [10, 50, 100, 500, 1000]
        # Store counts in a list where index i corresponds to self.denominations[i]
        self.counts = list(banknotes)

    def deposit(self, money: int, banknotes: list[int]) -> int:
        """
        Deposits money into the ATM.

        Args:
            money: The total amount of money to deposit.
            banknotes: A list of integers representing the count of each denomination.

        Returns:
            The total balance in the ATM after the deposit.
        """
        # Update the counts for each denomination provided in the deposit request
        for i in range(len(banknotes)):
            self.counts[i] += banknotes[i]
        
        # Calculate total balance by summing (denomination * count)
        total_balance = sum(self.denominations[i] * self.counts[i] for i in range(5))
        return total_balance

    def withdraw(self, amount: int, banknotes: list[int]) -> int:
        """
        Withdraws money from the ATM.

        Args:
            amount: The total amount of money to withdraw.
            banknotes: A list of integers representing the count of each denomination requested.

        Returns:
            The total balance in the ATM after the withdrawal, or -1 if withdrawal is impossible.
        """
        # First, check if the total requested amount matches the 'amount' parameter
        requested_total = sum(self.denominations[i] * banknotes[i] for i in range(5))
        if requested_total != amount:
            return -1

        # Second, check if the ATM has enough of each specific denomination requested
        for i in range(5):
            if self.counts[i] < banknotes[i]:
                return -1

        # If both checks pass, perform the actual withdrawal
        for i in range(5):
            self.counts[i] -= banknotes[i]

        # Calculate and return the new total balance
        total_balance = sum(self.denominations[i] * self.counts[i] for i in range(5))
        return total_balance

def solve():
    """
    Example usage of the ATM class.
    """
    # Initial counts for [10, 50, 100, 500, 1000]
    atm = ATM([0, 0, 0, 0, 0])
    
    # Deposit 10000: 10x1000, 0x500, 0x100, 0x50, 0x10
    print(atm.deposit(10000, [0, 0, 0, 0, 10]))  # Expected: 10000
    
    # Withdraw 1000: 1x1000, 0x500, 0x100, 0x50, 0x10
    print(atm.withdraw(1000, [0, 0, 0, 0, 1]))   # Expected: 9000
    
    # Withdraw 1000: 0x1000, 0x500, 0x100, 0x50, 0x10 (Invalid request total)
    print(atm.withdraw(1000, [0, 0, 0, 0, 0]))   # Expected: -1
    
    # Withdraw 1000: 0x1000, 0x500, 0x100, 0x50, 0x10 (Insufficient denominations)
    # Note: We only have 9x1000 left. If we ask for 10x100, it should fail if we don't have 100s.
    print(atm.withdraw(1000, [10, 0, 0, 0, 0]))  # Expected: -1 (only 10s requested, but we have 0 10s)
