public class WhitespaceContradicsPrecedence
{
    private void contracdictsOpPrecedence(int capacity)
    {
        // Nested expressions where the formatting contradicts the grouping enforced by operator precedence
        // are difficult to read and may even indicate a bug.
        // References:
        // Rule doc: https://lgtm.com/rules/11000068/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Arithmetic/WhitespaceContradictsPrecedence.ql

        // below, the spacing around + and >> suggests the grouping
        // capacity + (capacity>>1), i.e., the allocated array should
        // be 50% larger than the given capacity. 
        // However, + has higher precedence than >>, so this code allocates
        // an array of size (capacity + capacity) >> 1, which is the same
        // as capacity. 
        int[] buf = new int[capacity + capacity>>1];
    }
}