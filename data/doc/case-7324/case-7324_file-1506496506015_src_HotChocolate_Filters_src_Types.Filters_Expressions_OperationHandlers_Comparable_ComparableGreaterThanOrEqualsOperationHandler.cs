using System;
using System.Diagnostics.CodeAnalysis;
using System.Linq.Expressions;

namespace HotChocolate.Types.Filters.Expressions
{
    [Obsolete("Use HotChocolate.Data.")]
    public sealed class ComparableGreaterThanOrEqualsOperationHandler
        : ComparableOperationHandlerBase
    {
        protected override bool TryCreateExpression(
            FilterOperation operation,
            Expression property,
            Func<object> parseValue,
            [NotNullWhen(true)] out Expression? expression)
        {
            switch (operation.Kind)
            {
                case FilterOperationKind.GreaterThanOrEquals:
                    expression = FilterExpressionBuilder.GreaterThanOrEqual(
                        property, parseValue());
                    return true;

                case FilterOperationKind.NotGreaterThanOrEquals:
                    expression = FilterExpressionBuilder.Not(
                        FilterExpressionBuilder.GreaterThanOrEqual(
                            property, parseValue()));
                    return true;

                default:
                    expression = null;
                    return false;
            }
        }
    }
}