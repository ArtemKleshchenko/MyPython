def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
assert say_hi("Oliver", 18) == "Hi. My name is Oliver and I'm 18 years old", 'Test3'
assert say_hi("Jack", 27) == "Hi. My name is Jack and I'm 27 years old", 'Test4'
assert say_hi("Henry", 54) == "Hi. My name is Henry and I'm 54 years old", 'Test5'
print('ОК')