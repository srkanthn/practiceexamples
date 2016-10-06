# def fib(n):    # write Fibonacci series up to n
#      """Print a Fibonacci series up to n."""
#      a, b = 0, 1
#      l=[]
#      while a < n:
#          # print(a, end=' ')
#          l.append(a)
#          a, b = b, a+b
#      print(l)
#
# fib(200)


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
# ask_ok('Do you really want to quit?',0)


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
# parrot('a thousand', state='pushing up the daisies')
#
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
#
# # fun([1,2,3,4,5],a=1,b=2)

# def parrot(voltage, state='a stiff', action='voom'):
#      print("-- This parrot wouldn't", action, end=' ')
#      print("if you put", voltage, "volts through it.", end=' ')
#      print("E's", state, "!")
#
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

def make_incrementor(n):
     return lambda x: x + 2*n

f = make_incrementor(76)
print(f)
print(f(1))
print('hello')