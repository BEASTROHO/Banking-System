import pytest
from modules.auth import login_user, register_user

def test_valid_login():
    assert login_user("admin", "admin123") == True

def test_invalid_login():
    assert login_user("admin", "wrongpass") == False

def test_register_new_user():
    result = register_user("newuser", "newpass")
    assert result == True  # Assuming successful registration

def test_register_existing_user():
    register_user("existinguser", "pass123")
    result = register_user("existinguser", "pass123")
    assert result == False  # Should fail if user already exists
