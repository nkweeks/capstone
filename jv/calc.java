// calc.java


public class calc {
    public static final int NUM_OF_LOOPS = 100000;

    public static void main(String[] args) {
        long start = System.nanoTime();
        for(int i=0; i<NUM_OF_LOOPS; i++){
            // Save the counter to a variable that can be used
            int x = i;

            // Raise the counter to the power of itself
            x = pow(i, i);

        }

        // Calculate the time taken to run
        long end = System.nanoTime();
        double elapsedTime = (double)(end - start) / 1000000000; // nanoseconds to seconds

        // Print out the elapsed time
        System.out.printf("%f\n", elapsedTime);
    }
}
