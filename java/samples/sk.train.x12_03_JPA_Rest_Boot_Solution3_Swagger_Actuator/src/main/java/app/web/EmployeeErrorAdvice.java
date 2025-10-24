package app.web;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
public class EmployeeErrorAdvice {
	
	@ResponseBody	//ist hier Pflicht
	@ExceptionHandler(EmployeeExistsException.class)
	@ResponseStatus(HttpStatus.CONFLICT)
	public RestError employeeExistsHandler(EmployeeExistsException ex) {
		return new RestError(ex.getMessage(), 1);		
	}
	
	@ResponseBody	//ist hier Pflicht
	@ExceptionHandler(EmployeeNotFoundException.class)
	@ResponseStatus(HttpStatus.NOT_FOUND)
	public RestError employeeNotFoundHandler(EmployeeNotFoundException ex) {
		return new RestError(ex.getMessage(), 2);		
	}

}
