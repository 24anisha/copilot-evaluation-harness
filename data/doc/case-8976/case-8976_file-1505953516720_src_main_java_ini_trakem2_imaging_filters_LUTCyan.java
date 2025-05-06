/*-
 * #%L
 * TrakEM2 plugin for ImageJ.
 * %%
 * Copyright (C) 2005 - 2021 Albert Cardona, Stephan Saalfeld and others.
 * %%
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public
 * License along with this program.  If not, see
 * <http://www.gnu.org/licenses/gpl-3.0.html>.
 * #L%
 */
package ini.trakem2.imaging.filters;

import ij.process.ColorProcessor;
import ij.process.ImageProcessor;
import ini.trakem2.utils.Utils;

import java.awt.image.IndexColorModel;
import java.util.Map;

public class LUTCyan implements IFilter
{
	public LUTCyan() {}
	
	public LUTCyan(Map<String,String> params) {}

	@Override
	public ImageProcessor process(ImageProcessor ip) {
		if (ip instanceof ColorProcessor) {
			Utils.log("Ignoring " + getClass().getSimpleName() + " filter for RGB image");
			return ip;
		}
		byte[] s = new byte[256];
		for (int i=0; i<256; ++i) s[i] = (byte)i;
		ip.setColorModel(new IndexColorModel(8, 256, new byte[256], s, s));
		return ip;
	}

	@Override
	public String toXML(String indent) {
		return new StringBuilder(indent)
			.append("<t2_filter class=\"").append(getClass().getName())
			.append("\" />\n").toString();
	}

	@Override
	public boolean equals(final Object o) {
		return null != o && o.getClass() == getClass();
	}
}
