import java.io.File;

public class ContainerSizeCmpZero
{
    // Comparing the size of a container to zero with this operator will always return the same value.
    // References:
    // Rule doc: https://lgtm.com/rules/6780071/
    // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Likely%20Bugs/Likely%20Typos/ContainerSizeCmpZero.ql

    // A map, collection, string or array will always have size of at least zero.
    // Checking that an object of one of these types has size greater than or equal
    // to zero will always be true, while checking that it has size less than zero
    // will always be false.
    // For collections, maps and strings, if the intention was to check whether the
    // object was empty, is it preferred to use the isEmpty() method. For arrays, check
    // that the length field is greater than (not equal to) zero. 

    // The following example shows creation of a file guarded by comparison of a string
    // length with zero. This can result in the attempted creation of a file with an empty name.
    private static File MakeFile(String filename)
    {
        if (filename != null && filename.length() >= 0)
        {
            return new File(filename);
        }

        return new File("default.name");
    }

    /*
    This is a corrected version that will not create a file with an empty name.
    private static File MakeFile(String filename)
    {
        if (filename != null && !filename.isEmpty())
        {
            return new File(filename);
        }

        return new File("default.name");
    }
    */
}