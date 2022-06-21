from pay.processor import PaymentProcessor
import pytest

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"
CARD_NUM = "1249190007575069"


def test_payment_processor_invalid_api_key_raises_value_error() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card=CARD_NUM, month=12, year=2024, amount=2)


def test_payment_processor_invalid_card_raises_value_error() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card="123", month=12, year=2024, amount=2)


def test_payment_processor_invalid_date_raises_value_error() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(card=CARD_NUM, month=12, year=2020, amount=2)


def test_payment_processor_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card=CARD_NUM, month=12, year=2024, amount=2)
