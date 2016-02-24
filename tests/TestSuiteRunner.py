#!/usr/bin/env python 
import argparse
import os
import sys
import webbrowser


def get_directory_files(path):
    for _, _, files in os.walk(path):
        return [file for file in files]

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
                             "browserstack = 'bs'")
    parser.add_argument("-html", "--html", default="",
                        help="specify html report must be with expansion .html"
                             "(e.g -html=report.html)")

    args = parser.parse_args()
    browser = args.browser
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")
    if browser:
        browser = "--browser=" + args.browser
    if args.html:
        html = "--html=" + args.html
    if args.test_list:
        test_path = path + args.test_list
        test_list = get_directory_files(test_path)
        for i in test_list:
            if i.startswith("test") and not i.endswith(".pyc"):
                        os.system("py.test {} {} {}".format(
                            browser, html, os.path.join(test_path, "") + i))

    if args.html:
        html_path = get_directory_files(path)
        for i in html_path:
            if i.endswith(".html"):
                webbrowser.open_new_tab(i)


if __name__ == "__main__":
    main(sys.argv)
