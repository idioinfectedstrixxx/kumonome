import argparse
import colorama
from colorama import Fore, Back, Style
import cutie
import time
from datetime import datetime
from time import sleep
import keyboard
import logwriting
import os
import parsers
from platform import platform
import querygen
import sys
from threading import Thread



parser = argparse.ArgumentParser(description='Kumonome: simple random youtube parser')
parser.add_argument('--maxviews', type=int, default=2000, help='max views count for videos (default: 2000)')
parser.add_argument('--ql', type=int, default=5, help='number of random-generated symbols (default: 5)')
argsl = parser.parse_args()

colorama.init(autoreset=True)
puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
else:
    delet = 'clear'
os.system(delet)

print(Fore.RED + ('\n'
                  '              #    # #     # #     # ####### #     # ####### #     # #######\n'
                  '  / _ \       #   #  #     # ##   ## #     # ##    # #     # ##   ## #      \n'
                  '\_\(0)/_/     #  #   #     # # # # # #     # # #   # #     # # # # # #      \n'
                  ' _//"\\\_      ###    #     # #  #  # #     # #  #  # #     # #  #  # #####  \n'
                  '  /   \       #  #   #     # #     # #     # #   # # #     # #     # #      \n'
                  '              #   #  #     # #     # #     # #    ## #     # #     # #      \n'
                  '              #    #  #####  #     # ####### #     # ####### #     # #######'))
modes = ['Random video search', 'Random video search with date filter', 'Random channel search', 'Random playlist search',
         'Random playlist search with date filter', 'Exit']
print('Select a mode:')
mode = cutie.select(modes)
direct = logwriting.make_logs_dir()
os.chdir(direct)
dt = str(datetime.now())
with open('logs.txt', 'a+', encoding='utf-8') as l:
    l.write(f'<{dt}>')
os.chdir('../')
smodes = ['Normal mode', 'Endless scan mode']
if mode == 0:
    os.chdir(direct)
    parser = parsers.Yt_Parser("vid", argsl.maxviews)
    os.system(delet)
    smode = cutie.select(smodes)
    if smode == 0:
        while True:
            q = querygen.rand_qgen(argsl.ql, False, None)
            parser.search(q)
            c = ['Continue','Quit the program']
            choice = cutie.select(c)
            if choice == 0:
                q = querygen.rand_qgen(argsl.ql, False, None)
                parser.search(q)
            elif choice == 1:
                break
        exit(0)
    elif smode == 1:
        while True:
            q = querygen.rand_qgen(argsl.ql, False, None)
            parser.search(q)
elif mode == 1:
    os.chdir(direct)
    date = input("Please select a date for filter(will show videos which were uploaded earlier; year or yy-mm-dd format)\n")
    parser = parsers.Yt_Parser("vid", argsl.maxviews)
    smode = cutie.select(smodes)
    os.system(delet)
    if smode == 0:
        while True:
            q = querygen.rand_qgen(argsl.ql, True, date)
            parser.search(q)
            c = ['Continue', 'Quit the program']
            choice = cutie.select(c)
            if choice == 0:
                q = querygen.rand_qgen(argsl.ql, True, date)
                parser.search(q)
            elif choice == 1:
                exit(0)
    elif smode == 1:
        while True:
            q = querygen.rand_qgen(argsl.ql, True, date)
            parser.search(q)
elif mode == 2:
    os.chdir(direct)
    parser = parsers.Yt_Parser("chan", argsl.maxviews)
    smode = cutie.select(smodes)
    os.system(delet)
    if smode == 0:
        while True:
            q = querygen.rand_qgen(argsl.ql, False, None)
            parser.search(q)
            c = ['Continue', 'Quit the program']
            choice = cutie.select(c)
            if choice == 0:
                q = querygen.rand_qgen(argsl.ql, False, None)
                parser.search(q)
            elif choice == 1:
                exit(0)
    elif smode == 1:
        while True:
            q = querygen.rand_qgen(argsl.ql, False, None)
            parser.search(q)
elif mode == 3:
    os.chdir(direct)
    parser = parsers.Yt_Parser("plists", argsl.maxviews)
    smode = cutie.select(smodes)
    os.system(delet)
    if smode == 0:
        q = querygen.rand_qgen(argsl.ql, False, None)
        parser.search(q)
        c = ['Continue', 'Quit the program']
        choice = cutie.select(c)
        if choice == 0:
            q = querygen.rand_qgen(argsl.ql, False, None)
            parser.search(q)
        elif choice == 1:
            exit(0)
    elif smode == 1:
        while True:
            q = querygen.rand_qgen(argsl.ql, False, None)
            parser.search(q)
elif mode == 4:
    os.chdir(direct)
    date = input(
        "Please select a date for filter(will show playlists which were uploaded earlier; year or yy-mm-dd format)")
    parser = parsers.Yt_Parser("plists", argsl.maxviews)
    smode = cutie.select(smodes)
    os.system(delet)
    if smode == 0:
        while True:
            q = querygen.rand_qgen(argsl.ql, True, date)
            parser.search(q)
            c = ['Continue', 'Quit the program']
            choice = cutie.select(c)
            if choice == 0:
                q = querygen.rand_qgen(argsl.ql, True, date)
                parser.search(q)
            elif choice == 1:
                exit(0)
    elif smode == 1:
        while True:
            q = querygen.rand_qgen(argsl.ql, True, date)
            parser.search(q)
elif mode == 5:
    exit(0)