'''dict is a collection of key-value pairs.
Keys should be Unique & Only Immutable Objects are allowed as keys.'''
d1={1:"emp1",2:"emp2"}
d2={"TS":"Hyd","AP":"Amaravathi"}
#d3={{"TS","AP"}:"INDIA", {"NY","TX"}:"USA"}#Keys are sets
#d4={["TS","AP"]:"INDIA", ["NY","TX"]:"USA"}#keys are lists
d5={("TS","AP"):"INDIA", ("NY","TX"):"USA"}#keys are tuples
d6={frozenset({"TS","AP"}):"INDIA", frozenset({"NY","TX"}):"USA"}#Keys are sets
d7={3.14:"PI", 2.71:"Euler"}
print(f"d1={d1}\nd2={d2}\nd4={d5}\nd6={d6}\n{d7}")