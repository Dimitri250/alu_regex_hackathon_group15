#!/usr/bin/python3

import re

string = "The dates are 01-Jan-2022 and 31-Dec-2022."
pattern = r"\b(\d{2})-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(\d{4})\b"

matches = re.findall(pattern, string)
print(matches)

