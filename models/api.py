import json, re

CARDS_FILE = 'local-storage/all.json'


class API:

    def __init__(self):
        self.cards = json.loads(open(CARDS_FILE).read())
        self._card_count = len(self.cards)

    def search(self, card):
        card_set, card_nro = card
        try:
            return self.cards['%s-%s' % (card_set, card_nro)]
        except:
            if card == ('xy5', '163'):
                return self.cards['xy6-91']
            if card_set == 'g1' and int(card_nro) > 100: # These are Generations RC cards
                card_num = int(card_nro)
                card_num = 'rc' + str(card_num - 100)
                return self.cards['%s-%s' % (card_set, card_num)]
            if card_set == 'bw11' and int(card_nro) > 105:
                card_num = int(card_nro)
                if card_num == 140:
                    card_num = 126
                card_num = 'RC' + str(card_num - 115)
                return self.cards['%s-%s' % (card_set, card_num)]

            print "Not found: %s-%s" % card
            return '/static/images/tcg-not-found.png'

