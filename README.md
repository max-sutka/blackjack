# Blackjack (Python CLI)

A simple command-line blackjack game I built in Python. Nothing fancy. Just deal cards, hit or stand, try not to bust, and keep your chips.

## Why I made this

I needed a small project for a class to practice basic game logic in Python: tracking state (chips, hands, scores), handling user input without crashing, and dealing with edge cases like aces being worth 1 or 11 depending on the hand. Blackjack turned out to be a good fit for that.

## How to play

Just run the script with Python 3:

```bash
python blackjack.py
```

You'll start with 500 chips. Each round:

1. Place a bet
2. Get dealt two cards
3. Choose to `hit` (draw another card) or `stand` (keep your hand)
4. The dealer plays according to standard rules (draws until 17+)
5. Win, lose, or push based on who's closer to 21 without busting

Get a blackjack (21 on the deal), and you get paid out 3:2 automatically.

After each round, you'll be asked if you want to play again. Enter `y` to keep going, anything else to quit.

## Rules it follows

- Face cards (J/Q/K) are worth 10
- Aces are worth 11, unless that would bust your hand, in which case they count as 1
- Dealer hits until reaching 17 or higher
- Standard payouts: 1:1 for a normal win, 3:2 for blackjack, push returns your bet

## Notes / known limitations

- This is a single-deck-per-shuffle style setup. Cards aren't tracked as "removed" from the deck, so in theory the same card could come up more than once in a hand. Not exactly casino-accurate, but it keeps the logic simple.
- No splitting, doubling down, or insurance yet. Could be fun to add later.
- Everything runs in the terminal. No GUI.

## Possible future additions

- [ ] Splitting pairs
- [ ] Doubling down
- [ ] Persistent chip balance between sessions
- [ ] Basic betting strategy stats/tracking

## Requirements

Just Python 3 — no external libraries needed.

---
