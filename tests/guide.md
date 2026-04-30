## How to Run Tests

From the root directory (should be in venv):

``` bash
python3 -m pytest tests/[directory] -s
```

-   `-s` is optional --- use it if you want to see `print` statements.
-   Omit `-s` if you only care about which tests passed/failed.

### Example

``` bash
python3 -m pytest tests/supabase/test_queries.py
```
