package mobidev.com.dunstan;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class SplashActivity extends AppCompatActivity {

    // Splash screen timer
    private static int SPLASH_TIME_OUT = 3000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        final SharedPreferences preferences = getSharedPreferences("dunstan", Context.MODE_PRIVATE);
        new Handler().postDelayed(new Runnable() {

            /*
             * Showing splash screen with a timer. This will be useful when you
             * want to show case your app logo / company
             */

            @Override
            public void run() {
                // This method will be executed once the timer is over
                // Start your app main activity
                Boolean isLoggedIn = preferences.getBoolean("loggedIn", false);
                if (isLoggedIn) {
//                    Intent i = new Intent(SplashActivity.this, LogInActivity.class);
//                    startActivity(i);
                } else {
                    Intent i = new Intent(SplashActivity.this, FirstSetupActivity.class);
                    startActivity(i);
                }
            }
        }, SPLASH_TIME_OUT);
    }
}