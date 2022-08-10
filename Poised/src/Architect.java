// Architect

public class Architect {

    // Initialize Attributes

    String name;
    int phone_number;
    String email;
    String physical_address;

    // Methods


        // Constructor
    public Architect(String name, int phone_number, String email, String physical_address) {
        this.name = name;
        this.phone_number = phone_number;
        this.email = email;
        this.physical_address = physical_address;
    }


        // Setters
    public void setName(String newName){
        name = newName;
    }

    public void setPhone(int newPhone){
        phone_number = newPhone;
    }

    public void setEmail(String newEmail){
        email = newEmail;
    }

    public void setAddress(String newAddress){
        physical_address= newAddress;
    }


        // Getters
    public String getName(){
        return name;
    }

    public int getPhone(){
        return phone_number;
    }

    public String getEmail(){
        return email;
    }

    public String getAddress(){
        return physical_address;
    }


        // to string method
    public String toString(){
        String architectString ="\nArchitect Name:" + name + "\nArchitect phone number:" + phone_number +
                    "\nArchitect Email Address:" + email + "\nArchitect Address:" + physical_address;

    return architectString;
    }
}

