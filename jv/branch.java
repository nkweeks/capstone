// branch.java

public class branch {
    public static final int NUM_OF_LOOPS = 1000000;

    public static void main(String[] args) {
        long start = System.nanoTime();
        for(int i=0; i<NUM_OF_LOOPS; i++){
            if (i == 1) {}
            if (i == 2) {}
            if (i == 3) {}
            if (i == 4) {}
            if (i == 5) {}
            if (i == 6) {}
            if (i == 7) {}
            if (i == 8) {}
            if (i == 9) {}
            if (i == 10) {}
        }
        long end = System.nanoTime();
        double elapsedTime = (double)(end - start) / 1000000000; // nanoseconds to seconds
        System.out.printf("%f\n", elapsedTime);
    }
}
