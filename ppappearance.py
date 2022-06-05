#!/usr/bin/env python3

import os
from colorama import Back, Fore, Style
import getch

user = os.getlogin()

user_themes = os.listdir('/home/' + user + '/.themes/')
user_icons = os.listdir('/home/' + user + '/.icons/')
global_themes =  os.listdir('/usr/share/themes/')
global_icons = os.listdir('/usr/share/icons/')

themes = []
icons = []
cursors = []

for ob_theme in user_themes:
    folder = os.listdir('/home/' + user + '/.themes/' + ob_theme)

    if 'openbox-3' in folder:
        continue
    else:
        themes.append(ob_theme)

for ob_theme in global_themes:
    folder = os.listdir('/usr/share/themes/' + ob_theme)

    if 'openbox-3' in folder:
        continue
    else:
        themes.append(ob_theme)

for cursor in user_icons:
    folder = os.listdir('/home/' + user + '/.icons/' + cursor)

    if 'cursors' in folder and '8x8' in folder:
        icons.append(cursor)
        cursors.append(cursor)
    elif 'cursors' in folder:
        cursors.append(cursor)
    else:
        icons.append(cursor)


for cursor in global_icons:
    folder = os.listdir('/usr/share/icons/' + cursor)

    if 'cursors' in folder and '8x8' in folder:
        icons.append(cursor)
        cursors.append(cursor)
    elif 'cursors' in folder:
        cursors.append(cursor)
    else:
        icons.append(cursor)

f = '/home/' + user + '/.gtkrc-2.0'

pointer = 1

def get_key():
    first_char = getch.getch()
    if first_char == '\x1b':
        return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch.getch() + getch.getch()]
    else:
        return first_char

num = 0 

while True:
    os.system('clear')

    if pointer == 1:
        print(Back.BLUE + 'themes' + Style.RESET_ALL + ' icons cursors')

        for theme in themes:
            if themes[num] in theme:
                print(Fore.YELLOW + theme + Style.RESET_ALL)
            else:
                print(theme)
            
    elif pointer == 2:
        print('themes ' + Back.BLUE + 'icons' + Style.RESET_ALL + ' cursors')

        for icon in icons:
            if icons[num] in icon:
                print(Fore.YELLOW + icon + Style.RESET_ALL)
            else:
                print(icon)

    elif pointer == 3:
        print('themes icons ' + Back.BLUE + 'cursor' + Style.RESET_ALL)

        for cursor in cursors:
            if cursors[num] in cursor:
                print(Fore.YELLOW + cursor + Style.RESET_ALL)
            else:
                print(cursor)

    char = get_key()

    if char == 'q':
        os.system('clear')
        quit()
    elif char == 'h':
        while True:
            os.system('clear')

            print('to quit press q')
            print('to get help press h')
            print('to switch to themes icons or cursor press 1 2 or 3')
            print('use the up arrow and down arrow to hightlight a theme icon or cursor')
            print('press enter to select a hightlighted theme icon or cursor\n')
            print('WARNING if you have themes icons and cursor that are duplicates or start with the same few letters the program will break\n')
            print('ex: Adwaita Adwaita, Tela Tela-dark\n')

            prompt = input('press q to exit: ')

            if prompt == 'q':
                break
    elif char == '1':
        pointer = 1
        num = 0
    elif char == '2':
        pointer = 2
        num = 0
    elif char == '3':
        pointer = 3
        num = 0
    elif char == 'up':
        num = num - 1

        if num < 0:
            num = 0
    elif char == 'down':
        num = num + 1
        
        if pointer == 1:
            if num > len(themes) - 1:
                num = len(themes) - 1
        elif pointer == 2:
            if num > len(icons) - 1:
                num = len(icons) - 1
        elif pointer == 3:
            if num > len(cursors) - 1:
                num = len(cursors) - 1
    elif char == '\n':
        with open (f, 'r') as file:
            data = file.readlines()

            line_num = 0

            for line in data:
                if pointer == 1:
                    for theme in themes:
                        if 'gtk-theme-name="' + theme + '"' in line:
                            data[line_num] = 'gtk-theme-name="' + themes[num] + '"\n'

                    line_num = line_num + 1

                elif pointer == 2:
                    for icon in icons:
                        if 'gtk-icon-theme-name="' + icon + '"' in line:
                            data[line_num] = 'gtk-icon-theme-name="' + icons[num] + '"\n'

                    line_num = line_num + 1

                elif pointer == 3:
                    for cursor in cursors:
                        if 'gtk-cursor-theme-name="' + cursor + '"\n' in line:
                            data[line_num] = 'gtk-cursor-theme-name="' + cursors[num] + '"\n'

                    line_num = line_num + 1

        with open (f, 'w') as file:
            file.writelines(data)
