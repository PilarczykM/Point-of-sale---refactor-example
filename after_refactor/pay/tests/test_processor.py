from datetime import datetime

from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor
import pytest
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""


@pytest.fixture
def card() -> CreditCard:
    return CreditCard("1249190007575069", 12, 2024)


@pytest.fixture
def card_invalid_num() -> CreditCard:
    return CreditCard("123", 12, datetime.now().year + 2)


@pytest.fixture
def card_invalid_date() -> CreditCard:
    return CreditCard("1249190007575069", 12, datetime.now().year - 2)


def test_payment_processor_invalid_api_key_raises_value_error(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card, amount=2)


def test_payment_processor_invalid_card_raises_value_error(card_invalid_num: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card_invalid_num, amount=2)


def test_payment_processor_invalid_date_raises_value_error(card_invalid_date: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card_invalid_date, amount=2)


def test_payment_processor_valid_date(card: CreditCard) -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card, amount=2)
