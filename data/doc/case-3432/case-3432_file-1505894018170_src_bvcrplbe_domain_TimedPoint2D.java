package bvcrplbe.domain;

import java.awt.geom.Point2D;
import java.awt.geom.Point2D.Double;

public class TimedPoint2D{

	
	private double latitude;
	private double longitude;
	private long touchTime;
	
	public TimedPoint2D(){};
	
	public TimedPoint2D(double latitude, double longitude, long touchTime) {
		super();
		this.latitude = latitude;
		this.longitude = longitude;
		this.touchTime = touchTime;
	}

	public double getLatitude() {
		return latitude;
	}

	public void setLatitude(double latitude) {
		this.latitude = latitude;
	}

	public double getLongitude() {
		return longitude;
	}

	public void setLongitude(double longitude) {
		this.longitude = longitude;
	}

	public long getTouchTime() {
		return touchTime;
	}

	public void setTouchTime(long touchTime) {
		this.touchTime = touchTime;
	}

	

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		TimedPoint2D other = (TimedPoint2D) obj;
		if (latitude != other.latitude)
			return false;
		if (longitude != other.longitude)
			return false;
		if (touchTime != other.touchTime)
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "TimedPoint2D [latitude=" + latitude + ", longitude=" + longitude + ", touchTime=" + touchTime + "]";
	}
	
	

}