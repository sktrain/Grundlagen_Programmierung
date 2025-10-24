package app.dao;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import app.model.Employee;
import app.model.Name;

public interface EmpRepository  extends JpaRepository<Employee, Long>{
	
	public abstract List<Employee> findBySalary(BigDecimal salary);
	
	public abstract List<Employee> findBySalaryLessThan(BigDecimal salary);
	
	public abstract Optional<Employee> findByEmployeeIdAndSalary(long id, BigDecimal salary);
	
	@Query("select sum(e.salary)from Employee e")
	public abstract BigDecimal getSumSalary();
	
	@Query(value="select * from hr.employees where employee_id in" +
			"(select distinct manager_id from hr.employees)",nativeQuery=true)
	public abstract List<Employee> getChefsNative();
	
	@Query(value="select * from hr.employees where employee_id not in" +
			"(select distinct manager_id from hr.employees where manager_id is not null)"
			,nativeQuery=true)
	public abstract List<Employee> getIndianerNative();
	
	@Query("SELECT NEW app.model.Name(e.firstName, e.lastName) FROM Employee e")
	public abstract List<Name> getNames();	
	
	
}
