# -*- coding: UTF-8 -*-
# ======================================================================
# @Author   : SyncSketch LLC
# @Email    : dev@syncsketch.com
# @Version  : 1.0.0
# ======================================================================
import sys
import os

main_folder = os.path.dirname(__file__)
parent_folder = os.path.dirname(main_folder)
sys.path.append(parent_folder)

import syncsketchGUI
reload(syncsketchGUI)
syncsketchGUI.reload_toolkit()
syncsketchGUI.show_menu_window()