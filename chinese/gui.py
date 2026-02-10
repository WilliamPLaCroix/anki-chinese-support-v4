# Copyright © 2012 Thomas TEMPÉ <thomas.tempe@alysse.org>
# Copyright © 2017-2020 Joseph Lorimer <joseph@lorimer.me>
# Copyright © 2020 Joe Minicucci <https://joeminicucci.com>
# Copyright © 2023-2024 Gustaf Carefall <https://github.com/Gustaf-C>
# Copyright © 2025 Shigeyuki <http://patreon.com/Shigeyuki>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from functools import partial

from aqt import mw
from aqt.utils import openLink
from aqt.qt import QAction, QActionGroup, QMenu, QKeySequence

from .about import CSR_GITHUB_URL, showAbout
from .fill import (
    bulk_fill_all,
    bulk_fill_classifiers,
    bulk_fill_defs,
    bulk_fill_frequency,
    bulk_fill_hanzi,
    bulk_fill_silhouette,
    bulk_fill_sound,
    bulk_fill_transcript,
    bulk_fill_usage,
)
from .main import config


SPEECH_ENGINES = {
    'Baidu Translate': 'baidu|zh',
    'Google Mandarin (PRC)': 'google|zh-CN',
    'Google Mandarin (Taiwan)': 'google|zh-TW',
    'Amazon Polly': 'aws|Zhiyu',
    'Disabled': None,
}

PHONETIC_TARGETS = {
    'Pinyin': 'pinyin',
    'Pinyin (Taiwan)': 'pinyin_tw',
    'Bopomofo': 'bopomofo',
    'Jyutping': 'jyutping',
}


def load_menu():
    for k, v in PHONETIC_TARGETS.items():
        add_menu_item(
            'Chinese::Phonetics',
            k,
            partial(config.update, {'target': v}),
            checkable=True,
            checked=bool(config['target'] == v),
        )

    for k, v in SPEECH_ENGINES.items():
        add_menu_item(
            'Chinese::Speech Engine',
            k,
            partial(config.update, {'speech': v}),
            checkable=True,
            checked=bool(config['speech'] == v),
        )

    add_menu('Chinese::Bulk Fill')
    add_menu_item('Chinese::Bulk Fill', ('Hanzi'), bulk_fill_hanzi)
    add_menu_item('Chinese::Bulk Fill', ('Definitions'), bulk_fill_defs)
    add_menu_item('Chinese::Bulk Fill', ('Transcripts'), bulk_fill_transcript)
    add_menu_item('Chinese::Bulk Fill', ('Classifiers'), bulk_fill_classifiers)
    add_menu_item('Chinese::Bulk Fill', ('Sound'), bulk_fill_sound)
    add_menu_item('Chinese::Bulk Fill', ('Silhouette'), bulk_fill_silhouette)
    add_menu_item('Chinese::Bulk Fill', ('Frequency'), bulk_fill_frequency)
    add_menu_item('Chinese::Bulk Fill', ('Usage'), bulk_fill_usage)
    add_menu_item('Chinese::Bulk Fill', ('All'), bulk_fill_all)

    from ._shige_patch import SHIGE_PATCH_MENU, get_rate_this_url
    if SHIGE_PATCH_MENU:

        SHIGE_PATCH_MENU_NAME = f'Chinese::Fixed by Shigeඞ'
        add_menu(SHIGE_PATCH_MENU_NAME)
        add_menu_item(
            SHIGE_PATCH_MENU_NAME,
            ('🚨Report'),
            lambda: openLink('https://shigeyukey.github.io/shige-addons-wiki/contact.html'),
        )
        add_menu_item(
            SHIGE_PATCH_MENU_NAME,
            ('📖Wiki'),
            lambda: openLink('https://shigeyukey.github.io/shige-addons-wiki/chinese-support-v4.html'),
        )
        rate_this_url = get_rate_this_url()
        if rate_this_url:
            add_menu_item(
                SHIGE_PATCH_MENU_NAME,
                ('👍️Rate This'),
                lambda: openLink(rate_this_url),
            )
        add_menu_item(
            SHIGE_PATCH_MENU_NAME,
            ('💖Become a Patron'),
            lambda: openLink('https://www.patreon.com/Shigeyuki'),
        )

    else: # original
        add_menu('Chinese::Help')
        add_menu_item(
            'Chinese::Help',
            ('Report a bug or make a feature request'),
            lambda: openLink(CSR_GITHUB_URL + '/issues'),
        )
        add_menu_item('Chinese::Help', ('About...'), showAbout)


def unload_menu():
    for menu in mw.shige_patch_chinese_v4_menu.values():
        mw.form.menubar.removeAction(menu.menuAction())

    mw.shige_patch_chinese_v4_menu.clear()


def add_menu(path):
    if not hasattr(mw, 'shige_patch_chinese_v4_menu'):
        mw.shige_patch_chinese_v4_menu = {}

    if len(path.split('::')) == 2:
        parent_path, child_path = path.split('::')
        has_child = True
    else:
        parent_path = path
        has_child = False

    if parent_path not in mw.shige_patch_chinese_v4_menu:
        parent = QMenu('&' + parent_path, mw)
        mw.shige_patch_chinese_v4_menu[parent_path] = parent
        mw.form.menubar.insertMenu(mw.form.menuTools.menuAction(), parent)

    if has_child and (path not in mw.shige_patch_chinese_v4_menu):
        child = QMenu('&' + child_path, mw)
        mw.shige_patch_chinese_v4_menu[path] = child
        mw.shige_patch_chinese_v4_menu[parent_path].addMenu(child)


def add_menu_item(path, text, func, keys=None, checkable=False, checked=False):
    action = QAction(text, mw)

    if keys:
        action.setShortcut(QKeySequence(keys))

    if checkable:
        action.setCheckable(checkable)
        action.toggled.connect(func)
        if not hasattr(mw, 'action_groups'):
            mw.action_groups = {}
        if path not in mw.action_groups:
            mw.action_groups[path] = QActionGroup(None)
        mw.action_groups[path].addAction(action)
        action.setChecked(checked)
    else:
        action.triggered.connect(func)

    if path == 'File':
        mw.form.menuCol.addAction(action)
    elif path == 'Edit':
        mw.form.menuEdit.addAction(action)
    elif path == 'Tools':
        mw.form.menuTools.addAction(action)
    elif path == 'Help':
        mw.form.menuHelp.addAction(action)
    else:
        add_menu(path)
        mw.shige_patch_chinese_v4_menu[path].addAction(action)
