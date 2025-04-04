var1="Ram"
print(f"var1={var1}, type={type(var1)} , Address={id(var1)}")
var2="Ram"
print(f"var2={var2}, type={type(var2)} , Address={id(var2)}")
print(f"var1 is var2={var1 is var2}")
var1="Mam"
print(f"var1={var1}, type={type(var1)} , Address={id(var1)} - CHANGED")
print(f"var1 is not var2={var1 is not var2}")
var3="Mam"
print(f"var3={var3}, type={type(var3)} , Address={id(var3)}")
print(f"var1 is var3={var1 is var3}")