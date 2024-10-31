package tda367.myapplication.service;

import android.content.Context;
import android.content.ContextWrapper;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;


/**
 * @author Hanna Carlsson
 * Responsibility: Handles the storing and loading of objects
 * Used by: MainActivity, UpdateUserFragment, MyPageFragment
 */

public class UserFileReader {

    private static UserFileReader instance = new UserFileReader();

    private UserFileReader() {}

    private File myPath;

    public static UserFileReader getInstance() {
        return instance;
    }

    //Loads the stored object, and returns it, otherwise throws exception
    public ObjectInputStream loadObject(Context context) throws IOException {
        ContextWrapper cw = new ContextWrapper(context);
        File directory = cw.getDir("dataDir", Context.MODE_PRIVATE);
        myPath = new File(directory, "users");
        return new ObjectInputStream(new FileInputStream(myPath));
    }

    //Saves the object, is called in onDestory() from MainActivity
    public void saveObject(Context context, Object manager) {
        ContextWrapper cw = new ContextWrapper(context);
        File directory = cw.getDir("dataDir", Context.MODE_PRIVATE);
        myPath = new File(directory, "users");
        try {
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(new FileOutputStream(myPath));
            objectOutputStream.writeObject(manager);
            objectOutputStream.flush();
            objectOutputStream.close();
        } catch (IOException e) {
            //TODO add catch
        }
    }

}