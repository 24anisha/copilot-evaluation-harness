import java.io.File;

public class NullAlways
{
    // If a variable is dereferenced, and the variable has a null value on all possible execution paths
    // leading to the dereferencing, the dereferencing is guaranteed to result in a NullPointerException. 
    // A variable may also be implicitly dereferenced if its type is a boxed primitive type, and the variable
    // occurs in a context in which implicit unboxing occurs. Note that the conditional operator unboxes its
    // second and third operands when one of them is a primitive type and the other is the corresponding boxed type.
    // References:
    // Rule doc: https://lgtm.com/rules/3960073/
    // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Arithmetic/BadAbsOfRandom.ql

    public void createDir(File dir)
    {
        // in the below example, "!dir.exists()" is executed ONLY IF dir is null.
        if (dir != null || !dir.exists())
        {
            dir.mkdir();
        }
    }

    public void createDir2(File dir)
    {
        // this is the correct way.
        if (dir != null && !dir.exists())
        {
            dir.mkdir();
        }
    }
}