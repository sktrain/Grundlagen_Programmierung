package app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.math.BigDecimal;
import java.util.Date;
import java.util.Optional;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import app.dao.EmpRepository;
import app.model.Employee;

@SpringBootTest
class EmployeeServiceTests {

	@Test
	void contextLoads() {
	}
	
	@Autowired
	private EmpRepository myserv;
	
	//private Employee emp;
	
	@Test
	void crudTest() {
		
		Employee emp = new Employee();
		emp.setEmployeeId(471);
		emp.setFirstName("Max");
		emp.setLastName("Mustermann");
		emp.setHireDate(new Date());
		emp.setJobId("IT_PROG");
		emp.setPhoneNumber("1111");
		emp.setSalary(new BigDecimal(5000l));
		emp.setEmail("Mustermann@murks.de" + 4711);		
		
		Employee erg = myserv.save(emp);
		System.err.println(erg == emp);

		Optional<Employee> emp1 = myserv.findById(471L);
		System.err.println(emp1);

		emp.setSalary(new BigDecimal(8000L));
		erg = myserv.save(emp);
		System.err.println(erg == emp);

		emp1 = myserv.findById(471L);
		if (emp1.isPresent()) {
			System.err.println(emp1.get().getSalary());
		}

		myserv.deleteById(471L);
		
		assertTrue(myserv.findById(471L).isEmpty());		
	}
	
	@Test
	void chefIndianerTest() {
		
		assertEquals(myserv.count(), myserv.getChefsNative().size()
				                            + myserv.getIndianerNative().size());	
	}
	
	//usw. ...
	
}
