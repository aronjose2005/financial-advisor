import pytest
from src.financial_advisor import generate_financial_advice

def test_generate_financial_advice():
    advice = generate_financial_advice("Should I invest now?", sentiment_score=0.7)
    assert isinstance(advice, str)
    assert len(advice) > 0
