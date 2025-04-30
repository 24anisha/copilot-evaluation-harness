public class UselessParameter
{
    private boolean compare(int x, int y, int z)
    {
        // The param 'z' is not used and is useless
        // While this is a contrived example, it is possible to end up with useless params in the course of refactoring.
        // References:
        // Rule doc: https://lgtm.com/rules/1506317566749/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/DeadCode/UselessParameter.ql

        if (x < y)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}