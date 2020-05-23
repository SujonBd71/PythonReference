

def TestSplit():
    def split(s : str):
        print(s)
        splits = s.split(' |\+|\-|\*|\/|\n')
        print(splits)
        import re
        tokens = re.split(' |\+|\-|\*|\/|\n', s)
        print(tokens)



    split(" 3+5 / 2 +    3 /2  -9")


def TestReplace():
    s = " 3+5 / 2 +    3 *2  -9"

    print(s)
    t = s.replace(" ", "")
    print(t)

def RunTest():
    TestSplit()
    # TestReplace()

RunTest()
