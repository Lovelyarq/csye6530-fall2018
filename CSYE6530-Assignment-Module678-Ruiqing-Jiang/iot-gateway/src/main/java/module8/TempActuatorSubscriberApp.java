package module8;

import java.util.logging.Level;
import java.util.logging.Logger;

import module8.MqttClientConnector;

public class TempActuatorSubscriberApp {
	
	private String _userName = "******";//This is a personal information
	private String _authToken = null;
	private String _pemFileName = "********/pem/ubidots.pem";//This is a personal information
	private String _host = "things.ubidots.com";

	
	// static
	private static final Logger _Logger = Logger.getLogger(TempActuatorSubscriberApp.class.getName());
	private static TempActuatorSubscriberApp _App;
	
	// params
	private MqttClientConnector _Client;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_App = new TempActuatorSubscriberApp();
		try {
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.WARNING, "Failed!! to start _App.", e);
		}
	}
	
	// constructors
	/**
	 * Default.
	 */

	public TempActuatorSubscriberApp() {
		super();
	}
	
	// public methods
	/**
	 * Connect to the MQTT client, then: 1) If this is the subscribe app, subscribe
	 * to the given topic 2) If this is the publish app, publish a test message to
	 * the given topic
	 */
	public void start() {
		_Client = new MqttClientConnector(_host, _userName, _pemFileName, _authToken);
		_Client.connect();
		//Subscribe with the topic
		String topic = "/v1.6/devices/homeiotgateway/tempactuator";
		_Client.subscribeToTopic(topic); 
		//_Client.subscribeToAll(); 
		//_Client.disconnect();
	}
	
	
	

}
