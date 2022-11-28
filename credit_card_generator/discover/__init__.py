from .. import generic

def generate(*args, **kwargs):
    return generic.generate_card(generic.CardType.Discover, *args, **kwargs)