package net.compsoc.ox.database.util;

import java.util.Calendar;
import java.util.Date;

public class TermDatesUtil {
    
    /**
     * Return an integer representing which week of term the given date is.
     * 
     * @param mondayWeek1 - the date of monday of week 1 of the term
     * @param event - the date to work out which week it resides in
     * @return
     */
    public static int getTermWeek(Date mondayWeek1, Date date) {
        Calendar mondayWeek1Cal = Calendar.getInstance();
        mondayWeek1Cal.setTime(mondayWeek1);
        
        Calendar dateCal = Calendar.getInstance();
        dateCal.setTime(date);
        
        return dateCal.get(Calendar.WEEK_OF_YEAR) - mondayWeek1Cal.get(Calendar.WEEK_OF_YEAR) + 1;
    }
    
}