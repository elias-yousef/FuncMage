from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def new_func(spell1: Callable, spell2: Callable) -> Callable:
        spell1()
        spell2()
    return (new_func)

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    pass
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass
def spell_sequence(spells: list[Callable]) -> Callable:
    pass
