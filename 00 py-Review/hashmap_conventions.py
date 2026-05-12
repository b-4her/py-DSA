# Safe/common keys:
# int
# str
# tuple
# object references
key = (1, 2)
value = "Hello"
default_value = None

# Creation
mp = {}

# Insert / Update
mp[key] = value

# Access
value = mp[key]

# Safe access (returns None if key doesn't exist)
value = mp.get(key)

# Safe access with default value
value = mp.get(key, default_value)

# Check if key exists
if key in mp:
    ...

# Iterate through keys
for key in mp:
    ...

# Iterate through values
for value in mp.values():
    ...

# Iterate through key-value pairs
for key, value in mp.items():
    ...

# Common interview naming conventions
freq = {}
seen = set()
memo = {}
old_to_copy = {}
index_map = {}