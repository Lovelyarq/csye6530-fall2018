/*Written in the classroom
package module7;	

import java.util.logging.Level;
import java.util.logging.Logger;


//With great power with great responsibility

public class CoapServerApp {
	
	private static final Logger _logger =
			Logger.getLogger(CoapServerApp.class.getName());

	private static CoapServerApp _App = null;
	
	
	public CoapServerApp()
	{
		super();
	}
	
	/*
	 * 
	 * Starts the App, this will create an instance of the client 
	 * CoAP connection, and run a bunch of tests
	 *
	
	public void start()
	{
		CoapServerConnection serverConn = new CoapServerConnection();
		
		serverConn.start();
		//serverConn.stop();
	}
	
	public static void main(String[] args)
	{
		 try {
			 _App = new CoapServerApp();
			 
			 _App.start();
		 }catch (Exception e) {
			 _logger.log(Level.SEVERE, "Bad" ,e);
		 }
	}

}

*/


package module7;
import java.util.logging.Logger;

public class CoapServerApp{
	
	 // static
	 private static final Logger _Logger =
			 Logger.getLogger(CoapServerApp.class.getName());
	 private static CoapServerApp _App;
	 /**
	 * @param args
	 */
	 
	 public static void main(String[] args){
		 _App = new CoapServerApp();
		 try {
			 _Logger.info("ServerApp.start!!");
			 _App.start();
		 } catch (Exception e) {
			 _Logger.info("ServerApp.start Failed!!");
		 }
	 }
	 
	 // private var's
	 private CoapServerConnection _coapServer;
	 
	 // constructors
	 public CoapServerApp(){
		 super();
	 }
	 
	 // public methods
	 public void start(){
		 _coapServer = new CoapServerConnection();
		 _coapServer.start();
	 }
	 
}
