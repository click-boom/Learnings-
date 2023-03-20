public class later{
    public static void main(String[] args) {
        System.out.print("Loading: [          ]"); // print a loading bar with 10 spaces
        for (int i = 0; i < 10; i++) {
            System.out.print("\rLoading: ["); // move cursor back to beginning of line and start overwriting
            for (int j = 0; j <= i; j++) {
                System.out.print("#"); // print a hash symbol for each iteration
            }
            for (int j = i+1; j < 10; j++) {
                System.out.print(" "); // print spaces to fill up the rest of the loading bar
            }
            System.out.print("]"); // close the loading bar
            try {
                Thread.sleep(1000); // simulate a long-running process
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("\nDone!"); // print a newline character and "Done!" message
    }
}