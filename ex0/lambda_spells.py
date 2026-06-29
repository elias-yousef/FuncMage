from typing import Any


artifacts = [
            {'name': 'Storm Crown', 'power': 64, 'type': 'accessory'},
            {'name': 'Ice Wand', 'power': 96, 'type': 'focus'},
            {'name': 'Ice Wand', 'power': 79, 'type': 'focus'},
            {'name': 'Storm Crown', 'power': 80, 'type': 'accessory'}
              ]
mages = [
        {'name': 'Sage', 'power': 96, 'element': 'lightning'},
        {'name': 'Zara', 'power': 88, 'element': 'earth'},
        {'name': 'Ember', 'power': 56, 'element': 'lightning'},
        {'name': 'Kai', 'power': 58, 'element': 'ice'},
        {'name': 'Nova', 'power': 60, 'element': 'shadow'}
          ]
spells = ['tornado', 'shield', 'heal', 'earthquake']


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return (list(sorted(artifacts, key=lambda x: x['power'], reverse=True)))


def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    return (list(filter(lambda x: x['power'] >= min_power, mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda x: "* " + x + " * ", spells)))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    minimum = min(mages, key=lambda x: x['power'])['power']
    maximum = max(mages, key=lambda x: x['power'])['power']
    avg = maximum - minimum / len(mages)
    return (
        {'max_power': maximum,
         'min_power': minimum,
         'avg_power': round(avg, 2)}
        )


if __name__ == "__main__":
    print("Testing artifact sorter...")
    sorted_list = artifact_sorter(artifacts)
    print(f"{sorted_list[0]['name']} \
({sorted_list[0]['power']} power) comes before \
{sorted_list[1]['name']} ({sorted_list[1]['power']} power)")
    print("\nTesting power filter...")
    print(power_filter(mages, 60), '\n')
    print("\nTesting spell transformer...")
    list_spells = spell_transformer(spells)
    str_spells = "".join(list_spells)
    print(str_spells, '\n')
    print("\nTesting mage stats")
    print(mage_stats(mages))
