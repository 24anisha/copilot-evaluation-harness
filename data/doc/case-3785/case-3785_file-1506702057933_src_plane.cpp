#include "plane.hpp"
#include <stdio.h>

void Plane::resize(int width, int height) {
	if (width < 0) {
		width = 0;
	}
	if (height < 0) {
		height = 0;
	}
	this->width = width;
	this->height = height;
	if (data != 0) {
		delete data;
	}

	data = new unsigned char[width * height *3];
}

Plane::Plane(int width, int height) {
	data = 0;
	resize(width, height);
	up = 1.0;
	down = -1.0;
	left = -1.0;
	right = 1.0;
}

Plane::~Plane() {
	if (data != 0) {
		delete data;
	}
}