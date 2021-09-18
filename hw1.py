

# raw_input() from python2 got renamed and inherited as input() function in python3.
# input() from python2 is deprecated and it can be simulated as eval(input()) in python3
#
# PEP 3105 -- Make print a function https://www.python.org/dev/peps/pep-3105/
# print statement in python2 was replaced by print() function in python3

a = 0
b = 1
c = 2
d = True
e = None
f = False
g = "some text"
h = ""

print(f"We have multiple defined variables: a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h=\"\" ")

print("let`s check all of them with bool! \n ")
print(f"bool(a)={bool(a)}, bool(b)={bool(b)}, bool(c)={bool(c)}, bool(d)={bool(d)}, bool(e)={bool(e)}, \
bool(f)={bool(f)}, bool(g)={bool(g)}, bool(h)={bool(h)} ")
print("\nSo we see that variable a = 0, variable e = None, variable f = False and empty variable h are False in bool\n\
while other variable are True")