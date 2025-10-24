package app.model;

public class Name {
	
	private String vorname;
	private String nachname;
	
	public Name(String vorname, String nachname) {
		super();
		this.vorname = vorname;
		this.nachname = nachname;
	}

	@Override
	public String toString() {
		return "Name [vorname=" + vorname + ", nachname=" + nachname + "]";
	}	

}
