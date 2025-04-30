package omelet.data;

import java.util.concurrent.TimeUnit;

import org.apache.log4j.Logger;

import com.google.common.base.Stopwatch;

public class PrettyMessage implements Runnable {

	private boolean keepRunning = true;
	private static final Logger LOGGER = Logger.getLogger(PrettyMessage.class);
	
	
	public void swtichOffLogging(){
		keepRunning = false;
	}
	@Override
	public void run() {
		Stopwatch sw = new Stopwatch();
		sw.start();
		LOGGER.info("Please wait while we are building your testData");
		StringBuilder sb = new StringBuilder();
		while(keepRunning){
			sb.append(".");
			LOGGER.info(sb.toString());
			sleep(1);
		}
		LOGGER.info("Time taken to build data in seconds is:"+sw.elapsedTime(TimeUnit.SECONDS));
		sw.stop();
		
	}
	
	public void sleep(int timeInSeconds){
		try {
			Thread.sleep(timeInSeconds*1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			LOGGER.info(e);
		}
	}
	
	
	

}