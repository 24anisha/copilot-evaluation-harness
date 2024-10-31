package arrayproblems;

import java.util.Arrays;

/**
 * Created by gopalbala on 25/4/17.
 */
public class MissingNumberInDuplicateArrays {
    private static int findMissingNumberInDuplicateArrays(int[] inputArray1, int[] inputArray2) {
        //validations
        if (null == inputArray1 || null == inputArray2) {
            System.out.println("come on inputs are null?");
        }
        if (inputArray1.length == 0 && inputArray2.length == 0)
            System.out.println("what to compare?");
        if (inputArray1.length > inputArray2.length && inputArray1.length - inputArray2.length > 1) {
            System.out.println("cannot find.");
        }
        if (inputArray2.length > inputArray1.length && inputArray2.length - inputArray1.length > 1) {
            System.out.println("cannot find.");
        }
        if (inputArray1.length == inputArray2.length) {
            System.out.println("cannot find.");
        }
        if (inputArray1.length > inputArray2.length) {
            return getMeTheElement(inputArray1, inputArray2);
        } else {
            return getMeTheElement(inputArray2, inputArray1);
        }

    }

    private static int getMeTheElement(int[] inputArray1, int[] inputArray2) {
        int result;
        result = Arrays.stream(inputArray1).sum();
        result -= Arrays.stream(inputArray2).sum();

        return result;

    }

    public static void main(String[] args) {
        int[] inputArray1 = {9, 7, 8, 5, 4, 6, 2, 3, 1};
        int[] inputArray2 = {2, 3, 4, 9, 1, 8, 5, 6};
        System.out.println(findMissingNumberInDuplicateArrays(inputArray1, inputArray2));
    }
}