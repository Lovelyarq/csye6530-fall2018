//written in the classroom
package module7;



import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.core.server.resources.CoapExchange;


public class TempResourceHandler extends CoapResource {
	//static
	private static final Logger _Logger = 
			Logger.getLogger(TempResourceHandler.class.getName());
	
	//constructors, set name to temp
	public TempResourceHandler() {
		super("temp");
	}
	
	public TempResourceHandler(String name) {
		super(name);
	}

	public TempResourceHandler(String name, boolean visible) {
		super(name, visible);
	}
	
	//public methods
	
	@Override
	//handleGET
	public void handleGET(CoapExchange ce) {
		
		String responseMsg =  "Here's the reponse to TEMP request::" + super.getName();

		ce.respond(ResponseCode.VALID, responseMsg);
		
		_Logger.info("Handling GET:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	@Override
	//handlePOST
	public void handlePOST(CoapExchange ce) {
		String responseMsg =  "Here's the reponse to temp request::" + super.getName();

		System.out.println("HHHHHHHH" + ce.getRequestText());
		ce.respond(ResponseCode.VALID, responseMsg);
		
		_Logger.info("Handling POST:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	@Override
	//handlePUT
	public void handlePUT(CoapExchange ce) {
		String responseMsg =  "Here's the reponse to temp request::" + super.getName();
		
		ce.respond(ResponseCode.VALID, responseMsg);
		
		_Logger.info("Handling PUT:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	@Override
	//handleDELETE
	public void handleDELETE(CoapExchange ce) {
		String responseMsg =  "Here's the reponse to temp request::" + super.getName();
		
		ce.respond(ResponseCode.VALID, responseMsg);
		
		_Logger.info("Handling DELETE:" + responseMsg);
		_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
	}
	
	

}
