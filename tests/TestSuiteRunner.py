#!/usr/bin/env python 
import argparse
import os
import sys


def main(argv):
    """
    main function
    @param argv: running arguments
    @return: none
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--test_list",
                        help="specify tests list file OR group test list file "
                             "default is run all tests from dir \"tests\"")
    parser.add_argument("-browser", "--browser", default="",
                        help="specify browser type: Chrome = 'ch', Firefox = 'ff', "
                             "browserstack = 'browserstack'")

    args = parser.parse_args()
    browser = args.browser
    if browser:
        browser = "--browser=" + args.browser
    if args.test_list:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "") + args.test_list
        for directories, sub_dirs, files in os.walk(path):
                for file in files:
                    if file.startswith("test") and not file.endswith(".pyc"):
                        os.system("py.test {} {}".format(
                            browser, os.path.join(path, "") + file))

if __name__ == "__main__":
    main(sys.argv)
