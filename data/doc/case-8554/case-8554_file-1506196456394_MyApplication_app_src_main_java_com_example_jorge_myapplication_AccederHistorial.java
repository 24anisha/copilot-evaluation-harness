package com.example.jorge.myapplication;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class AccederHistorial extends AppCompatActivity {

    public final static String EXTRA_CONSULTA = "consulta";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_acceder_historial);

        final ListView listview = (ListView) findViewById(R.id.LLista2);
        ArrayList<String> lista = new ArrayList<String>();
        final Activity actividad = this;

        try {
            String linea;
            BufferedReader reader = new BufferedReader(new InputStreamReader(openFileInput("Historial.txt")));
            while ((linea = reader.readLine()) != null){
                lista.add(0, linea);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //Log.i("Lista", lista.toString());
        final ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, lista);
        listview.setAdapter(adapter);

    }

    public void borrarHistorial(View view) {
        deleteFile("Historial.txt");
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}