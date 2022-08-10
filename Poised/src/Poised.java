// Capstone I - Poised

// Imports

import java.util.Scanner;
import java.lang.*;

// Main Code
public class Poised {

    public static void main(String[] args) {

        // Welcome message
        System.out.println("Welcome to Poised Project Manager\n");

        // User input (initializing scanner)
        Scanner user_choice = new Scanner(System.in);

        // Requesting local variables from user

        // Architect details
        System.out.println("Please enter Architects name: ");
        String arch_name = user_choice.nextLine();  // local variable

        System.out.println("Please enter Architects number: ");
        int arch_number = user_choice.nextInt();  // local variable

        System.out.println("Please enter Architects email: ");
        user_choice.nextLine();  // Consuming the leftover new line
        String arch_email = user_choice.nextLine();  // local variable

        System.out.println("Please enter Architects address: ");
        String arch_address = user_choice.nextLine();  // local variable

        // Contractor details
        System.out.println("Please enter Contractors name: ");
        String cont_name = user_choice.nextLine();  // local variable

        System.out.println("Please enter Contractors number: ");
        int cont_number = user_choice.nextInt();  // local variable

        System.out.println("Please enter Contractors email: ");
        user_choice.nextLine();  // Consuming the leftover new line
        String cont_email = user_choice.nextLine();  // local variable

        System.out.println("Please enter Contractors address: ");
        String cont_address = user_choice.nextLine();  // local variable

        // Customer details
        System.out.println("Please enter Customers name: ");
        String cust_name = user_choice.nextLine();  // local variable

        System.out.println("Please enter Customers number: ");
        int cust_number = user_choice.nextInt();  // local variable

        System.out.println("Please enter Customers email: ");
        user_choice.nextLine();  // Consuming the leftover new line
        String cust_email = user_choice.nextLine();  // local variable

        System.out.println("Please enter Customers address: ");
        String cust_address = user_choice.nextLine();  // local variable

        // Project details
        System.out.println("Please enter project number: ");
        int proj_number = user_choice.nextInt();  // local variable

        System.out.println("Please enter building type: ");
        user_choice.nextLine();  // Consuming the leftover new line
        String type = user_choice.nextLine();  // local variable

        System.out.println("Please enter project name: ");
        String name = user_choice.nextLine();  // local variable

        // if no name is given
        if (name.equals("")){
            name = cust_name + type;
        }

        System.out.println("Please enter physical address: ");
        String address = user_choice.nextLine();  // local variable

        System.out.println("Please enter ERF number: ");
        int ERF = user_choice.nextInt();  // local variable

        System.out.println("Please enter total fee charge: ");
        float total_fee = user_choice.nextFloat();  // local variable

        System.out.println("Please enter amount paid to date: ");
        float paid_to_date = user_choice.nextFloat();  // local variable

        System.out.println("Please enter the deadline date (dd/mm/yyy): ");
        user_choice.nextLine();  // Consuming the leftover new line
        String date = user_choice.nextLine();  // local variable

        System.out.println("\nThank you for entering the details\n");

        // Constructing the instances
        Architect architect = new Architect(arch_name, arch_number, arch_email, arch_address);

        Contractor contractor = new Contractor(cont_name, cont_number, cont_email, cont_address);

        Customer customer = new Customer(cust_name, cust_number, cust_email, cust_address);

        Project project = new Project(proj_number, type, name, address, ERF, total_fee, paid_to_date, date, architect, contractor, customer);

        // Printing to string
        System.out.println("\n The project details are as follows:\n");

        System.out.println(project);

        // While loop for making edits
        while (true) {

            // User choice regarding what they want to change
            System.out.println("\nDo you want to edit:" +
                    "\n Due Date (d)" +
                    "\n Total fee paid (tfp)" +
                    "\n Contractors details (c)" +
                    "\n Finalize project (f)" +
                    "\n OR Exit(x)");

            String edit_choice = user_choice.nextLine().toLowerCase();

            if (edit_choice.equals("d")) {

                // Requesting the new information
                System.out.println("Enter the new date (dd/mm/yyyy):");
                String newDate = user_choice.nextLine();

                // Using the setters to change details
                project.setDate(newDate);

                // Printing to string
                System.out.println("\n The new project details are as follows:\n");

                System.out.println(project);

            } else if (edit_choice.equals("tfp")) {

                // Requesting the new information
                System.out.println("Enter the new amount:");
                float newAmount = user_choice.nextFloat();

                // Using the setters to change details
                project.setPaid_to_date(newAmount);

                // Printing to string
                System.out.println("\n The new project details are as follows:\n");

                System.out.println(project);

            } else if (edit_choice.equals("c")) {

                // Requesting the new information
                System.out.println("Please enter Contractors name: ");
                String newCont_name = user_choice.nextLine();  // local variable

                System.out.println("Please enter Contractors number: ");
                int newCont_number = user_choice.nextInt();  // local variable

                System.out.println("Please enter Contractors email: ");
                user_choice.nextLine();  // Consuming the leftover new line
                String newCont_email = user_choice.nextLine();  // local variable

                System.out.println("Please enter Contractors address: ");
                String newCont_address = user_choice.nextLine();  // local variable

                // Using the setters to change details
                project.contr.setName(newCont_name);
                project.contr.setPhone(newCont_number);
                project.contr.setEmail(newCont_email);
                project.contr.setAddress(newCont_address);

                // Printing to string
                System.out.println("\n The new project details are as follows:\n");

                System.out.println(project);

            }else if (edit_choice.equals("f")){

                // Finalisation message
                System.out.println("You have marked the project as complete, find below the invoice details");

                // Invoicing code
                if(total_fee > paid_to_date){

                    Double owing = Double.valueOf(total_fee - paid_to_date);

                    System.out.println("\n Invoice for" + cust_name +
                            "\nPhone number:" + cust_number +
                            "\nEmail Address:" + cust_email +
                            "\n Amount owing:" + owing );
                }

                else{
                    System.out.println("No fee outstanding");
                }

            }else if (edit_choice.equals("x")) {

                // Goodbye message
                System.out.println("Goodbye!");

                // Exit command
                System.exit(0);
                break;

            } else {

                // Error message
                System.out.println("\nYou have entered an incorrect input, please try again\n");
            }
        }
    }
}



