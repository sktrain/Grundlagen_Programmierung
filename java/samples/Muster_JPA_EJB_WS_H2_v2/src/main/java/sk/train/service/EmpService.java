package sk.train.service;

import java.util.List;
import jakarta.ejb.Stateless;
import jakarta.ejb.TransactionAttribute;
import jakarta.ejb.TransactionAttributeType;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;

import sk.train.model.Department;
import sk.train.model.Employee;

/**
 * Session Bean implementation class EmpService
 */
@Stateless
@TransactionAttribute(TransactionAttributeType.SUPPORTS)
public class EmpService implements EmpServiceLocal {

	@PersistenceContext
	private EntityManager em;

	// default-Konstruktor
	public EmpService() {
		super();
	}

	@TransactionAttribute(TransactionAttributeType.REQUIRED)
	@Override
	public void createEmp(Employee emp) {		
		em.persist(emp);
	}

//	//Optional ist nicht Serializable!
//	public Optional<Employee> readEmp(long id){
//		return Optional.ofNullable(em.find(Employee.class, id));
//	}
	
	public Employee readEmp(long id) {
		return em.find(Employee.class, id);  //jetzt kommt "null" statt leeres "Optional" 
	}
	

	@TransactionAttribute(TransactionAttributeType.REQUIRED)
	@Override
	public void deleteEmp(long id){
		Employee emp = em.find(Employee.class, id);
		if (emp != null)
			em.remove(emp);
	}

	@TransactionAttribute(TransactionAttributeType.REQUIRED)
	@Override
	public void updateEmp(Employee emp){
		if (em.find(Employee.class, emp.getEmployeeId()) != null){
			em.merge(emp);
		}
	}
	
	@Override
	public List<Employee> getAllEmps(){
		//alle Angestellten: Named Query nutzen
		return em.createNamedQuery("Employee.findAll", Employee.class).getResultList();
	}
	
	/********** Ergaenzungen bzgl. Departments ***********/

	@Override
	public List<Department> getAllDeps(){
		return em.createNamedQuery("Department.findAll", Department.class).getResultList();
	}

	//analog  zu "readEmp": Optional ist nicht Serializable
	@Override
	public Department readDep(long id){
		return em.find(Department.class, id);  //jetzt kommt "null" statt leeres "Optional" 

	}

	@TransactionAttribute(TransactionAttributeType.REQUIRED)
	@Override
	public void createDep(Department dep){
		em.persist(dep);
	}

	@TransactionAttribute(TransactionAttributeType.REQUIRED)
	@Override
	public void deleteDep(long id){
		Department dep = em.find(Department.class, id);
		if (dep != null)
			em.remove(dep);
	}

	@TransactionAttribute(TransactionAttributeType.REQUIRED)
	@Override
	public void updateDep(Department  dep){
		if (em.find(Department.class, dep.getDepartmentId()) != null){
			em.merge(dep);
		}
	}
	
	
}
