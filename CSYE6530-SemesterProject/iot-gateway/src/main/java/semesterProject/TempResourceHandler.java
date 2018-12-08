package semesterProject;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.core.server.resources.CoapExchange;

/**
 * @author Ruiqing Jiang
 *
 */

public class TempResourceHandler extends CoapResource {
	// static
	private static final Logger _Logger = Logger.getLogger(TempResourceHandler.class.getName());

	
	private String _userName = "A1E-hRhHhHVjakJvL8VNMxjLCzfNN7BOMJ";
	private String _authToken = null;
	private String _pemFileName = "/Users/jrq/Documents/pem/ubidots.pem";
	private String _host = "things.ubidots.com";
	
	private MqttClientConnector _Client;
	
	// constructors 
	public TempResourceHandler() {
		super("temp");
		// TODO Auto-generated constructor stub
	}

	public TempResourceHandler(String name) {
		super(name);
		// TODO Auto-generated constructor stub
	}

	/**
	 * @param name
	 * @param visible
	 */
	public TempResourceHandler(String name, boolean visible) {
		super(name, visible);
	}

	// public methods

	@Override
	/**
	 * Post is to create a resource
	 * Add MQTT part:
	 * After handlePOST, we can get the temp value from senseHat by COAP protocol
	 * And the value would get by ce.getRequestText() and send it to mqtt payload.
	 * Then, we use mqtt protocol--publish the value to the broker, cloud. 
	 * Final, the ubidots will get the sensor value from senseHat and decide to upload the event or not.
	 */
	public void handlePOST(CoapExchange ce) {
		String responseMsg = "Here's the reponse to temp request::" + super.getName();

		System.out.println(ce.getRequestText());
		ce.respond(ResponseCode.VALID, responseMsg);
		
		
		_Client = new MqttClientConnector(_host, _userName, _pemFileName, _authToken);
		//_ClientPC.connectPC();	
		_Client.connect();
		String topic = "/v1.6/devices/homeiotgateway/tempsensor";
		// Set the temperature to what we get from the Raspberry Pi
		String payload = ce.getRequestText();
		
		//publish payload with the topic in Qoslevel 0
		_Client.publishMessage(topic, 0, payload.getBytes());
		_Client.disconnect();
	

		_Logger.info("Handling POST:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
		
		
		
		
		
	}

	@Override
	/**
	 * Put is to update a resource
	 *
	 */
	public void handlePUT(CoapExchange ce) {
		String responseMsg = "Here's the reponse to temp request::" + super.getName();

		ce.respond(ResponseCode.VALID, responseMsg);

		_Logger.info("Handling PUT:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}

	@Override
	/**
	 * Get is to read or get a resource
	 *
	 */
	public void handleGET(CoapExchange ce) {

		String responseMsg = "Here's the reponse to temp request::" + super.getName();
		
		
		ce.respond(ResponseCode.VALID, responseMsg);

		_Logger.info("Handling GET:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
		
	}

	@Override
	/**
	 * Post is to delete a resource
	 *
	 */
	public void handleDELETE(CoapExchange ce) {
		String responseMsg = "Here's the reponse to temp request::" + super.getName();

		ce.respond(ResponseCode.VALID, responseMsg);

		_Logger.info("Handling DELETE:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());

	}
}
