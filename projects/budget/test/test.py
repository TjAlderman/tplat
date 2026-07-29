import pytest
from pathlib import Path
from budget.main import TransactionCategoriser


def test_budget():
    print("Testing the budget TransactionCategoriser class...")
    spending = TransactionCategoriser(Path(__file__).parent.parent/"docs/data/Transactions_2022-12-01_2023-05-03.csv")
    assert (spending.categorised['Groceries']-100<0.0001)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-s"]))