class LegendaryFarming:
    def __init__(self):
        self.special_materials = {
            'shards': 0,
            'fragments': 0,
            'motes': 0
        }

        self.legendary_item_by_material = {
            'shards': 'Shadowmourne',
            'fragments': 'Valanyr',
            'motes': 'Dragonwrath'
        }

        self.junk_materials = {}

        self.crafted = False

    def farm(self):
        while not self.crafted:
            line = input()
            materials = line.split()
            for idx in range(0, len(materials) - 1, 2):
                quantity = int(materials[idx])
                material = materials[idx + 1].lower()

                if material in self.special_materials:
                    self.special_materials[material] += quantity
                    if self.special_materials[material] >= 250:
                        self.special_materials[material] -= 250
                        self.crafted = True
                        print(f"{self.legendary_item_by_material[material].title()} obtained!")
                        break
                else:
                    if material in self.junk_materials:
                        self.junk_materials[material] += quantity
                    else:
                        self.junk_materials[material] = quantity

    def print_results(self):
        for material, count in self.special_materials.items():
            print(f"{material}: {count}")

        for material, count in self.junk_materials.items():
            print(f"{material}: {count}")


lf = LegendaryFarming()
lf.farm()
lf.print_results()
