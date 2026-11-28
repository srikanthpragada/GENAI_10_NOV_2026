# Create Account class with acno, customer, balance attribues and deposit, withdraw and getbalance methods.

class Account:
    """Represent a bank account and provide basic balance operations.

    Args:
        acno: The unique account number.
        customer: The customer associated with the account.
        balance: The initial balance. It must be a non-negative number.
    """

    def __init__(self, acno, customer, balance=0):
        """Initialize an account with an account number, customer, and balance.

        Raises:
            ValueError: If the account number or customer is missing, or the balance is negative.
            TypeError: If the balance is not a number.
        """
        if acno is None:
            raise ValueError("Account number is required.")
        if customer is None:
            raise ValueError("Customer is required.")
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise TypeError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account.

        Args:
            amount: The positive number to add to the balance.

        Raises:
            TypeError: If amount is not a number.
            ValueError: If amount is not positive.
        """
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        """Withdraw a positive amount when sufficient funds are available.

        Args:
            amount: The positive number to subtract from the balance.

        Raises:
            TypeError: If amount is not a number.
            ValueError: If amount is not positive or exceeds the balance.
        """
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Withdrawal amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        """Return the account's current balance.

        Returns:
            The current balance as a number.
        """
        return self.balance
