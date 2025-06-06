/* xoreos - A reimplementation of BioWare's Aurora engine
 *
 * xoreos is the legal property of its developers, whose names
 * can be found in the AUTHORS file distributed with this source
 * distribution.
 *
 * xoreos is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 3
 * of the License, or (at your option) any later version.
 *
 * xoreos is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with xoreos. If not, see <http://www.gnu.org/licenses/>.
 */

/** @file
 *  The keyboard mapping menu.
 */

#include "src/engines/aurora/widget.h"

#include "src/engines/kotor/gui/options/keyboardconfig.h"

namespace Engines {

namespace KotOR {

OptionsKeyboardConfigurationMenu::OptionsKeyboardConfigurationMenu(::Engines::Console *console) :
		KotORBase::GUI(console) {

	load("optkeymapping");

	addBackground(KotORBase::kBackgroundTypeMenu);
}

OptionsKeyboardConfigurationMenu::~OptionsKeyboardConfigurationMenu() {
}

void OptionsKeyboardConfigurationMenu::callbackActive(Widget &widget) {
	if (widget.getTag() == "BTN_Default") {
	}

	if (widget.getTag() == "BTN_Cancel") {
		_returnCode = 1;
		return;
	}

	if (widget.getTag() == "BTN_Accept") {
		_returnCode = 1;
		return;
	}
}

} // End of namespace KotOR

} // End of namespace Engines