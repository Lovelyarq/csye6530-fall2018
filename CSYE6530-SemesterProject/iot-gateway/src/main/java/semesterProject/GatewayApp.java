package semesterProject;

import java.util.logging.Logger;

/**
 * @author Ruiqing Jiang
 *
 */

public class GatewayApp{
	
	//private var's
	private static final Logger _Logger =
	 Logger.getLogger(GatewayApp.class.getName());
	private static GatewayApp _APP;
	private CoapServerConnection _Server;
	/**
	* @param args
	*/

	/**
	 * Constructor.
	 * Default
	 *
	 */
	public GatewayApp() {
		
	}
	
	// public methods
	/**
	 * Start COAP server method
	 *
	 */
	public void start() {
			_Server = new CoapServerConnection();
			_Server.start();

	}

	public static void main(String[] args) {
		
		 _APP = new GatewayApp();
		 try {
			 _Logger.info("ServerApp.start!!");
			 //coap server start
			 _APP.start();
		 } catch (Exception e) {
			 _Logger.info("ServerApp.start Failed!!");
		 }
		
	}
	
}

