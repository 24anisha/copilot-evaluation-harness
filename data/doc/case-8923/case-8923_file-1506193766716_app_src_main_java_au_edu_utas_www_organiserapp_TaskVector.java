package au.edu.utas.www.organiserapp;


import android.content.Context;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.Vector;

/**
 * Created by Rhys on 19/05/2017.
 */

public class TaskVector extends Vector<taskObject> implements Serializable{
    private static final long serialVersionUID = -29238982928391L;
    public void save(String name, Context ctx) {
        TaskVector thisList = this;
        try {
            File file = new File(ctx.getFilesDir(), name);
            if(!file.exists()) {
                file.createNewFile();
            }
            FileOutputStream fos = ctx.openFileOutput(name, Context.MODE_PRIVATE);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(thisList);
            oos.close();
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }

    public TaskVector load(String name, Context ctx) {
        try {
            ObjectInputStream input = new ObjectInputStream(new FileInputStream(new File(new File(ctx.getFilesDir(),"")+File.separator+name)));
            TaskVector loaded = (TaskVector) input.readObject();
            input.close();
            return loaded;
        }
        catch(IOException e) {
            e.printStackTrace();
            return new TaskVector();
        }
        catch(ClassNotFoundException e) {
            e.printStackTrace();
            return new TaskVector();
        }
    }
}