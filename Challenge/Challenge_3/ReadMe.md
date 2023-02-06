# Challenge 3

Here i have used python language to solve the code and tried to run it locally on VS code.

# Explaination

1. The function get_value_from_nested_object takes two arguments: the nested object obj and the key key in the format of key1/key2/key3.
2. The key string is split into a list of individual keys using the split method. For example, "x/y/z" becomes ["x", "y", "z"].
3. The function then loops through the list of keys. For each key k, it uses the get method to extract the value of the key from the nested object obj. The get method returns None if the key is not present in the object.
4. If the value is None, it means that the key is not present in the object, and the function returns None.
5. Finally, the function returns the value of the last key in the list.The code also includes several test cases that demonstrate how the function can be used. Each test case defines a nested object and a key, and then calls the get_value_from_nested_object function to extract the value of the key from the object. The result is printed for each test case.

