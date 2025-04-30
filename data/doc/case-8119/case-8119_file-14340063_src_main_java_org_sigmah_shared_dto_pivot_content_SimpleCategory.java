package org.sigmah.shared.dto.pivot.content;

/*
 * #%L
 * Sigmah
 * %%
 * Copyright (C) 2010 - 2016 URD
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

/**
 * @author Alex Bertram (akbertram@gmail.com)
 */
public class SimpleCategory implements LabeledDimensionCategory {

    private String label;

    private SimpleCategory() {

    }

    public SimpleCategory(String label) {
        this.label = label;
    }

    @Override
    public Comparable getSortKey() {
        return label;
    }

	@Override
    public String getLabel() {
        return label;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        SimpleCategory that = (SimpleCategory) o;

        if (label != null ? !label.equals(that.label) : that.label != null) {
            return false;
        }

        return true;
    }

    @Override
    public int hashCode() {
        return label != null ? label.hashCode() : 0;
    }

    @Override
    public String toString() {
        return "SimpleCategory{" +
                "label='" + label + '\'' +
                '}';
    }

	@Override
	public DimensionCategory getParent() {
		return null;
	}

	@Override
	public boolean hasParent() {
		return false;
	}
}
