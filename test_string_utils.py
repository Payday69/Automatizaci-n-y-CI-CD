import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.string_utils import capitalize_words, reverse_text

def test_capitalize_words():
    assert capitalize_words("hola mundo") == "Hola Mundo"

def test_reverse_text():
    assert reverse_text("abcd") == "dcba"
