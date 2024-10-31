package com.pasodoff.hcp.badapple.service;

import org.springframework.stereotype.Component;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Created by aaron on 19/06/2017.
 */
@Component
public class CmdService {

    private static String command = "nslookup ";
    public CmdService() {
    }

    public String nslookup(String address){
        StringBuffer output = new StringBuffer();
        String fullCmd = command + address;

        Process p;
        try {
            //TODO: Unsanitized commandline input
            p = Runtime.getRuntime().exec(fullCmd);
            p.waitFor();
            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(p.getInputStream()));

            String line = "";
            while ((line = reader.readLine())!= null) {
                output.append(line + "\n");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return fullCmd + "\n" + output.toString();
    }
}