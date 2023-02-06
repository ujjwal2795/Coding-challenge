def get_value_from_nested_object(obj, key):
    keys = key.split("/")
    for k in keys:
        obj = obj.get(k)
        if obj is None:
            return None
    return obj

# Example usage
nested_object = {"a": {"b": {"c": "d"}}}
key = "a/b/c"
value = get_value_from_nested_object(nested_object, key)
print(f"Key: {key}, Value: {value}") # Output: Key: a/b/c, Value: d

nested_object = {"x": {"y": {"z": "a"}}}
key = "x/y/z"
value = get_value_from_nested_object(nested_object, key)
print(f"Key: {key}, Value: {value}") # Output: Key: x/y/z, Value: a

nested_object = {"x": {"y": {"z": "a"}}}
key = "x/y/w"
value = get_value_from_nested_object(nested_object, key)
print(f"Key: {key}, Value: {value}") # Output: Key: x/y/w, Value: None

nested_object = {"x": {"y": {"z": {"w": {"u": "v"}}}}}
key = "x/y/z/w/u"
value = get_value_from_nested_object(nested_object, key)
print(f"Key: {key}, Value: {value}") # Output: Key: x/y/z/w/u, Value: v

nested_object = {}
key = "x/y/z"
value = get_value_from_nested_object(nested_object, key)
print(f"Key: {key}, Value: {value}") # Output: Key: x/y/z, Value: None
