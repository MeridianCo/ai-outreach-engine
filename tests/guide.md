## How to Run Tests

From the root directory (make sure your virtual environment is
activated):

``` bash
python3 -m pytest tests/[directory] -s
```

-   `-s` is optional --- use it if you want to see `print` statements.
-   Omit `-s` if you only care about which tests passed/failed.

### Example

``` bash
python3 -m pytest tests/supabase/test_queries.py
```

------------------------------------------------------------------------

## Test Structure

    tests/
    ├── followup/
    │   ├── integration/
    │   │   └── test_api.py
    │   └── static/
    │       └── test_api.py
    ├── supabase/
    │   └── test_queries.py

### Notes

-   **static/**\
    Uses static/mock JSON data. These are fast, isolated tests that do
    not depend on external services.

-   **integration/**\
    Fetches real data from the database (Supabase). These tests validate
    end-to-end behavior and may be slower.

-   **supabase/**\
    Contains tests specific to database queries and interactions.
