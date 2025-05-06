package tda367.myapplication.service;

import android.content.Context;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by: Tobias
 * Responsibility: Reading from .txt files containing all level texts
 * Used by: HashMapCreator
 * Uses:
 */

public class FileReader {

    private String stringWRows;
    private String string;
    List<String> strings;

    //Method returns array containing each part of a level
    public List<String> getTextArray(String filename, Context context){
        try {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(context.getAssets().open(filename)));
            strings = new ArrayList<>();
            String lineOfContent = bufferedReader.readLine();
            while (lineOfContent != null){
                rowCheck(lineOfContent);
                strings.add(string);
                lineOfContent = bufferedReader.readLine();
            }
        } catch (IOException e){

        }
        return strings;
    }

    //Returns The same string but with newlines
    private String getStringWRows(String fileString){
        stringWRows = "";
        setNewRows(fileString);
        return stringWRows;
    }

    //Method for setting the new rows
    private void setNewRows(String fileString){
        String[] splitString = fileString.split("row");
        for (String string:splitString){
            stringWRows = stringWRows + string + "\n";
        }
    }

    //Method for checking if line has "row"
    private void rowCheck (String lineOfContent) {
        if (lineOfContent.contains("row")){
            string = getStringWRows(lineOfContent);
        }
        else {
            string = lineOfContent;
        }
    }
}