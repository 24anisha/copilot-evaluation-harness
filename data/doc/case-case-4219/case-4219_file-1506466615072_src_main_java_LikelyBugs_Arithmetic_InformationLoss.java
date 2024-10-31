public class InformationLoss
{
    private static int narrowingConversion()
    {
        // Compound assignment statements (for example 'intvar += longvar') that implicitly cast a value of
        // a wider type to a narrower type may result in information loss and numeric errors such as overflows.
        // References:
        // Rule doc: https://lgtm.com/rules/1780084/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Arithmetic/InformationLoss.ql

        int x = 100;
        long y = 200;
        return x *= y;
    }
}