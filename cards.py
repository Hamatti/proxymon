import json, os

outfile = open('cards/all.json', 'w')
all_cards = {}
for _, _, files in os.walk('cards'):
    for f in files:
        if f == 'all.json':
            continue
        fname = 'cards/%s' % f
        print fname
        data = open(fname).read()
        cards = json.loads(data)
        if not cards['cards']:
            continue
        for card in cards['cards']:
            try:
                all_cards[card['id']] = card['imageUrlHiRes']
            except Exception as e:
                try:
                    all_cards[card['id']] = card['imageUrl']
                except Exception as e2:
                    print card, e2.message

outfile.write(json.dumps(all_cards))
