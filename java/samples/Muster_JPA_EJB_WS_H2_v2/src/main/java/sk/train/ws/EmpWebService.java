package sk.train.ws;

import java.util.List;

import jakarta.ejb.EJB;
import jakarta.jws.WebService;

import sk.train.model.Department;
import sk.train.model.Employee;
import sk.train.service.EmpServiceLocal;

@WebService(endpointInterface = "sk.train.ws.EmpServiceIf")
public class EmpWebService implements EmpServiceIf {
	
	@EJB
	private EmpServiceLocal myejb;

	@Override
	public void createEmp(Employee emp) {
		myejb.createEmp(emp);
		
	}

	@Override
	public Employee readEmp(long id) {
		return myejb.readEmp(id);
	}

	@Override
	public void updateEmp(Employee emp) {
		myejb.updateEmp(emp);
		
	}

	@Override
	public void deleteEmp(long id) {
		myejb.deleteEmp(id);
		
	}

	@Override
	public List<Employee> getAllEmps() {
		return myejb.getAllEmps();
	}

	@Override
	public void createDep(Department dep) {
		myejb.createDep(dep);
		
	}

	@Override
	public Department readDep(long id) {
		return myejb.readDep(id);
	}

	@Override
	public void deleteDep(long id) {
		myejb.deleteDep(id);
		
	}

	@Override
	public void updateDep(Department dep) {
		myejb.updateDep(dep);
		
	}

	@Override
	public List<Department> getAllDeps() {
		return myejb.getAllDeps();
	} 

	


}
