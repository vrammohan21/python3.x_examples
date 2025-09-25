gl_var="I am EVREY_WHERE"#Global

def sample_func():
    lo_var="I exist ONLY in the func"#LOCAL

    print(f"Global VARIABLE: {gl_var}")
    print(f"LOCAL variable: {lo_var}")

    def inner():
        nl_var="I am NON-LOCAL"
        print("Value of nl_var = {}".format(nl_var))
    #print("Value of nl_var = {}".format(nl_var))
    inner()
sample_func()
print(f"Global={gl_var}")
#print(f"Sorry to disturb you :{lo_var}")