import java.util.Random;

public class BadAbsOfRandom
{
    private static void absOfRandom()
    {
        // Calling 'Math.abs' to find the absolute value of a randomly generated integer is not guaranteed
        // to return a non-negative integer.
        // References:
        // Rule doc: https://lgtm.com/rules/1800073/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Arithmetic/BadAbsOfRandom.ql

        int seed = 17;
        Random rng = new Random(seed);
        int val = Math.abs(rng.nextInt());   // gotcha! this is not guaranteed to return a non-negative integer - contradicts programmer intent.
    }
}