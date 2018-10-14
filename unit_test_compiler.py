"""
compiler unit test
"""

import compiler


def main():
    """
    main function
    """
    print('Start UT')
    ut = UnitTestCompiler()
    ut.unit_test()
    print('Done UT')


class UnitTestCompiler:
    """
    Class for unit test UnitTestCompiler
    """

    def __init__(self):
        self.error = 0

    def unit_test(self):
        """
        test compiler
        """
        compiler.compile()


if __name__ == "__main__":
    main()
