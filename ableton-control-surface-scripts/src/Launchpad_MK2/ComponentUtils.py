# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_MK2/ComponentUtils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 399 bytes


def skin_scroll_component(component):
    for button in (component.scroll_up_button, component.scroll_down_button):
        button.color = "Scrolling.Enabled"
        button.pressed_color = "Scrolling.Pressed"
        button.disabled_color = "Scrolling.Disabled"
