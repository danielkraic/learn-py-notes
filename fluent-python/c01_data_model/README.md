# python data model

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

len(deck)

deck[0]
deck[-1]
deck[1:5]
deck[-4:]

from random import choice
choice(deck)


for item in deck:
    print(item)

for item in reversed(deck):
    print(item)

Card('Q', 'hearts') in deck
```

```python
class Vector:
    def __init__(self):
        


```