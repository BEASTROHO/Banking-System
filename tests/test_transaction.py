import pytest
from modules.transactions import deposit, withdraw, transfer

def test_deposit():
    balance = deposit(1000, 500)
    assert balance == 1500

def test_withdraw_success():
    balance = withdraw(1000, 400)
    assert balance == 600

def test_withdraw_insufficient_funds():
    with pytest.raises(ValueError):
        withdraw(300, 500)

def test_transfer_success():
    sender, receiver = transfer(1000, 500, 200)
    assert sender == 800 and receiver == 700

def test_transfer_insufficient_funds():
    with pytest.raises(ValueError):
        transfer(100, 500, 200)
