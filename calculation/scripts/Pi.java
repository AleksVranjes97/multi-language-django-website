// Java program to demonstrate calculation on Django server;
// Calculate and display the first 300 (approximate) digits of Pi.
// (Reference: http://www.codecodex.com/wiki/Calculate_digits_of_pi#Implementations)

class Pi {

    // Constant variable to be used for scale
    private static int SCALE = 10000;  

    // Function to find and store digits of pi
	public static String digits_of_pi(int digits) {

        // Initialize string buffer and array
		StringBuffer pi_string = new StringBuffer();
		int array[] = new int[digits + 1];
		int carry = 0;

        // Initialize all array values to 2000
		for (int i = 0; i <= digits; i++)
			array[i] = 2000;

        // Calculating digits
		for (int i = digits; i > 0; i -= 14) {
			int sum = 0;
			for (int j = i; j > 0; j--) {
				sum = sum * j + SCALE * array[j];
				array[j] = sum % (j * 2 -1);
				sum /= j * 2 - 1;
			}

            // Appending digit to string
			pi_string.append(String.format("%04d", carry + sum / SCALE));
			carry = sum % SCALE;
		}

        // Return pi string
		return pi_string.toString();
	}

    // Pass in number of digits to print and format string to
    // show a proper decimal
    public static void main(String args[]) {
    	int digits = 1020;
        String pi_string = Pi.digits_of_pi(digits);
        String three = pi_string.substring(0, 1);
        String decimal = pi_string.substring(1);
    	System.out.println(three + "." + decimal);
    }
}