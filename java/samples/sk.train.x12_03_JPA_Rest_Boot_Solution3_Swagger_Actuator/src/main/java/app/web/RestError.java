package app.web;

public class RestError {
	
	private String message;
	private int code;
	
	public RestError(String message, int code) {
		super();
		this.message = message;
		this.code = code;
	}

	public String getMessage() {
		return message;
	}

	public int getCode() {
		return code;
	}	

}
