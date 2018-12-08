
package module6;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * @author Ruiqing Jiang
 *
 */
public class MqttSubClientTestApp {

	// static
	private static final Logger _Logger = Logger.getLogger(MqttSubClientTestApp.class.getName());
	private static MqttSubClientTestApp _App;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new MqttSubClientTestApp();
		try {
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.WARNING, "Failed!! to start _App.", e);
		}
	}

	// params
	private MqttConnGateToDev _Client;

	// constructors
	/**
	 * Default.
	 */

	public MqttSubClientTestApp() {
		super();
	}

	// public methods
	/**
	 * Connect to the MQTT client, then: 1) If this is the subscribe app, subscribe
	 * to the given topic 2) If this is the publish app, publish a test message to
	 * the given topic
	 */
	public void start() {
		_Client = new MqttConnGateToDev();
		_Client.connect();
		//Subscribe with the topic
		String topic = "Assignment6";
		_Client.subscribeToTopic(topic); 
		
		//_Client.subscribeToAll(); 
		//_Client.disconnect();
	}

}
