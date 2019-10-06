

import pdb

def working_func(test, job, build):
    print("Works good")
    print("Works good...")
    print("Works good.....")
    pdb.set_trace()
    print("Works good.......")
    print("Works good.........")
    print("Works good...........")
    print("I guess something is wrong")
    print("Yeah it is wrong, What's the wrong")
    print("Yesss, I find the bug..")
    print("Fixed ASAP")


if __name__ == '__main__':
    print('''
c: continue execution
w: shows the context of the current line it is executing.
a: print the argument list of the current function
s: Execute the current line and stop at the first possible occasion.
n: Continue execution until the next line in the current function is reached or it returns.
''')
    working_func("main_test", "job_build_packge", "build2233")
