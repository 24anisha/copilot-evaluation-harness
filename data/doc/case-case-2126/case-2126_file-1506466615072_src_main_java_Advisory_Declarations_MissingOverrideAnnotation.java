class Parent
{
    public void m1()
    {
        System.out.println("From parent m1()");
    }
}

class Child extends Parent
{
    // @Override
    public void m1()
    {
        // The @Override annotation serves as a reminder that the intent of the method is to override a parent method.
        // A method that overrides a method in a superclass but does not have an 'Override' annotation cannot take
        // advantage of compiler checks, and makes code less readable.
        // References:
        // Rule doc: https://lgtm.com/rules/2046390549/
        // QL query: https://github.com/lgtmhq/lgtm-queries/blob/master/java/Advisory/Declarations/MissingOverrideAnnotation.ql

        System.out.println("From child m1()");
    }
}