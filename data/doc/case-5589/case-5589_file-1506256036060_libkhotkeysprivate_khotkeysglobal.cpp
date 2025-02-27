/*
    SPDX-License-Identifier: GPL-2.0-only
    SPDX-FileCopyrightText: 1999-2001 Lubos Lunak <l.lunak@kde.org>
 */

#define _KHOTKEYSGLOBAL_CPP_

#include "khotkeysglobal.h"

#include <KGlobal>
#include <QDebug>
#include <kstandarddirs.h>

#include "input.h"
#include "shortcuts_handler.h"
#include "triggers/gestures.h"
#include "triggers/triggers.h"
#include "windows_handler.h"

namespace KHotKeys
{
QPointer<ShortcutsHandler> keyboard_handler = nullptr;
QPointer<WindowsHandler> windows_handler = nullptr;

static bool _khotkeys_active = false;

void init_global_data(bool active_P, QObject *owner_P)
{
    // Make these singletons.
    if (!keyboard_handler) {
        keyboard_handler = new ShortcutsHandler(active_P ? ShortcutsHandler::Active : ShortcutsHandler::Configuration, owner_P);
    }
    if (!windows_handler) {
        windows_handler = new WindowsHandler(active_P, owner_P);
    }
    if (!gesture_handler) {
        gesture_handler = new Gesture(active_P, owner_P);
    }
    khotkeys_set_active(false);
}

void khotkeys_set_active(bool active_P)
{
    _khotkeys_active = active_P;
}

bool khotkeys_active()
{
    return _khotkeys_active;
}

// does the opposite of KStandardDirs::findResource() i.e. e.g.
// "/opt/kde2/share/applnk/System/konsole.desktop" -> "System/konsole.desktop"
QString get_menu_entry_from_path(const QString &path_P)
{
    const QStringList dirs = KGlobal::dirs()->resourceDirs("apps");
    for (QStringList::ConstIterator it = dirs.constBegin(); it != dirs.constEnd(); ++it)
        if (path_P.indexOf(*it) == 0) {
            QString ret = path_P;
            ret.remove(0, (*it).length());
            if (ret[0] == '/')
                ret.remove(0, 1);
            return ret;
        }
    return path_P;
}

} // namespace KHotKeys