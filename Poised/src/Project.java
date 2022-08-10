// Project

import java.util.Date;

public class Project {

    // Initialize Attributes

    int proj_number;
    String name;
    String type;
    String address;
    int ERF;
    float total_fee;
    float paid_to_date;
    String date;
    Architect archi;
    Contractor contr;
    Customer cust;

    // Methods


        // Constructor
    public Project(int proj_number, String type, String name, String address, int ERF, float total_fee, float paid_to_date, String date, Architect archi, Contractor contr, Customer cust) {
        this.proj_number = proj_number;
        this.name = name;
        this.type = type;
        this.address = address;
        this.ERF = ERF;
        this.total_fee = total_fee;
        this.paid_to_date = paid_to_date;
        this.date = date;
        this.archi = archi;
        this.contr = contr;
        this.cust = cust;
    }


        // Setters

    public void setProj_number(int newProj_number){proj_number = newProj_number;}

    public void setName(String newName){name = newName;}

    public void setType(String newType){type = newType;}

    public void setAddress(String newAddress){address = newAddress;}

    public void setDate(String newDate){date = newDate;}

    public void setTotal_fee(float newTotal_fee){total_fee = newTotal_fee;}

    public void setPaid_to_date(float newPaid_to_date){paid_to_date = newPaid_to_date;}

    public void setERF(int newERF){ERF = newERF;}


        // Getters
    public int getProj_number(){return proj_number;}

    public String getName(){return name;}

    public String getType(){return type;}

    public String getAddress(){return address;}

    public int getERF(){return ERF;}

    public float getTotal_fee(){return total_fee;}

    public float getPaid_to_date(){return paid_to_date;}

    public String getDate(){return date;}

    public Architect getArchi() {return archi;}

    public Contractor getContr() {return contr;}

    public Customer getCust() {return cust;}


        // to string method
    public String toString(){
        String projectString = "Project Details:\n" + "\nProject Number:" + proj_number + "\nName:" + name + "\nType:" + type + "\nAddress:" + address +
                "\nERF:" + ERF + "\nTotal Fee:" + total_fee + "\nPaid to Date:" + paid_to_date + "\nDue Date:" + date + "\n" +
                "\nArchitect Details:\n" + archi + "\n" + "\nContractor Details:\n" +  contr + "\n" + "\nCustomer Details:\n" +  cust;

        return projectString;
    }
}


