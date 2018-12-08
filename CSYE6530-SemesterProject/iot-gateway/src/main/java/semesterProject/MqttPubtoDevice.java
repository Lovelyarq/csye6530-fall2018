
package semesterProject;

import java.util.logging.Level;
import java.util.logging.Logger;

import org.eclipse.paho.client.mqttv3.MqttMessage;

/**
 * @author Ruiqing Jiang
 *
 */
public class MqttPubtoDevice {
	// static
	private static final Logger _Logger = Logger.getLogger(MqttPubtoDevice.class.getName());
	private static MqttPubtoDevice _App;
	
	// params
	private MqttConnGateToDev _Client;
	
	/**
	 * 
	 */
	public MqttPubtoDevice() {
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new MqttPubtoDevice();
		try {
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.WARNING, "Failed!! to start _App.", e);
		}
	}
	
	// public methods
	/**
	 * Connect to the MQTT client and publish a test message to the given topic
	 * The publish part for Gateway to Device is using in the MqttClientConnect.java
	 * in here : public void messageArrived(String data, MqttMessage msg) throws Exception {
	 * This start is just a example for testing.
	 * 
	 */
	public void start() {
		//Create a new MqttClient:_Client and connection
		_Client = new MqttConnGateToDev();
		_Client.connect();
		
		//Set topic 
		String topic = "ActuatorData";
		
		// Set the payload for publishing...
		String payload = "Ha!!You already finished this assignment! Be happy~~";
		//publish payload with the topic in Qoslevel 2
		_Client.publishMessage(topic, 2, payload.getBytes());
		_Client.disconnect();
	}

}
