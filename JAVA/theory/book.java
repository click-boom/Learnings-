package theory;
public class book {
    // public static void main(String[] args) {
    // System.out.print("Hello java");
    // System.out.println();
    // }

    // public static void main(String[] args){
    // int example1= 200;
    // int example2= 100;
    // int sum_of_examples=example1+example2;
    // System.out.println("Sum is:"+ sum_of_examples);
    // }

    // public static void main(String[] args){
    // for (int i = 0; i <=5; i++) {
    // for (int j = 0; j <=i; j++) {
    // System.out.print("*");
    // }
    // System.out.println();
    // }
    // }

    // public static void main(String[] args) {
    // int initialized = 10;
    // int After_increment = initialized++;
    // System.out.println("Y after post-increment:" + After_increment);
    // System.out.println("X after post-increment:" + initialized);
    // /*
    // * Post means dont increment at the point it was declared, but increment for
    // the steps from now on.
    // * Something like while loop in C.
    // */
    //
    // After_increment = ++initialized;
    // System.out.println("Y after pre-increment:" + After_increment);
    // System.out.println("X after pre-increment:" + initialized);
    // }
    // /*
    // * Pre means increment at the point it was declared.
    // * Something like while loop in C.
    // */

    // public static void main(String[] args){
    // if (true) System.out.println("Its true");
    // System.out.println((10>9));
    // }
    //
    // public static void main(String[] args){
    // long rep_long=12L;
    // float rep_float=12F;
    // System.out.println("represent float and long
    // respectively:"+rep_float+rep_long);
    //
    // char rep_char_using_int=90;
    // System.out.println("represent char using int:"+rep_char_using_int);
    //
    // int sep_underscore=10_00_000;
    // System.out.println("separating integer values with
    // underscore:"+sep_underscore);
    //
    // char single_char='a';
    // System.out.println(single_char);
    // }

    /* Scope */
    // public static void main(String[] args){
    // int rep_hexa = 0xFF;
    // int rep_octal = 011;
    // int rep_binary = 0b100;
    //
    // System.out.println("represent hexadecimal ,octal and binary respectively:" +
    // rep_hexa + " " + rep_octal + " "+ rep_binary);
    // }

    // public static void main(String[] args) {
    // int x;
    // x = 10;
    // if (x == 10) {
    // int y = 20;
    // System.out.println("x and y" + x + "" + y);
    // x = y * 2;
    // }
    // // y = 100; Error
    // x = 100; // No error
    // }

    // public static void main(String[] args) throws java.io.IOException {
    // System.out.print("Enter:");
    // char ch= (char) System.in.read();
    // System.out.println("Entered:"+ch);
    // }

    // Traditional Switch
    // public static void main(String[] args) throws java.io.IOException {
    // System.out.println("enter:");
    // char ch = (char) System.in.read();
    // switch (ch) {
    // case 'A': point here is that a well-designed class group
    // case 'a': {
    // System.out.println("This is a");
    // break;
    // }
    // default:
    // System.out.println("Its nothing");
    // }
    // }

    // if statement
    // public static void main(String[] args) throws java.io.IOException {
    // System.out.println("enter:");
    // char ch = (char) System.in.read();

    // if (ch == 'A' || ch == 'a')
    // System.out.println("Its an " + ch);
    // else if (ch == 'B' || ch == 'b')
    // System.out.println("Its a " + ch);
    // else
    // System.out.println("Neither a nor b");
    // }

    /**
     * Types of for loop:
     * Loop without initialization --> done inside main method
     * Loop without increment --> done inside the block
     * Loop without condition --> infinite loop
     * Loop with multi values initialized and incremented at once, but contains only
     * one condition
     */

    // public static void main(String[] args) throws java.io.IOException {
    // System.out.println("press S to stop:");
    // for (int i = 0; (char) System.in.read() != 'S'; i++) {
    // System.out.println("Pass#" + i);
    // }
    // }
    /*
     * This program is important because it helps understand the SYstem.in.read
     * morebetter.
     * THe thing is that system.in.read stores all the input as integer in the
     * inputbuffer.
     * It takes input in the form of line buffer, i.e. all the characters are stored
     * until a newline character, i.e. ENTER is pressed.
     * Thing to note is that the enter pressed at end is also cosidered as a
     * character by the method.
     * 
     * So. to ignore the newline character at the end, run the read method again and dont implement it anywhere.
     * The concept behind it is that, if the method is used after using the required
     * values in buffer, the items re-read after 2nd call is a separate thing from the 1st one and wont interfere the first one.
     */
}
