package com.rs.math.geometry.shape;

import com.rs.math.geometry.Constants;

public class Point {
    public final double x;
    public final double y;
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public Point(Point point) {
        this.x = point.x;
        this.y = point.y;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Point) {
            return same(this, (Point) obj);
        } else {
            return super.equals(obj);
        }
    }
    public static boolean same(Point p1, Point p2) {
        return same(p1, p2, Constants.EPSILON);
    }
    public static boolean same(Point p1, Point p2, double epsilon) {
        return Math.abs(p1.x - p2.x) < epsilon && Math.abs(p1.y - p2.y) < epsilon;
    }
}