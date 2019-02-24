// loop.java


public class loop {

    public static void main(String[] args) {
        int j;
        long start = System.nanoTime();
        for(int i=0; i<10000; i++){
            if (i/2 > 100) {
                j = i %2;
            } else {
                j = i/2;
            }
        }
        long end = System.nanoTime();
        double elapsedTime = (double)(end - start) / 1000000000; // nanoseconds to seconds
        System.out.printf("%d\n", (end - start));
        System.out.printf("%f\n", elapsedTime);
    }
}
