# -*- coding: utf-8 -*-
from helpers import get_answer

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if get_answer():
        print("whoohoo!")
        print(get_hmm())
