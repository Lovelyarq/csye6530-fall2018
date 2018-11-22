/**Written in the classroom
 * package module7;	

import java.util.logging.Level;
import java.util.logging.Logger;




public class CoapClientApp {
	
	//static
	
	private static final Logger _logger =
			Logger.getLogger(CoapClientApp.class.getName());

	private static CoapClientApp _App = null;
	
	
	public CoapClientApp()
	{
		super();
		//_coapClient = new CoapCommClient("coap","localhost",5683);
		_coapClient = new CoapCommClient("coap","localhost",5683);
	}
	
	/*
	 * 
	 * Starts the App, this will create an instance of the client 
	 * CoAP connection, and run a bunch of tests
	 //
	
	public void start()
	{
		CoapClientConnection clienConn = new CoapClientConnection();
		
		//lienConn.runTest();
		
		clienConn.sendGetRequest("temp");
		clienConn.sendGetRequest("humidity");
	}
	
	
	public static void main(String[] args)
	{
		_App = new CoapClientApp();
		
		try {
			 _App.start();
			 
		 }catch (Exception e) {
			 _logger.log(Level.SEVERE, "Bad" ,e);
		 }
	}
	
	private CoapCommClient _coapClient;
	
	public CoapClientApp1() {
		
	}
	
	
	
	

}
 


*/

package module7;

import java.util.logging.Logger;

public class CoapClientApp{
	
	 // static
	 private static final Logger _Logger =
		Logger.getLogger(CoapClientApp.class.getName());
	 private static CoapClientApp _App;
	 
	 /**
	 * @param args
	 */
	 
	 public static void main(String[] args){
		 _App = new CoapClientApp();
		 try {
			 _Logger.info("ClientApp.start!!");
			 _App.start();
		 } catch (Exception e) {
			 _Logger.info("ClientApp.start Failed!!!");
			 e.printStackTrace();
	 	 }
	 }
	 
	 // private var's
	 private CoapClientConnection _coapClient;
	 
	 // constructors
	 public CoapClientApp(){
		 super();
	 }
	 
	 // public methods
	 /**
	 * Connect to the CoAP server
	 *
	 */
	 public void start(){
		 _coapClient = new CoapClientConnection();
		 _coapClient.runTests("temp");
	 }
}