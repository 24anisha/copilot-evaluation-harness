using System;

namespace TestProject
{
    // ReSharper disable once UnusedMember.Global
    internal sealed class LocalVariables
    {
        // ReSharper disable once UnusedMember.Global
        public void LocalVariableShouldBeConstant()
        {
            // ReSharper disable once ConvertToConstant.Local
            // ReSharper disable once RedundantAssignment
            // ReSharper disable once InlineOutVariableDeclaration
            ulong localVariable = 7;
            const string c_logAsString = "7";
            // ReSharper disable once AssignmentIsFullyDiscarded
            _ = ulong.TryParse(c_logAsString, out localVariable);
            Console.WriteLine(localVariable);
            // test
        }
    }
}