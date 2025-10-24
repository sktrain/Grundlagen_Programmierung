package app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication
public class EmployeeServiceStarter {

	public static void main(String[] args) {
		ConfigurableApplicationContext ctx = SpringApplication.run(EmployeeServiceStarter.class);
//		String[] beans = ctx.getBeanDefinitionNames();
//		for (String s: beans) {
//			System.out.println(s);
//		}
	}


}