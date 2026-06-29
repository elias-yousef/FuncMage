from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return (count)
    return (counter)


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return (total_power)
    return(accumulator)


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    stored_memory = {}
    def store(key: str, value: int) -> int:
        stored_memory[key] = value
        return f"Store {key} = {value}"
    def recall(key: str):
        if key in stored_memory:
            return stored_memory[key]
        else:
            return ("Memory not found")
    return({"store": store, "recall": recall})


if __name__ == "__main__":
    enchantment_types = ['Radiant', 'Shocking', 'Frozen']
    items_to_enchant = ['Shield', 'Cloak', 'Amulet', 'Ring']
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(2):
        counter_num = counter_a()
        print(f"counter_a call {i}: {counter_num}")
    counter_b = mage_counter()
    counter_num = counter_b()
    print(f"counter_b call {1}: {counter_num}")
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    added_power_a = accumulator(20)
    print(f"Base 100, add 20:  {added_power_a}")
    added_power_b = accumulator(30)
    print(f"Base 100, add 30:  {added_power_b}")
    print("\nTesting enchantment factory...")
    spell = enchantment_factory('Radiant')
    item = spell('Shield')
    print(item)
    spell = enchantment_factory('Flaming')
    item = spell('Sword')
    print(item)
    print("\nTesting memory vault...")
    memory = memory_vault()
    print(memory["store"]("secret", 42))
    print(f"Reacall 'secret' {memory['recall']('secret')}")
    print(f"Reacall 'unknown' {memory['recall']('unknown')}")
