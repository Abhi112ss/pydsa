METADATA = {
    "id": 2043,
    "name": "Simple Bank System",
    "slug": "simple-bank-system",
    "category": "Simulation",
    "aliases": [],
    "tags": ["hash_map", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Implement a bank system that supports transfers, deposits, and withdrawals using account IDs.",
}

class Bank:
    def __init__(self, accounts: list[int]):
        """
        Initializes the bank with a list of account balances.

        Args:
            accounts: A list of integers representing initial balances for each account.
        """
        # Use a dictionary for O(1) average time complexity for lookups and updates
        self.account_balances: dict[int, int] = {i: balance for i, balance in enumerate(accounts)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfers money from account1 to account2.

        Args:
            account1: The ID of the source account.
            account2: The ID of the destination account.
            money: The amount of money to transfer.

        Returns:
            True if the transfer was successful, False otherwise.
        """
        # Check if both accounts exist and if account1 has sufficient funds
        if (account1 in self.account_balances and 
            account2 in self.account_balances and 
            self.account_balances[account1] >= money):
            
            self.account_balances[account1] -= money
            self.account_balances[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposits money into the specified account.

        Args:
            account: The ID of the account.
            money: The amount of money to deposit.

        Returns:
            True if the deposit was successful, False otherwise.
        """
        if account in self.account_balances:
            self.account_balances[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        """
        Withdraws money from the specified account.

        Args:
            account: The ID of the account.
            money: The amount of money to withdraw.

        Returns:
            True if the withdrawal was successful, False otherwise.
        """
        # Check if account exists and has enough balance
        if account in self.account_balances and self.account_balances[account] >= money:
            self.account_balances[account] -= money
            return True
        return False


def solve():
    """
    Example usage of the Bank class.
    """
    bank = Bank([10, 20])
    print(bank.transfer(0, 1, 5))    # Expected: True
    print(bank.transfer(1, 0, 25))   # Expected: False
    print(bank.deposit(1, 10))       # Expected: True
    print(bank.withdraw(0, 15))      # Expected: False
    print(bank.withdraw(1, 15))      # Expected: True
