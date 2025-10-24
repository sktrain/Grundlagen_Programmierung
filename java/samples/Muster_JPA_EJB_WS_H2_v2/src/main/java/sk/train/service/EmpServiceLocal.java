package sk.train.service;

import java.util.List;
import jakarta.ejb.Local;
import sk.train.model.Department;
import sk.train.model.Employee;

@Local
public interface EmpServiceLocal {
	
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