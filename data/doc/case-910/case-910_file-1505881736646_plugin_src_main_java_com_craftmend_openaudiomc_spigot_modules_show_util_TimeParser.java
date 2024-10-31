package com.craftmend.openaudiomc.spigot.modules.show.util;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class TimeParser {

    public static Long toMilis(String input) {
        Long time = 0L;

        // ITS A TIMECODE
        if (input.contains(":")) {
            return Long.valueOf(LocalTime.parse(input, DateTimeFormatter.ofPattern("HH:mm:ss")).toSecondOfDay()* 1000);
        }

        input = input.toLowerCase() + "-";

        String[] milisSplit = input.split("ms");
        if (isValid(milisSplit)) {
            time += Long.parseLong(milisSplit[0]);
            input = input.replace(milisSplit[0] + "ms", "");
            return time;
        }

        String[] secondsSplit = input.split("s");
        if (isValid(secondsSplit)) {
            time += Math.round(Double.parseDouble(secondsSplit[0]) * 1000);
            input = input.replace(secondsSplit[0] + "s", "");
            return time;
        }

        String[] minutesSplit = input.split("m");
        if (isValid(minutesSplit)) {
            time += Math.round(Double.parseDouble(minutesSplit[0]) * 60000);
            input = input.replace(minutesSplit[0] + "m", "");
            return time;
        }

        String[] tickSplit = input.split("t");
        if (isValid(tickSplit)) {
            time += Math.round(Integer.parseInt(tickSplit[0]) * 50);
            return time;
        }

        return time;
    }

    private static boolean isValid(String[] array) {
        return array.length > 1 && array[0].length() > 0;
    }

}