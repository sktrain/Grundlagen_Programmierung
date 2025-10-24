package sk.train.model;

import java.io.Serializable;
import jakarta.persistence.*;


import java.math.BigDecimal;
import java.math.BigInteger;
import java.sql.Timestamp;



/**
 * The persistent class for the EMPLOYEES database table.
 * 
 */

@Entity
@Table(name="EMPLOYEES", schema="HR")
@NamedQuery(name="Employee.findAll", query="SELECT e FROM Employee e")
public class Employee implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
	@Column(name="EMPLOYEE_ID")
	private long employeeId;

	@Column(name="COMMISSION_PCT")
	private BigDecimal commissionPct;

	@Column(name="DEPARTMENT_ID")
	private BigDecimal departmentId;

	private String email;

	@Column(name="FIRST_NAME")
	private String firstName;

	@Column(name="HIRE_DATE")
	private Timestamp hireDate;

	@Column(name="JOB_ID")
	private String jobId;

	@Column(name="LAST_NAME")
	private String lastName;

	@Column(name="PHONE_NUMBER")
	private String phoneNumber;

	private BigDecimal salary;

	@Column(name="Manager_ID")
	private BigInteger managerId;

	public Employee() {
	}

	public long getEmployeeId() {
		return this.employeeId;
	}

	public void setEmployeeId(long employeeId) {
		this.employeeId = employeeId;
	}

	public BigDecimal getCommissionPct() {
		return this.commissionPct;
	}

	public void setCommissionPct(BigDecimal commissionPct) {
		this.commissionPct = commissionPct;
	}

	public BigDecimal getDepartmentId() {
		return this.departmentId;
	}

	public void setDepartmentId(BigDecimal departmentId) {
		this.departmentId = departmentId;
	}

	public String getEmail() {
		return this.email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getFirstName() {
		return this.firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public Timestamp getHireDate() {
		return this.hireDate;
	}

	public void setHireDate(Timestamp hireDate) {
		this.hireDate = hireDate;
	}

	public String getJobId() {
		return this.jobId;
	}

	public void setJobId(String jobId) {
		this.jobId = jobId;
	}

	public String getLastName() {
		return this.lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getPhoneNumber() {
		return this.phoneNumber;
	}

	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

	public BigDecimal getSalary() {
		return this.salary;
	}

	public void setSalary(BigDecimal salary) {
		this.salary = salary;
	}

	

	public BigInteger getManagerId() {
		return managerId;
	}

	public void setManagerId(BigInteger managerId) {
		this.managerId = managerId;
	}

	@Override
	public String toString() {
		return "Employee [employeeId=" + employeeId + ", commissionPct=" + commissionPct + ", departmentId="
				+ departmentId + ", email=" + email + ", firstName=" + firstName + ", hireDate=" + hireDate + ", jobId="
				+ jobId + ", lastName=" + lastName + ", phoneNumber=" + phoneNumber + ", salary=" + salary
				+ ", managerId=" + managerId + "]";
	}

}