using System;
using System.Linq;
using System.Linq.Expressions;
using System.Reflection;

namespace Carupano.Configuration
{
    using Model;
    public class AggregateModelBuilder<T> : IAggregateModelBuilder
    {
        AggregateModel _model;
        public AggregateModelBuilder()
        {
            _model = new AggregateModel(typeof(T));   

        }
        
        public AggregateModelBuilder<T> Executes<TCommand>(Expression<Func<TCommand,string>> correlationAccessor)
        {
            var id = new Func<object, string>((obj) => {
                var expr = correlationAccessor.Body as MemberExpression;
                var prop = expr.Member as PropertyInfo;
                return (string)prop.GetValue(obj);
            });
            _model.AddCommandHandler(new CommandHandlerModel(FindMethodByParameter(typeof(TCommand)), new CommandModel(typeof(TCommand), new AggregateCorrelation(id))));
            return this;
        }
        public AggregateModelBuilder<T> CreatedBy<TCommand>()
        {
            _model.SetFactoryHandler(new CommandHandlerModel(FindMethodByParameter(typeof(TCommand))));
            return this;
        }

        public AggregateModelBuilder<T> WithId(Expression<Func<T,string>> idAccessor)
        {
            _model.SetIdentifier(new AggregateIdentifier((obj)=> {
                var expr = idAccessor.Body as MemberExpression;
                var prop = expr.Member as PropertyInfo;
                return (string)prop.GetValue(obj);
            }));
            return this;
        }
        private MethodInfo FindMethodByParameter(Type param)
        {
            return _model.Type.GetMethods().Single(c => c.GetParameters().Count() == 1 && c.GetParameters().First().ParameterType == param);
        }

        public AggregateModel Build()
        {
            return _model;
        }

    }
    
}