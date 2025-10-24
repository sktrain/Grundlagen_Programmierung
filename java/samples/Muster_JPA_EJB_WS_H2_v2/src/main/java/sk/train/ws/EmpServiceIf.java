package sk.train.ws;

import java.util.List;

import jakarta.jws.WebService;

import sk.train.model.Department;
import sk.train.model.Employee;

@WebService
public interface EmpServiceIf {

	void createEmp(Employee emp);

	Employee readEmp(long id);
	
	void updateEmp(Employee emp);

	void deleteEmp(long id);

	List<Employee> getAllEmps();	

	void createDep(Department dep);
	
	Department readDep(long id);	

	void deleteDep(long id);

	void updateDep(Department dep);
	
	List<Department> getAllDeps();

}