// loop.java


public class loop {
    public static final int NUM_OF_LOOPS = 1000;

    public static void main(String[] args) {
        long start = System.nanoTime();
        for(int i=0; i<NUM_OF_LOOPS; i++){
            for (int j=0; j<NUM_OF_LOOPS; j++) {
                for (int k=0; k<NUM_OF_LOOPS; k++) {}
            }
        }
        long end = System.nanoTime();
        double elapsedTime = (double)(end - start) / 1000000000; // nanoseconds to seconds
        System.out.printf("%f\n", elapsedTime);
    }
}
