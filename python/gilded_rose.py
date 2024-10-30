# -*- coding: utf-8 -*-
SULFURAS_QUALITY = 80
MAX_QUALITY = 50
MIN_QUALITY = 0


class Names:
    BACKSTAGE_PASS = 'Backstage passes to a TAFKAL80ETC concert'
    SULFURAS = 'Sulfuras, Hand of Ragnaros'
    AGED_BRIE = 'Aged Brie'
    CONJURED = 'Conjured'


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == Names.SULFURAS:
                self.update_sulfuras(item)
            elif item.name == Names.AGED_BRIE:
                self.update_aged_brie(item)
            elif item.name == Names.BACKSTAGE_PASS:
                self.update_backstage_pass(item)
            elif item.name == Names.CONJURED:
                self.update_conjured_item(item)
            else:
                self.update_standard_item(item)

    def update_sulfuras(self, item):
        item.quality = SULFURAS_QUALITY

    def update_aged_brie(self, item):
        self.increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_backstage_pass(self, item):
        self.increase_quality(item)
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = MIN_QUALITY

    def update_conjured_item(self, item):
        self.decrease_quality(item, 2)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item, 2)

    def update_standard_item(self, item):
        self.decrease_quality(item)
        item.sell_in -= 1
        if item.sell_in < 0:
            self.decrease_quality(item)

    def increase_quality(self, item):
        if item.quality < MAX_QUALITY:
            item.quality += 1

    def decrease_quality(self, item, amount=1):
        item.quality = max(MIN_QUALITY, item.quality - amount)

