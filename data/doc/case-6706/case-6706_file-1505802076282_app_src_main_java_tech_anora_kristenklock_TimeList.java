package tech.anora.kristenklock;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ListView;
import java.util.ArrayList;

/*
* Project Title: Kristen Klock
* Class: COMP590, Spring 2017
* Date: 5/2/17
* Authors: Sifron Benjamin and Collin Makohon
 */

public class TimeList extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_time_list);

        ArrayList<SensorAlarm> sensorsArray = (ArrayList<SensorAlarm>)MainActivity.getAlarms();
        AlarmListAdapter adapter = new AlarmListAdapter(this, sensorsArray);

        ListView listView = (ListView) findViewById(R.id.alarmsList);
        listView.setAdapter(adapter);

    }

    public void launchMainActivity(View view)
    {
        finish();
    }

}