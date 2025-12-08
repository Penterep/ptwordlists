#!/usr/bin/python3
"""
Copyright (c) 2025 Penterep Security s.r.o.

ptwordlists is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ptwordlists is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ptwordlists.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import os
import sys; sys.path.append(__file__.rsplit("/", 1)[0])

from ptlibs import ptjsonlib, ptmisclib, ptnethelper
from ptlibs.ptprinthelper import ptprint, print_banner, help_print, get_colored_text
from _version import __version__


class PtWordlists:
    def __init__(self, args):
        self.args        = args

    def run(self) -> None:
        """Main method"""

        if self.args.show_wordlists:
            self.show_wordlists()

    def show_wordlists(self):
        # get the directory of the current file
        current_dir = os.path.dirname(__file__)
        # wordlists folder relative to this file
        wordlists_dir = os.path.join(current_dir, "wordlists")

        # make sure the folder exists
        if not os.path.isdir(wordlists_dir):
            print(f"Wordlists folder not found: {wordlists_dir}")
            return

        # list all files in the wordlists folder
        for filename in sorted(os.listdir(wordlists_dir)):
            filepath = os.path.join(wordlists_dir, filename)
            if os.path.isfile(filepath):
                print(filename)

def get_help():
    return [
        {"description": ["ptwordlists"]},
        {"usage": ["ptwordlists <options>"]},
        {"usage_example": [
            "ptwordlists --show-wordlists",
            "ptwordlists --install-wordlists",
        ]},
        {"options": [
            ["-s",  "--show-wordlists",         "",                 "Show wordlists"],
            ["-v",  "--version",                "",                 "Show script version and exit"],
            ["-h",  "--help",                   "",                 "Show this help message and exit"],
        ]
        }]

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(add_help="False", description=f"{SCRIPTNAME} <options>")
    parser.add_argument("-s", "--show-wordlists",  action="store_true")
    parser.add_argument("-v",  "--version",        action='version', version=f'{SCRIPTNAME} {__version__}')

    if len(sys.argv) == 1 or "-h" in sys.argv or "--help" in sys.argv:
        ptprint(help_print(get_help(), SCRIPTNAME, __version__))
        sys.exit(0)

    args = parser.parse_args()
    print_banner(SCRIPTNAME, __version__, False, 0)
    return args

def main():
    global SCRIPTNAME
    SCRIPTNAME = "ptwordlists"
    args = parse_args()
    script = PtWordlists(args)
    script.run()

if __name__ == "__main__":
    main()
