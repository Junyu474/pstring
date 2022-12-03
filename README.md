# PString
_Pretty String for Python_

Use __method chaining__ to add __color, style, and background__ to your strings.

```python
from pstring import PString as ps

# Red color, green background, bold, underline
ps('Hello World').r().bg_g().bold().underline()

# in any order
ps('Hello World').bold().underline().r().bg_g()
```