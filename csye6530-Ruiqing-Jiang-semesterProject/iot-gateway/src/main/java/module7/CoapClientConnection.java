/*Written in the classroom

package module7;

import java.util.Set;
import java.util.logging.Logger;

import org.eclipse.californium.core.CoapClient;
import org.eclipse.californium.core.CoapResponse;
import org.eclipse.californium.core.WebLink;

public class CoapClientConnection {


	//static
	
	//private var's 
	
	private static final Logger _Logger =
			Logger.getLogger(CoapClientConnection.class.getName());
	
	private String     _protocol = "coap";
	//private String   _host	 = "californium.eclipse.org"
	private String     _host 	 = "localhost";
	private int        _port 	 = 5683;
	private String     _connUrl  = null;
	
	private String     _serverAddr;
	
	private CoapClient _coapClient;
	
	
	//Contractors
	
	/*
	 * 
	 * Default
	 * 
	 
	
	public CoapClientConnection()
	{
		super();
		System.out.println("ssssssssssssssssss" + _connUrl);
		_connUrl = new String(_protocol + "://" + _host + ":" + _port + "");
		
	}
	
	public CoapClientConnection(String host, int port, boolean isSeCure)
	{
		super();
		if(isSecure) {
			_protocol = ConfigConst.SECURE_COAP_PROTOCOL;
			_port     = ConfigConst.
		}
	}
	
	
	public void runTest()
	{
		System.out.println("ping:   ");
		pingServer();
		System.out.println("display:   ");
		displayResources();
		System.out.println("Get:   ");
		sendGetRequest();
		
	}
	
	public void pingServer()
	{
		initClient();
		
		if (_coapClient.ping()) {
			_Logger.info("Ping successful");
		};
		
		
	}
	
	public void displayResources()
	{
		initClient();
		
		_Logger.info("Getting all remote web links...");
		
		Set<WebLink> webLinkSet = _coapClient.discover();
		
		for (WebLink w1 : webLinkSet) {
			_Logger.info(w1.getURI());
		}
	}
	
	public void sendGetRequest()
	{
		sendGetRequest(null);
	}
	/*
	 * 
	 * 'resource' should ONLY be the file path
	 * 
	 * @param resource
	 
	public void sendGetRequest(String resource)
	{
		initClient(null);
		
		CoapResponse response = _coapClient.get();
		byte[] rawPayload = response.getPayload();
		
		_Logger.info("Payload for GET: " + new String(rawPayload));
		
	}
	public void sendPostRequest()
	{
		
	}
	public void sendPushRequest()
	{
		
	}
	
	//private method
	private void initClient()
	{
		initClient(null);
	}
	private void initClient(String resource)
	{
		if(_coapClient != null) {
			_coapClient.shutdown();
			_coapClient = null;
		}
		if(resource != null && resource.trim().length() > 0) {
			_coapClient = new CoapClient(_connUrl + resource);
		}else {
			_coapClient = new CoapClient(_connUrl);
		}
	}

}

*/


package module7;

import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.eclipse.californium.core.CoapClient;
import org.eclipse.californium.core.CoapResponse;
import org.eclipse.californium.core.WebLink;
import org.eclipse.californium.core.coap.MediaTypeRegistry;
import common.ConfigConst;



public class CoapClientConnection{
	
	 // static
	 private static final Logger _Logger = Logger.getLogger(CoapClientConnection.class.getName());
	 
	 // params
	 private String _protocol;
	 private String _host;
	 private int _port;
	 private String _serverAddress;
	 private CoapClient _clientConnect;
	 private boolean _isInitialized;
	 
	 // constructors
	 public CoapClientConnection(){
		 this(ConfigConst.DEFAULT_COAP_SERVER, false);
	 }
	 
	 /**
	  * Constructor.
	  *
	  * @param host
	  */
	  public CoapClientConnection(String host, boolean isSecure){
		  super();
		  
		  if (isSecure) {
			  _protocol = ConfigConst.SECURE_COAP_PROTOCOL;
			  _port = ConfigConst.SECURE_COAP_PORT;
		  } 
		  else {
			  _protocol = ConfigConst.DEFAULT_COAP_PROTOCOL;
			  _port = ConfigConst.DEFAULT_COAP_PORT;
		  }
		  
		  if (host != null && host.trim().length() > 0) {
			  _host = host;
		  } 
		  else {
			  _host = ConfigConst.DEFAULT_COAP_SERVER;
		  }
		   
		  // NOTE: URL does not have a protocol handler for "coap", construct the URL manually
		  
		  
		  //_serverAddress = _protocol + "://" + _host + ":" + _port;
		  
		  _serverAddress = "coap://192.168.0.130:5683";
		  _Logger.info("Using URL for server conn: " + _serverAddress);
	  }
	  
	  // public methods
	  
	  public void runTests(String resourceName){
		  try {
			  _isInitialized = false;
			  initClient(resourceName);
			  _Logger.info("Current URI: " + getCurrentUri());
			  String payload = "Sample payload.HAHAHAHAHA!!!!!!Finddddallllllllllyyyyyyy success!!!!!!!!!!!!";
			  
			  pingServer();
			  discoverResources();
			  
			  sendGetRequest();
			  sendGetRequest(true);
			  sendPostRequest(payload, false);
			  sendPostRequest(payload, true);
			  sendPutRequest(payload, false);
			  sendPutRequest(payload, true);
			  sendDeleteRequest();
			  
		  } catch (Exception e) {
			  _Logger.log(Level.SEVERE, "Failed to issue request to CoAP server.", e);
		  }
	  }
	  
