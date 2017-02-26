# Collection of regex patterns used in parsers

import re


class BulbapediaPattern(object):
    QUANTITY_PATTERN = re.compile(r' *([0-9]+).*')
    CARD_PATTERN = re.compile(r'.*\(([A-Za-z& ]+) (\d+)\)')

class PTCGOPattern(object):
    BASIC_ENERGY_PATTERN = re.compile(r'(?:\* )?(\d+) (Grass|Lightning|Fire|Fairy|Darkness|Metal|Fighting|Psychic|Water)')
    SET_CARD_PATTERN = re.compile(r'(?:\* )?(\d+) .* ([A-Z]{2,3}|[A-Z]{2}-[A-Z]{2})? (\d+|XY\d+|BW\d+)')

class TCGOnePattern(object):
    SET_CARD_PATTERN = re.compile(r'(\d+) .* \(([A-Z]{2,3}) (\d+)\)')

