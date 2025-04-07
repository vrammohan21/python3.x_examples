name="Python"#GLOBAL SCOPE
def outer_func():
    print("Hello, World!")
    name="Java"#MODIFIED -> this value is only in the function scope.
    print(f"\tOUTER name={name}")
    def inner_function():
        name="DS"
        return name
        #print(f"\t#8INNER: name={name}")
    return inner_function()

print(f"\t#12 {outer_func()}")
name=outer_func()
print(f"\tlast name={name}")