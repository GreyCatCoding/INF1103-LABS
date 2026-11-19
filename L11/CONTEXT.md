# INF1103 Lab 9 – Design Patterns and Error Handling

## Goal
Extend the Lab 8 Inventory Management System (copied from L10/) with the
Strategy and Factory patterns, validation, exception handling and automated tests.

## Requirements
- DiscountStrategy (ABC, given by the brief) with apply(total) -> float.
  Strategies: NoDiscount, PercentageDiscount(percentage), BulkDiscount(threshold, amount),
  plus one strategy of my own (e.g. StudentDiscount).
- Order takes a DiscountStrategy when created (default NoDiscount()), has set_discount(),
  and calculate_total() passes the sum of its line subtotals to strategy.apply().
  Order contains no discount if/elif logic.
- ProductFactory with a static create(product_type, ...) -> Product.
  Unknown product type raises ValueError with a clear message.
  Direct product creation elsewhere is replaced by ProductFactory.create().
- Validation raising ValueError, placed in the class that owns the rule:
  price > 0 and stock >= 0 (Product), OrderLine quantity > 0.
- get_positive_float(prompt): keeps asking until it gets a valid positive number;
  handles ValueError from float() and from validation.
- load_products(path, inventory, supplier): reads products.csv (exactly as given in the brief)
  using try/except/else/finally. Missing file is reported, bad rows are reported and skipped,
  prints how many loaded, finally prints "Load attempt finished."
- Tests in tests/ covering the Section 7 checklist. Each except catches a specific exception.
- Deliverables: Predict-first notes (Word, written by me), Python source and tests,
  updated UML class diagram (Strategy, Factory, Order–DiscountStrategy multiplicities,
  dashed «creates» arrow from ProductFactory to Product), Git and Docker screenshot.

## Out of scope
- Changing Lab 8 relationships beyond what the brief asks.
- Writing my Predict-first answers for me (Claude may check them).

## Stack and environment
Python 3.14, pytest, Docker (same workflow as L10). Windows laptop.

## Structure
- L11/ : Lab 9 code, copied from L10/
- L11/tests/ : pytest tests
- One class per file (lecture rule)

## Constraints
- No new dependencies beyond the standard library and pytest.
- Git is handled by me.

## Decisions so far
- Lab 9 lives in L11/, copied from L10/.

## Open questions
- Constructor mismatch: PhysicalProduct, DigitalProduct and SubscriptionProduct each take
  one extra argument (weight, download_size, duration), but products.csv has only 5 columns.
  Options: (a) default values on the extra arguments, (b) factory takes one optional extra
  value and passes it on, (c) add a column to the CSV. Recommended: (b).
- Dockerfile, .dockerignore, .gitignore and inventory.json were not copied from L10/ yet.
