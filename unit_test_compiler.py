"""
compiler unit test
"""

import compiler
import filecmp


def main():
    """
    main function
    """
    print('Start UT')
    ut = UnitTestCompiler()
    print('Done UT')


class UnitTestCompiler:
    """
    Class for unit test UnitTestCompiler
    """

    def __init__(self):
        self.error = 0
        self.expectedFile = 'unit_test_expected_hex.txt'
        self.outputFile = 'hexcode_16_bit.txt'
        self.run_test()

    def run_test(self):
        """
        test compiler
        """
        compiler.compileGG()
        self.check_output()

    def check_output(self):
        """
        check output file
        """
        if filecmp.cmp(self.expectedFile, self.outputFile):
            print('Passed!')
            return 0
        else:
            print('Failed!')
            return -1


if __name__ == "__main__":
    main()
