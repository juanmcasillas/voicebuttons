#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# ############################################################################
#
# voicebuttons.py
# 11/01/2023 (c) Juan M. Casillas <juanm.casillas@gmail.com>
#
# read a config file, talk when a button is pressed, or released.
#
# ############################################################################


from voicebuttons import *
import argparse
import sys
import platform

import warnings
warnings.filterwarnings("ignore")
# ignore pyglet win32 warning
# python39\lib\site-packages\pyglet\libs\win32\__init__.py:326: UserWarning: Could not set COM MTA mode. Unexpected behavior may occur.

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Show data about file and processing (Debug)", action="count", default=0)
    parser.add_argument("-c", "--config", help="reads the configuration from <config>", default="config/config.json")
    parser.add_argument("-l", "--list", help="show available USB devices", action="store_true")
    parser.add_argument("-d", "--dcs", help="start reading form DCS (set default config to config/config_dcs.json)", action="store_true")
    parser.add_argument("-o", "--logfile", help="Outputs to the defined file. Default = 'stdout'", default=sys.stdout)
    parser.add_argument("-g", "--gui", help="Start minimized as traybar", action="store_true")
    parser.add_argument("-t", "--test", help="Talk a sample test")
    args = parser.parse_args()

    mode = "default"
    if args.dcs:
        mode = "DCS"
        args.config = args.config if args.config != "config/config.json" else "config/config_dcs.json"
    
    App.config(args.config,mode)
    App.config_set('platform',platform.system()) 
    App.config_set('verbose',args.verbose)
    App.config_set('gui',args.gui)

    if args.logfile != sys.stdout:
        output_fd = open(args.logfile,"w+")
        OutputManager.config(output_fd) 


    manager = VoiceButtonsClass(CONFIG().voice,mode)

    if args.test:
        manager.say_text(args.test)
        sys.exit(0)

    if args.list:
        manager.list_devices()
        sys.exit(0)

    manager.start()