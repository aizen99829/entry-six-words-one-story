"""Write the six-word story to /output/entry.txt.

The story: "He sold the piano. She sang."
Six words, twenty-eight bytes, no trailing newline. He takes the piano;
her voice answers anyway. Every word earns its place.
"""

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("He sold the piano. She sang.")
