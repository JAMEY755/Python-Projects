class Account:
    """A helper class to maintain a shared balance across transaction instances."""

    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        self.balance = initial_balance


class Transaction:

    def __init__(self, account: Account):
        self.account = account  # Reference to the shared account object

    def execute(self, *args):
        print("Executing a generic transaction...")


class Deposit(Transaction):
    # Method Overriding: Specialized execution for deposits
    # Method Overloading: Can handle (amount) or (amount, bonus_code)
    def execute(self, *args):
        if not args:
            print("Error: Specify a deposit amount.")
            return

        amount = args[0]
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        # Overloaded behavior check
        if len(args) == 2 and args[1] == "COMPANY_BONUS":
            bonus = 500.0
            self.account.balance += amount + bonus
            print(
                f"[Deposit] Employer deposited payroll ${amount} + ${bonus} Corporate Bonus. New Balance: ${self.account.balance}"
            )
        else:
            self.account.balance += amount
            print(
                f"[Deposit] Deposited ${amount}. New Balance: ${self.account.balance}"
            )


class Withdrawal(Transaction):
    # Method Overriding: Specialized execution for withdrawals
    def execute(self, *args):
        if not args:
            print("Error: Specify a withdrawal amount.")
            return

        amount = args[0]
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if amount > self.account.balance:
            print(
                f"[Withdrawal] Denied! Insufficient funds. Available: ${self.account.balance}"
            )
        else:
            self.account.balance -= amount
            print(
                f"[Withdrawal] Employer withdrew ${amount} for office cash. New Balance: ${self.account.balance}"
            )


class Transfer(Transaction):
    # Method Overriding: Specialized execution for transfers
    # Method Overloading: Expects (amount, target_recipient)
    def execute(self, *args):
        if len(args) < 2:
            print("Error: Transfer requires both an amount and a recipient name.")
            return

        amount = args[0]
        recipient = args[1]

        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if amount > self.account.balance:
            print(
                f"[Transfer] Failed! Unable to send ${amount} to {recipient} due to insufficient funds."
            )
        else:
            self.account.balance -= amount
            print(
                f"[Transfer] Successfully transferred ${amount} to Employee ({recipient}). New Balance: ${self.account.balance}"
            )


# --- Simulating the Employer Managing Funds ---

# 1. Initialize the Employer's Corporate Account
employer_account = Account("MegaCorp CEO", 5000.0)
print(
    f"Initial Account Balance for {employer_account.owner}: ${employer_account.balance}"
)

# 2. Employer executes a Deposit (with an overloaded corporate bonus parameter)
deposit_runner = Deposit(employer_account)
deposit_runner.execute(10000.0, "COMPANY_BONUS")

# 3. Employer executes a Transfer to pay an employee's salary
transfer_runner = Transfer(employer_account)
transfer_runner.execute(3500.0, "Alice Smith (Lead Developer)")

# 4. Employer executes a Withdrawal for petty cash expenses
withdraw_runner = Withdrawal(employer_account)
withdraw_runner.execute(450.0)

# 5. Employer attempts an invalid transaction to test boundary validations
withdraw_runner.execute(20000.0)