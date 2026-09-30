# Assignment 5: PAN Number validation using Regular Expression
import re

# Format: 5 uppercase letters + 4 digits + 1 uppercase letter  (AAAAA9999A)
PAN_PATTERN = r"^[A-Z]{5}[0-9]{4}[A-Z]$"


def is_valid_pan(pan):
    return re.fullmatch(PAN_PATTERN, pan) is not None


pan = input("Enter PAN number: ").strip()

if is_valid_pan(pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")

# Test cases from the assignment:
# ABCDE1234F -> Valid PAN Number
# ABCD@1234F -> Invalid PAN Number
# ABCDE12345 -> Invalid PAN Number
