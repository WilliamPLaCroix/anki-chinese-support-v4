# Copyright (C) Shigeyuki <http://patreon.com/Shigeyuki>
# License: GNU AGPL version 3 or later <http://www.gnu.org/licenses/agpl.html>

# Chinese Support 3
# origin addon page: https://ankiweb.net/shared/info/1128979221
# origin github: https://github.com/Gustaf-C/anki-chinese-support-3

# 1. the six in the lib folder is outdated, please update with pip (or uv).

# 2. I get a database error when add-on updating.
    # (this error is strange, how did updates work before?)
    # anyway, the database is closed when updating the add-on.
from aqt import mw, gui_hooks
from aqt.addons import AddonManager

def update_shige_patch(addon_manager: AddonManager, module, *args, **kwargs):
    if module == addon_manager.addonFromModule(__name__):
        from .main import dictionary
        dictionary.close()

def set_shige_patch():
    gui_hooks.addon_manager_will_install_addon.append(update_shige_patch)


# 🐼Chinese Support V4 (Fixed by Shigeඞ)

# 3. Change the menu because the contact info is different.
# gui.py
SHIGE_PATCH_MENU = True
def get_rate_this_url():
    rate_this_url = None
    addon_package = mw.addonManager.addonFromModule(__name__)
    if (isinstance(addon_package, (int, float))
        or (isinstance(addon_package, str)
        and addon_package.isdigit())):
        rate_this_url = f"https://ankiweb.net/shared/review/{addon_package}"
    return rate_this_url


# Pull: Update MDBG links
# fetsorn commented on Feb 22 • <https://github.com/fetsorn>
# https://github.com/Gustaf-C/anki-chinese-support-3/pull/104
# https://github.com/Gustaf-C/anki-chinese-support-3/pull/104/commits/f720766e824872aa3453a19ff0fcf1ef599ccd0d


# 5. other pull requests (not yet)
# https://github.com/Gustaf-C/anki-chinese-support-3/pulls


# kieranlblack commented on Feb 18
# https://github.com/Gustaf-C/anki-chinese-support-3/pull/102
# よくわかりません. ｽｷｯﾌﾟします.

# https://github.com/Gustaf-C/anki-chinese-support-3/pull/95
# よくわかりません. ｽｷｯﾌﾟ.

# 6. fill.py
# fill.py", line 242, in bulk_fill_transcript
#     'hanzi': get_hanzi(copy),
#                        ^^^^
# UnboundLocalError:
# ｶｰﾄﾞがないときにcopyがｴﾗｰになるﾊﾞｸﾞを修正
#     if not copy:
#         showInfo("not found")

# 7. gui.py
# add-onsの競合を避けるためにmw.custom_menusをmw.shige_patch_chinese_v4_menuへ変更します.

# Configは特殊な仕組みで働いているように見えるのでuser_filseに保存した方がいいかも?

# 