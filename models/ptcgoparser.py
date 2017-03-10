# Uses PTCGO decklist (old or new, tries to cater both needs) to build a proxy
# deck

# For example samples/sample.dec

from patterns import PTCGOPattern
from sets import PTCGO_SETS
from abstractparser import AbstractParser


class PTCGOParser(AbstractParser):
    """Parser to parse PTCGO deck lists."""

    def __init__(self, decklist):
        super(PTCGOParser, self).__init__()
        self.raw_decklist = decklist
        self.decklist = []
        self.errors = []

    def run(self):
        self.pre_parse()
        self.search()
        self.html()

    def pre_parse(self):
        self.parse_raw_decklist()

    # PTCGO specific methods
    def parse_raw_decklist(self):
        for line in self.raw_decklist.split('\n'):
            try:
                line = line.strip()
                match = PTCGOPattern.SET_CARD_PATTERN.match(line)
                if match:
                    quantity, set_name, set_nro = match.groups()
                    try:
                        set_name = PTCGO_SETS[set_name]
                        self.decklist.append(((set_name, set_nro), int(quantity)))
                    except KeyError:
                        is_energy = PTCGOPattern.BASIC_ENERGY_PATTERN.match(line)
                        quantity, energy_name = is_energy.groups()
                        self.decklist.append(((energy_name, None), int(quantity)))
                else:
                    is_energy = PTCGOPattern.BASIC_ENERGY_PATTERN.match(line)
                    if is_energy:
                        quantity, energy_name = is_energy.groups()
                        self.decklist.append(((energy_name, None), int(quantity)))
            except:
                self.errors.append(line)

