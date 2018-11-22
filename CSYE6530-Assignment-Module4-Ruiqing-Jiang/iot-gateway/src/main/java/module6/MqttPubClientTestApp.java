
package module6;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * @author Ruiqing Jiang
 *
 */
public class MqttPubClientTestApp {
	// static
	private static final Logger _Logger = Logger.getLogger(MqttPubClientTestApp.class.getName());
	private static MqttPubClientTestApp _App;
	
	// params
	private MqttClientConnector _Client;
	
	/**
	 * 
	 */
	public MqttPubClientTestApp() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new MqttPubClientTestApp();
		try {
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.WARNING, "Failed!! to start _App.", e);
		}
	}
	
	// public methods
	/**
	 * Connect to the MQTT client and publish a test message to the given topic
	 */
	public void start() {
		//Create a new MqttClient:_Client and connection
		_Client = new MqttClientConnector();
		_Client.connect();
		
		//Set topic 
		String topic = "Assignment6";
		
		// Set the payload for publishing...
		String payload = "Ha!!You already finished this assignment! Be happy~~";
		//publish payload with the topic in Qoslevel 2
		_Client.publishMessage(topic, 2, payload.getBytes());
		_Client.disconnect();
	}

}
