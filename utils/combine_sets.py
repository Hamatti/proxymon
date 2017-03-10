# Combines sets into one big json file

import json, os

this_files_dir = os.path.abspath(__file__)
parent_dir = os.path.abspath(os.path.join(this_files_dir, os.pardir, os.pardir))
local_storage_dir = os.path.join(parent_dir, 'local-storage')

outfile = open(os.path.join(local_storage_dir, 'all.json'), 'w')

all_cards = {}
for _, _, files in os.walk(local_storage_dir):
    for f in files:
        if f == 'all.json':
            continue
        fname = os.path.join(local_storage_dir, f)
        print fname
        data = open(fname).read()
        cards = json.loads(data)
        if not cards['cards']:
            continue
        for card in cards['cards']:
            try:
                all_cards[card['id']] = card['imageUrl']
            except Exception as e:
                try:
                    all_cards[card['id']] = card['imageUrl']
                except Exception as e2:
                    print card, e2.message

outfile.write(json.dumps(all_cards))
