from bs4 import BeautifulSoup
import urllib
from tcg_api import API

from sets import ENERGIES


class AbstractParser(object):
    """Abstract parser for Pokemon TCG deck lists"""

    def __init__(self):
        self.decklist = []
        self.images = []
        self.full_html = ''
        self.api = API()
        self.IMG_TEMPLATE = '<img width="312" height="441" src="{img}" />'
        self.HTML_TEMPLATE = """
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

            <html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">

            <head profile="http://gmpg.org/xfn/11">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>Pokemon TCG Proxy Builder</title>
            <style type="text/css">
            body, html, img, a { border: none; margin: 0; padding: 0; }
            img { height: 309px; margin: 0 1px 1px 0; width: 225px; }
            img { height: 316px; margin: 0 1px 1px 0; width: 230px; }
            #back { display: block; font-family: 'Lucida Grande', sans-serif; font-size: 125%; padding: 10px; position: absolute; right: 0; top: 0; }
            @media print { #back { display: none; } }
            .footer {
                display: block;
                position: fixed;
                width: 100%;
                text-align: center;
                height: 50px;
                line-height: 50px;
                background: red;
                color: white;
                font-weight: 700;
                font-size: 20px;
                text-decoration: none;
                bottom: 0;
            }
            </style>
            </head>

            <body>
            </body>

            </html>
        """

    def pre_parse(self):
        pass

    def search(self):
        for playset in self.decklist:
            card, quantity = playset
            if card[1]:
                card_image = self.api.search(card)
            else:
                card_image = ENERGIES[card[0]]
            if not card_image:
                continue
            for _ in xrange(quantity):
                self.images.append(card_image)

    def html(self):
        images_html = ''
        for card in self.images:
            images_html += self.IMG_TEMPLATE.format(img=card)
        soup = BeautifulSoup(self.HTML_TEMPLATE, 'html.parser')
        body = soup.find('body')
        footer = '<a class="footer" href="javascript:window.print()">Print deck</a>'
        body.append(BeautifulSoup(images_html, 'html.parser'))
        body.append(BeautifulSoup(footer, 'html.parser'))
        self.full_html = str(soup)

    def run(self):
        pass
