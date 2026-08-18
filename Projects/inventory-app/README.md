# Inventory App

A command-line inventory manager built with an OOP design that separates
pure logic from user interaction: `Item` and `Inventory` hold zero
`input()`/`print()` calls between them, so the same classes back the CLI,
the test suite, and JSON persistence with no changes needed to either.

## Features

- Add, remove, and search for items by name
- List everything currently in the inventory
- Running total value across all items
- Save/load the inventory to/from a JSON file, so it survives between runs

## Design

```
item.py       Item: pure data + behavior for a single item (name, price, quantity)
inventory.py  Inventory: holds Items via composition (a list, not inheritance),
              manages add/remove/find/total, and JSON persistence
cli.py        The only file that talks to the user - owns the menu loop,
              delegates every real decision to Inventory/Item
test_inventory.py  pytest suite against Item/Inventory's logic directly
```

`Inventory` composes `Item`s rather than inheriting from `Item`, since an
inventory *contains* items - it isn't a more specific kind of item itself.

## Running it

```
python cli.py
```

Follow the menu prompts to add items, look one up, remove one, check the
total value, or save/load your inventory to a JSON file.

## Running the tests

```
pytest test_inventory.py
```

## Example

```
What would you like to do?
1. Add item
2. Remove item
3. Find item
4. List all items
5. Show total value
6. Save to file
7. Load from file
8. Quit
Choose an option: 1
What's the item called? Taco
How much does it cost? $3.00
How many do you have? 5
Got it, added Taco to your inventory.
```
