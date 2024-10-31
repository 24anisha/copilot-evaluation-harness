package br.com.costa.agenda.clients;

import java.io.PrintStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

/**
 * Created by Lauciano FA on 01/05/2017.
 */

public class WebClient {
    public String post(String js) {

        try {
            URL url = new URL("https://www.caelum.com.br/mobile");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestProperty("Content-type", "application/json");
            connection.setRequestProperty("Accept", "application/json");

            connection.setDoOutput(true);

            PrintStream output = new PrintStream(connection.getOutputStream());

            output.println(js);

            connection.connect();

            Scanner scanner = new Scanner(connection.getInputStream());
            String response = scanner.next();

            return response;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

}