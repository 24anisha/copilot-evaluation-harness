public class IntMultToLong
{
    private void overflow()
    {
        // A multiplication result that is converted to a larger type can be a sign that the result can overflow the type converted from.
        // References:
        // Rule doc: https://lgtm.com/rules/7900075/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Arithmetic/IntMultToLong.ql

        int i = 2000000000;
        long j = i * i;     // multiplication done using integer arithmetic causing overflow.
                            // to avoid overflow, use: i * (long) i
    }
}