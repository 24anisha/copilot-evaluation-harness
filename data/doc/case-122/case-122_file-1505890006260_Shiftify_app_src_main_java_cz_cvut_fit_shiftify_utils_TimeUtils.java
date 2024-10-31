package cz.cvut.fit.shiftify.utils;

import org.joda.time.format.DateTimeFormat;
import org.joda.time.format.DateTimeFormatter;

import java.util.Calendar;

/**
 * Created by petr on 12/11/16.
 */

public class TimeUtils {

    public static DateTimeFormatter JODA_TIME_FORMATTER = DateTimeFormat.forPattern("HH:mm");

    private static final String TAG = "MY_TIME_UTILS";

    public static String timeToString(int minutes) {
        return timeToString(getHour(minutes), getMinutes(minutes));
    }

    public static String timeToString(int hour, int minute) {
        String res = "";
        if (hour < 10) {
            res += "0";
        }
        res += String.valueOf(hour) + ":";
        if (minute < 10) {
            res += "0";
        }
        res += String.valueOf(minute);
        return res;
    }

    public static int StringToTime(String time) {
        Calendar calendar = Calendar.getInstance();
        String[] nums = time.split(":");
        if (nums.length == 2) {
            int h = Integer.parseInt(nums[0], 10);
            int m = Integer.parseInt(nums[1], 10);
            return h * 60 + m;
        } else {
            throw new IllegalArgumentException("Bad time format");
        }
    }

    public static int getHour(int minutes) {
        return minutes / 60;
    }

    public static int getMinutes(int minutes) {
        int hours = minutes / 60;
        return minutes - 60 * hours;
    }

    public int getTimeDuration(int start, int stop) {
        if (start < stop) {
            return stop - start;
        } else if (start == start) {
            return 0;
        } else {
            return 24 * 60 - start + stop;
        }
    }


}