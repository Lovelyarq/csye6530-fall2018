/**
 * 
 */
package mqtt;

import java.util.logging.Logger;


/**
 * @author xingli
 *
 */
public class MqttSubClientTestApp extends Thread{

	// static
	private static final Logger _Logger = Logger.getLogger(MqttSubClientTestApp.class.getName());
	private static MqttSubClientTestApp _App;
	// parameters
	private MqttClientConnection _mqttClient;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new MqttSubClientTestApp();
		try {
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}


	// constructors
	/**
	 * Default constructor
	 */

	public MqttSubClientTestApp() {
		super();
	}

	// public methods
	/**
	 * Connect to the MQTT client, and subscribe to the given topic
	 * unsubscribe the topic after 80s, then disconnect with the MQTT client
	 */
	public void start() {
		_mqttClient = new MqttClientConnection();
		_mqttClient.connect();
		String topicName = "xingli";
		_mqttClient.subscribeToTopic(topicName); // subscribe to the given topic
		//_mqttClient.subscribeToAll(); // subscribe all the topic
		try {
			sleep(80000);
			_mqttClient.unSubscribeToTopic(topicName);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		_mqttClient.disconnect();
	}

}
