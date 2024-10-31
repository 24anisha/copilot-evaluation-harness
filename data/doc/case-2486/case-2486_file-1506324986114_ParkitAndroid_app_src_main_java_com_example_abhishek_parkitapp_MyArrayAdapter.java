package com.example.abhishek.parkitapp;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class MyArrayAdapter extends ArrayAdapter<String> {
    private final Context context;
    private final String[] values;

    public MyArrayAdapter(Context context, String[] values) {
        super(context, R.layout.mylist);
        this.context = context;
        this.values = values;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        View rowView = inflater != null ? inflater.inflate(R.layout.mylist, parent, false) : null;
        TextView textView = (TextView) rowView.findViewById(R.id.label);
        ImageView imageView = (ImageView) rowView.findViewById(R.id.logo);
        textView.setText(values[position]);

        // Change icon based on name
        String s = values[position];

        System.out.println(s);

        if (s.equals("Make a Reservation")) {
            imageView.setImageResource(R.drawable.icon_calendar_black);
        } else if (s.equals("Upcoming Reservations")) {
            imageView.setImageResource(R.drawable.icon_loaction_black);
        } else if (s.equals("Slot Locator")) {
            imageView.setImageResource(R.drawable.icon_calendar_black);
        }else if(s.equals("Transaction History")){
            imageView.setImageResource(R.drawable.icon_loaction_black);
        }

        return rowView;
    }

    @Override
    public int getCount() {
        return 4;
    }
}