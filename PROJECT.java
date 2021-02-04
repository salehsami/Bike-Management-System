import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class PROJECT {

    // INITIALIZING ARRAY LIST TO STORE DATA IN THROUGHTOUT
    static ArrayList<String> bike = new ArrayList<String>();

    // >>> DECLARING AND INITIALIZING VARIBALES

    static int indexI; // used to store index of the ID in an arraylist
    static Boolean alreadyExists; // this value will be used to check if ID already exists
    static Boolean found = false; // used in search function if an ID is found or not
    static Scanner input = new Scanner(System.in); // scanner used in program
    static final String PATH = "myFile.txt"; // path to the file where data is stored
    static String notFound = "No record found. Enter record first."; // repetitive msg in methods when no record present
    static final String SPACES = "\t\t\t"; // for proper formatting

    static Boolean admin; // to check if user is admin or not
    static String adminUsername = "admin"; // admin credentials
    static String password = "123"; // same

    // METHODS
    public static void main(String[] args) {

        // LOAD DATA FROM PREVIOUS SESSION OR NOT
        System.out.println("Do you want to load stored data? Write Y to load otherwise N!");
        String value = input.nextLine();

        // LOAD ACCORDINGLY
        Boolean load = (value.equals("Y")) ? true : false;

        if (load) {
            readData();
        }

        // VERIFYING USER IF THEY ARE ADMIN OR NOT
        admin = verifyUser();

        // LOAD THE MENU
        Menu();

    }

    public static Boolean verifyUser() {

        while (true) {
            // ASK IF IT IS ADMIN OR USER
            try {
                System.out.println("Do you want to log in as admin or user. Enter 1 for admin, 2 for User: ");
                int userChoice = input.nextInt();
                input.nextLine();

                // IF USER CHOOSES 1, CREDENTIALS ARE ASKED OTHERWISE REGARDED AS NORMAL USER
                switch (userChoice) {

                    // IF CHOOSE 1
                    case 1:

                        // ASKING ADMIN USERNAME & PASSWORD TO VERIFY
                        System.out.println("Enter username: ");
                        String username = input.nextLine();
                        System.out.println("Enter password: ");
                        String pass = input.nextLine();

                        // CHECKING AGAINST STORED USERNAME AND PASSWORD
                        if (username.equals(adminUsername) && pass.equals(password)) {
                            System.out.println("Admin privileges have been granted");
                            admin = true;
                        }

                        else {
                            System.out.println("Wrong credentials.");
                            admin = false;
                            continue;
                        }
                        break;

                    // IF CHOOSE 2
                    case 2:
                        admin = false;
                        break;

                    default:
                        // If wrong input, ask again.
                        continue;
                }
                // BREAK LOOP IF USER VERIFIED
                break;

            } catch (Exception e) {
                // INCASE USER ENTER ANYTHING OTHER THAN REQUIRED VALUES
                input.nextLine();
                System.out.println("Enter correct input!");
            }

        }

        return admin;
    }

    public static void writeData() {

        // TRY WITH RESOURCES
        try {
            // FILEWRITER TO MAKE NEW FILE AND WRITE DATA TO IT
            FileWriter writer = new FileWriter(PATH);
            for (String i : bike) {
                writer.write(i + System.lineSeparator());
            }

            writer.close();

            // SUCCESS MESSAGE
            System.out.println("Data has been successfully written to file!");
        }

        catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void readData() {

        System.out.println("Reading data" + "\n");

        // LOADS FILE FROM PATH INTO SCANNER
        File file = new File(PATH);

        try {
            Scanner s = new Scanner(file);

            // CHECKING IF MORE DATA IN FILE
            while (s.hasNext()) {

                // ADD DATA TO ARRAYLIST
                bike.add(s.next());
            }

            // SAVE THE FILE
            s.close();
        }

        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static Boolean checkIfAlreadyExists(String id) {

        // LOOPING THROUGH DATA TO SEE IF ID IS PRESENT

        for (int i = 0; i < bike.size(); i += 5) {

            if (bike.get(i).equals(id))
                return true;

        }
        return false;
    }

    public static void add() {

        while (true)

        {
            // CHECK IF IT ALREADY EXISTS
            while (true) {

                // Taking id from user
                System.out.println("Enter bike owner id: "); // ID
                String id = input.nextLine();

                alreadyExists = checkIfAlreadyExists(id);

                if (alreadyExists) {
                    System.out.println("ID already exists. Enter a unique ID.");
                    continue;
                }

                bike.add(id);
                break;
            }

            // Taking inputs from user
            System.out.println("Enter bike owner name: "); // BIKE OWNER NAME
            String owner = input.nextLine();
            bike.add(owner);

            System.out.println("Enter the Engine CC: "); // ENGINE CC
            String engineCC = input.nextLine();
            bike.add(engineCC);

            System.out.println("Enter the Chassis Number of Bike: "); // CHASSIS NUMBER
            String chasisNo = input.nextLine();
            bike.add(chasisNo);

            System.out.println("Enter bike model: "); // BIKE MODEL
            String bikeModel = input.nextLine();
            bike.add(bikeModel);

            System.out.println("Enter 0 to add another record, 1 to go to Menu: ");
            int value = input.nextInt();
            input.nextLine();

            // End Condition for loop
            if (value != 0) {
                break;
            }

            // SAVES THE DATA TO FILE
            writeData();

        }
        Menu();
    }

    public static void view() {
        if (!bike.isEmpty()) {
            // PRINT MESSAGE SO THAT OUTPUT OF CODE LOOKS NICE
            System.out.println(">>>RECORD VIEWED\n");
            System.out.println("Id\t Owner Name \t Engine Power \t Chassis Number\t Bike Model ");

            // ITERATE AND LIST ALL RECORDS
            for (int i = 0; i < bike.size(); i = i + 5) {
                System.out.printf("%-9S", bike.get(i));

                System.out.printf("%-16S", bike.get(i + 1));

                System.out.printf("%-16S", bike.get(i + 2));

                System.out.printf("%-16S", bike.get(i + 3));

                System.out.printf("%-21S", bike.get(i + 4));

                // BLANK LINE INSERTED
                System.out.println("");

            }
            Menu();
        }

        else {
            System.out.println(notFound);
            Menu();
        }
    }

    public static void edit() {

        if (!bike.isEmpty()) {

            // ASK FOR ITEM TO EDIT
            System.out.print("Enter item id to edit: ");
            String search = input.nextLine();

            // CHECKING IF ITEM TO BE EDITED EXISTS
            for (int i = 0; i < bike.size(); i += 5) {

                if (bike.get(i).equals(search)) {

                    found = true;
                    System.out.println("Item found");

                    indexI = bike.indexOf(bike.get(i));
                    break;
                }
            }

            if (found) {

                while (true) {

                    // Taking id from user
                    System.out.print("Enter bike owner id: "); // ID
                    String id = input.nextLine();

                    // CHECK IF IT ALREADY EXISTS BEFORE EDITING
                    alreadyExists = checkIfAlreadyExists(id);

                    if (alreadyExists) {
                        System.out.println("ID already exists. Enter a unique ID.");
                        continue;
                    }

                    bike.set(indexI, id);
                    break;
                }

                // Taking inputs from user
                System.out.print("Enter bike owner name: "); // BIKE OWNER NAME
                String owner = input.nextLine();
                bike.set(indexI + 1, owner);

                System.out.print("Enter Engine CC Power: "); // ENGINE CC
                String engineCC = input.nextLine();
                bike.set(indexI + 2, engineCC);

                System.out.print("Enter the Chassis Number of Bike: "); // CHASSIS NUMBER
                String chasisNo = input.nextLine();
                bike.set(indexI + 3, chasisNo);

                System.out.print("Enter bike model: "); // BIKE MODEL
                String bikeModel = input.nextLine();
                bike.set(indexI + 4, bikeModel);

                writeData(); // SAVING TO FILE

                System.out.println("Record edited"); // SUCCESS MSG
                found = false;

                Menu();
            }

            else {
                System.out.println("Item not found"); // IF NO RECORD FOUND
                Menu();
            }
        }

        else {
            System.out.println(notFound);
            Menu();
        }
    }

    public static void search() {
        if (!bike.isEmpty()) {

            // ASK FOR ITEM TO SEARCH
            System.out.println("Enter item id to search: ");
            String search = input.nextLine();

            // CHECKING IF ITEM TO BE SEARCH EXISTS
            for (int i = 0; i < bike.size(); i += 5) {
                if (bike.get(i).equals(search)) {

                    found = true;
                    indexI = bike.indexOf(bike.get(i));
                    break;
                }
            }

            if (found) {
                System.out.println("Your search found!\n");
                // Displaying found record and formatting to align data in a table
                System.out.println("Id \t Owner Name \t Engine Power \t\t Chassis Number.\t Bike Model ");

                System.out.printf("%-9S", bike.get(indexI));

                System.out.printf("%-16S", bike.get(indexI + 1));

                System.out.printf("%-16S", bike.get(indexI + 2));

                System.out.printf("%-16S", bike.get(indexI + 3));

                System.out.printf("%-21S", bike.get(indexI + 4));

                // BLANK LINE INSERTED
                System.out.println("");

                found = false;
                Menu();
            }

            else {
                System.out.println("No record found.");
                Menu();
            }
        }

        else {
            System.out.println(notFound);
            Menu();
        }
    }

    public static void delete() {
        if (!bike.isEmpty()) {

            // ASK FOR ITEM TO SEARCH
            System.out.println("Enter item id to delete: ");
            String search = input.nextLine();

            // CHECKING IF ITEM TO BE SEARCH EXISTS
            for (int i = 0; i < bike.size(); i += 5) {
                if (bike.get(i).equals(search)) {

                    found = true;
                    indexI = bike.indexOf(bike.get(i));
                    break;
                }
            }

            if (found) {
                System.out.println("Item to delete found");
                // Displaying found record
                System.out.println("Id \t Owner Name \t Engine Power \t\t Chassis Number.\t Bike Model ");

                bike.remove(indexI + 4);
                bike.remove(indexI + 3);
                bike.remove(indexI + 2);
                bike.remove(indexI + 1);
                bike.remove(indexI);

                // BLANK LINE INSERTED
                System.out.println("Item Deleted");

                writeData();

                found = false;
                Menu();
            }

            else {
                System.out.println("Record not found");
                Menu();
            }
        }

        else {
            System.out.println(notFound);
            Menu();
        }
    }

    public static void Menu() {

        while (true) {

            try {

                System.out.println("Welcome to Bike Management System");

                System.out.println("\n-----------Menu------------");

                // FOR ADMIN

                if (admin) {
                    System.out.print("Enter \n" + "1. Add Record \n" + "2. View Record \n" + "3. Edit Record \n"
                            + "4. Search Record \n" + "5. Delete Record \n" + "0 to Exit\n>>> ");

                    int choice = input.nextInt();

                    // REMOVING ANYTHING LEFT IN INPUT STREAM AFTER PRESSING ENTER
                    input.nextLine();

                    if (choice == 1) {
                        add();
                    } else if (choice == 2) {
                        view();
                    } else if (choice == 3) {
                        edit();
                    } else if (choice == 4) {
                        search();
                    } else if (choice == 5) {
                        delete();
                    } else if (choice == 0) {
                        System.exit(0);
                        break;
                    }
                }

                // IF THE PERSON IS USER

                else {
                    System.out.print("Enter \n" + "1. View Record \n" + "2. Search Record \n" + "0 to Exit\n>>> ");

                    int choice = input.nextInt();
                    input.nextLine();

                    if (choice == 1) {
                        view();
                    } else if (choice == 2) {
                        search();
                    } else if (choice == 0) {
                        System.exit(0);
                        break;
                    }

                }

            }

            catch (Exception e) {
                input.nextLine();
                System.out.println("Incorrect input! Enter correct input.");
            }

        }

    }

}