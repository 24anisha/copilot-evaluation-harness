/**
 * The MIT License (MIT)
 * Copyright (c) 2016 FI MUNI
 */
package main.java.framework.api;

/**
 * Enum of visitor scopes
 * @author Tomas Lestyan
 */
public enum Scope {

	METHOD(2), CLASS(1), ALL(0);

	private final int value;

	/**
	 * Constructor
	 * @param text
	 */
	private Scope(final int value) {
		this.value = value;
	}

	/**
	 * @return the value of the scope
	 */
	public int getValue() {
		return value;
	}

	public static Scope valueOf(int value) {
		Scope result = null;
		switch (value) {
		case 0:
			result = Scope.ALL;
			break;
		case 1:
			result = Scope.CLASS;
			break;
		case 2:
			result = Scope.METHOD;
			break;
		default:
			break;
		}
		return result;
	}
}