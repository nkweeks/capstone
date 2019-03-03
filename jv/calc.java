// calc.java
public class calc {
    public static final int NUM_OF_LOOPS = 1000;

    public static void main(String[] args) {
        // Start timer
        long start = System.nanoTime();

        // Restart calculations 100 times
        for(int j = 0; j < 100; j++) {
            // Loop through 1000 sets of calculations
            for(int i = 1; i <= NUM_OF_LOOPS; i++){
                // Raise the counter to the power of itself
                long x = mypow(i, 3);
                // Multiply 
                x = x * 3;
                // Divide
                x = x / i;
                // Subtract
                x = x - i;
            }
        }

        // Calculate the time taken to run
        long end = System.nanoTime();
        double elapsedTime = (double)(end - start) / 1000000000; // nanoseconds to seconds

        // Print out the elapsed time
        System.out.printf("%f\n", elapsedTime);
    }


    /** returns the minimum of two numbers */
    public static long mypow(long x, int y) {
       if (y <= 1)
          return x;
       else
          return x * mypow(x, y-1);
    }
}
