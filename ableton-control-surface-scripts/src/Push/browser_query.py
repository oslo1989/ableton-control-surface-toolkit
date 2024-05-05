# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/browser_query.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4540 bytes
from functools import partial

from ableton.v2.base import const, find_if, first
from future.utils import string_types

from .browser_model import VirtualBrowserItem


class BrowserQuery:
    def __init__(self, subfolder=None, *a, **k):
        self.subfolder = subfolder

    def __call__(self, browser):
        if self.subfolder:
            return [
                VirtualBrowserItem(
                    name=(self.subfolder),
                    children_query=(partial(self.query, browser)),
                    is_folder=True,
                ),
            ]
        return self.query(browser)

    def query(self, browser):
        raise NotImplementedError


class PathBrowserQuery(BrowserQuery):
    def __init__(self, path=(), root_name=None, *a, **k):
        (super().__init__)(*a, **k)
        self.path = path
        self.root_name = root_name

    def query(self, browser):
        return self._find_item(self.path, [getattr(browser, self.root_name)], browser) or []

    def _find_item(self, path, items=None, browser=None):
        name = path[0]
        elem = find_if(lambda x: x.name == name, items)
        if elem:
            if len(path) == 1:
                return [elem]
            return self._find_item(path[1:], elem.children)
        return None


class TagBrowserQuery(BrowserQuery):
    def __init__(self, include=(), exclude=(), root_name=None, *a, **k):
        (super().__init__)(*a, **k)
        self.include = include
        self.exclude = exclude
        self.root_name = root_name

    def query(self, browser):
        return list(
            filter(
                lambda item: item.name not in self.exclude,
                sum(list(map(partial((self._extract_path), browser=browser), self.include)), ()),
            ),
        )

    def _extract_path(self, path, items=None, browser=None):
        if isinstance(path, string_types):
            path = [path]
        if items is None:
            items = [getattr(browser, self.root_name)]
        if path:
            name = path[0]
            elem = find_if(lambda x: x.name == name, items)
            if elem:
                items = self._extract_path(path[1:], elem.children)
        return tuple(items)


class SourceBrowserQuery(TagBrowserQuery):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)

    def query(self, browser):
        root = super().query(browser)
        groups = {}
        for item in root:
            groups.setdefault(item.source, []).append(item)

        return [
            VirtualBrowserItem(name=(k_g[0] if k_g[0] is not None else ""), children_query=(const(k_g[1])))
            for k_g in sorted(groups.items(), key=first)
        ]


class PlacesBrowserQuery(BrowserQuery):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)

    def query(self, browser):
        return [browser.packs, browser.user_library, browser.current_project, *list(browser.user_folders)]


class ColorTagsBrowserQuery(BrowserQuery):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)

    def query(self, browser):
        return list(browser.colors)
