from .. import generic


def generate(*args, **kwargs):
    return generic.generate_card(generic.CardType.MasterCard, *args, **kwargs)