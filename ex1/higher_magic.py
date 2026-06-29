from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal {target}"


def fire(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def Condition(target: str, power: int) -> bool:
    if power > 20:
        return True
    else:
        return False


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def spell(target: str, power: int) -> tuple:
        first = spell1(target, power)
        second = spell2(target, power)
        return (first, second)
    return (spell)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifire(target: str, power: int) -> Callable:
        Amplified = power * multiplier
        print(f"Original: {power}, Amplified: {Amplified}")
        return (base_spell(target, Amplified))
    return (amplifire)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def guarded_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return (guarded_spell)


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_list(target: str, power: int) -> list:
        spell_list = []
        for spell in spells:
            spell_list.append(spell(target, power))
        return (spell_list)
    return (cast_list)


if __name__ == "__main__":
    mega_spell = spell_combiner(fire, heal)
    final_out = mega_spell("Dragon", 20)
    print("Testing spell combiner...")
    print(f"Combined spell result: {" ".join(final_out)}")
    print("Testing power amplifier...")
    amp_spell = power_amplifier(heal, 5)
    amp_massege = amp_spell("Dragon", 15)
    print("Testing conditional caster...")
    example3 = conditional_caster(Condition, heal)
    new_output = example3("Dragon", 25)
    print(new_output)
    print("Testing spell sequence...")
    sequence = spell_sequence([heal, fire])
    final_out = sequence("Dragon", 25)
    print(" ".join(final_out))
