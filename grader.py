#! /usr/bin/python3

import argparse
import sqlite3

# Create the overall parser
parser = argparse.ArgumentParser(description="A simple commandline gradebook utility that stays out of your way.")

# Attach an option for specifying a non-standard filename
parser.add_argument('-f', '--filename', default='dbgrades.db', help="The name of the grades database file to use.")

# Add the subcommand parsers here

# Parse the other args

# Make the cursor

# Dispatch to the appropriate utility
