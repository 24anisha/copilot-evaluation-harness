using System;
using System.Diagnostics.CodeAnalysis;
using System.Linq.Expressions;

namespace HotChocolate.Types.Filters.Expressions
{
    [Obsolete("Use HotChocolate.Data.")]
    public sealed class StringEndsWithOperationHandler
        : StringOperationHandlerBase
    {
        protected override bool TryCreateExpression(
            FilterOperation operation,
            Expression property,
            object parsedValue,
            [NotNullWhen(true)] out Expression? expression)
        {
            switch (operation.Kind)
            {
                case FilterOperationKind.EndsWith:
                    expression = FilterExpressionBuilder.EndsWith(
                        property, parsedValue);
                    return true;

                case FilterOperationKind.NotEndsWith:
                    expression = FilterExpressionBuilder.Not(
                        FilterExpressionBuilder.EndsWith(
                            property, parsedValue));
                    return true;

                default:
                    expression = null;
                    return false;
            }
        }
    }
}