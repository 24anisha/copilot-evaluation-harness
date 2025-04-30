public class MultiplyRemainder
{
    private static void operatorPrecendenceConfusion()
    {
        // Using the remainder operator with the multiplication operator without adding parentheses to clarify
        // precedence may cause confusion.
        // References:
        // Rule doc: https://lgtm.com/rules/7860069/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Arithmetic/MultiplyRemainder.ql

        int d = 75000;          // durationInMillisecs
        int r = d % 60 * 1000;  // remainingDurationInMillisecs after 60 secs have elapsed
                                // Oops: it should have been parenthesized as d % (60 * 1000)
    }
}