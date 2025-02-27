
import pytest
from main import primo

def test_primo():
    assert primo(2) == True
    assert primo(3) == True
    assert primo(7) == True
    assert primo(8) == False
    assert primo(9) == False
    