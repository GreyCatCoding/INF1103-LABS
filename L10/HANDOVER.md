# Handover log: INF1103 Labs – Inventory Management System

## 2026-11-11

### Summary
Started Lab 8 in `L10/`. Built a `Supplier` class and linked every product to a supplier. Stopped while updating the menu (`main_program.py`) and the save/load code (`inventory.py`) so they also handle suppliers.

### What I did
- Turned the "get" methods into properties, so I write `product.price` instead of `product.get_price()`.
- Made a new `Supplier` class with an ID, name and email. Its details can be read but not changed from outside.
- Gave every product a supplier when it is created, and a way to look it up: `product.supplier`.
- Fixed a bug where digital products couldn't be created because a required method had the wrong name.
- Added type hints, small labels that say what type each value should be.
- Wrote my first pytest tests to check that a product remembers its supplier.

### Key ideas to remember

**Three ways objects relate.** Ask: *"If the whole goes away, what happens to the part?"*

| Relationship | Plain meaning | Everyday example | In my lab |
|---|---|---|---|
| Association | They know each other, nobody owns anybody | A customer and their mechanic | Product ↔ Supplier |
| Aggregation | A group that holds things it didn't make | A playlist holds songs; delete the playlist and the songs remain | Inventory ◇ Product |
| Composition | It builds its own parts, and they disappear with it | A robot's brain goes when the robot goes | Order ◆ OrderLine |

**Properties.** They look like a normal value (`product.price`) but quietly run a small method, so the data stays protected. With no setter, a value can be read but not changed.

**Type hints.** Notes saying what type something should be (`price: float`). Python doesn't enforce them, but VS Code underlines mistakes. Put them where something is *defined*, not where it is *used*.

**Names vs objects.** A variable is a name tag on an object, not the object itself. `del` removes the tag, not the object. If two products point at the same supplier, both still work after one tag is deleted.

**Inherit vs implement.**
- Inherit means "is a": a digital product *is a* product.
- Implement means "can do": a physical product *can be shipped*.

**Abstract methods are promises.** If the parent says "every product must have `get_fulfilment_info()`", each child must use exactly that name, or Python refuses to create it.

### Good habits I applied
- **One job per class:** `Supplier` only describes a supplier.
- **Keep classes loosely linked:** the product knows its supplier, but the supplier doesn't track products.
- **Children keep the parent's promises (LSP):** same method names and return types.
- **Protect data:** private attributes, readable through properties.
- **Predict first, then run:** write down what I expect before testing.
- **One class per file.**

### Next time
1. Fix the small typing mistakes that stop `inventory.py` and `main_program.py` from running.
2. Ask the user for supplier details in the menu, and create a `Supplier` before making the product.
3. Save and load suppliers in the JSON file, with products from the same supplier sharing one supplier object.
4. Add tests showing two products share one supplier, and that it survives `del`.
5. Then Section 3: Inventory (add, remove, find products).