	  /**
	  * Returns the CoAP client URI 
	  * @return String
	  */
	  
	  public String getCurrentUri(){
		  return (_clientConnect != null ? _clientConnect.getURI() : _serverAddress);
	  }
	  
	  public void discoverResources(){
		  _Logger.info("Issuing discover...");
		  initClient();
		  Set<WebLink> weblinkSet = _clientConnect.discover();
		  
		  if (weblinkSet != null) {
			  for (WebLink wls : weblinkSet) {
				  _Logger.info(" --> WebLink: " + wls.getURI());
			  }
		  }
	  }
	  
	  //ping
	  public void pingServer(){
		  _Logger.info("Sending ping...");
		  initClient();
			if (_clientConnect.ping()) {
				_Logger.info("Ping successful");
			};
	  }
	  
	  public void sendDeleteRequest(){
		  initClient();
		  handleDeleteRequest();
	  }
	  
	  public void sendDeleteRequest(String resourceName){
		  _isInitialized = false;
		  initClient(resourceName);
		  handleDeleteRequest();
	  }
	  
	  public void sendGetRequest(){
		  initClient();
		  handleGetRequest(false);
	  }
	  
	  public void sendGetRequest(String resourceName) {
		  _isInitialized = false;
		  initClient(resourceName);
		  handleGetRequest(false);
	  }
	  
	  public void sendGetRequest(boolean useCON){
		  initClient();
		  handleGetRequest(useCON);
	  }
	  
	  public void sendGetRequest(String resourceName, boolean useCON){
		  _isInitialized = false;
		  initClient(resourceName);
		  sendGetRequest(useCON);
	  }
	  
	  public void sendPostRequest(String payload, boolean useCON){
		  initClient();
		  handlePostRequest(payload, useCON);
	  }
	  
	  public void sendPostRequest(String resourceName, String payload, boolean useCON){
		  _isInitialized = false;
		  initClient(resourceName); 
		  handlePostRequest(payload, useCON);
	  }
	  
	  public void sendPutRequest(String payload, boolean useCON){
		  initClient();
		  handlePutRequest(payload, useCON);
	  }
	  
	  public void sendPutRequest(String resourceName, String payload, boolean useCON){
		  _isInitialized = false;
		  initClient(resourceName);
		  handlePutRequest(payload, useCON);
	  }

	  // private methods 
	  //Get
	  private void handleGetRequest(boolean useCON){
		  _Logger.info("Sending GET...");
		  CoapResponse response = null;
		  if (useCON) {
			  _clientConnect.useCONs().useEarlyNegotiation(32).get();
		  }
		  response = _clientConnect.get();
		  if (response != null) {
			  _Logger.info(
					  "Response: " + response.isSuccess() + " - " + response.getOptions() + " - " + response.getCode());
		  } else {
			  _Logger.warning("No response received.");
		  }
	  }
	  
	  //Put
	  private void handlePutRequest(String payload, boolean useCON){
		  _Logger.info("Sending PUT...");
		  CoapResponse response = null;
		  if (useCON) {
			  _clientConnect.useCONs().useEarlyNegotiation(32).get();
		  }
		  response = _clientConnect.put(payload, MediaTypeRegistry.TEXT_PLAIN);
		  if (response != null) {
			  _Logger.info(
					  "Response: " + response.isSuccess() + " - " + response.getOptions() + " - " + response.getCode());
		  } else {
			  _Logger.warning("No response received.");
		  }
	  }
	  
	  //Post
	  private void handlePostRequest(String payload, boolean useCON){
		  _Logger.info("Sending POST...");
		  CoapResponse response = null;
		  if (useCON) {
			  _clientConnect.useCONs().useEarlyNegotiation(32).get();
		  }
		  response = _clientConnect.post(payload, MediaTypeRegistry.TEXT_PLAIN);
		  if (response != null) {
			  _Logger.info(
					  "Response: " + response.isSuccess() + " - " + response.getOptions() + " - " + response.getCode());
		  } else {
		  _Logger.warning("No response received.");
		  }
	  }
	  
	  //Delete
	  private void handleDeleteRequest(){
		  _Logger.info("Sending Delete...");
		  CoapResponse response = null;
		  response = _clientConnect.delete();
		  if (response != null) {
			  _Logger.info(
					  "Response: " + response.isSuccess() + " - " + response.getOptions() + " - " + response.getCode());
		  } else {
			  _Logger.warning("No response received.");
		  }
	  }
	  
	  private void initClient(){
		  initClient(null);
	  }
	  
	  //initClient
	  private void initClient(String resourceName){
		  if (_isInitialized) {
			  return;
		  }
		  if (_clientConnect != null) {
			  _clientConnect.shutdown();
			  _clientConnect = null;
		  }
		  try {
			  if (resourceName != null) {
				  _serverAddress += "/" + resourceName;
			  }
			  _clientConnect = new CoapClient(_serverAddress);
			  _Logger.info("Created client connection to server / resource: " + _serverAddress);
		  } catch (Exception e) {
			  _Logger.log(Level.SEVERE, "Failed to connect to broker: " + getCurrentUri(), e);
		  }
	  }
}
