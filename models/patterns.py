# Collection of regex patterns used in parsers

import re


class PTCGOPattern(object):
    BASIC_ENERGY_PATTERN = re.compile(r'(?:\* )?(\d+) (Grass|Lightning|Fire|Fairy|Darkness|Metal|Fighting|Psychic|Water)')
    SET_CARD_PATTERN = re.compile(r'(?:\* )?(\d+) .* ([A-Z]{2,3}|[A-Z]{2}-[A-Z]{2}|[A-Z0-9]{3})? (\d+|XY\d+|BW\d+)')

