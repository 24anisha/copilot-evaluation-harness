using AspectCore.DynamicProxy;
using System;
using System.Threading.Tasks;

namespace aspnetcorehystrix
{
    [AttributeUsage(AttributeTargets.Method)]
    public class HystrixCommandAttribute : AbstractInterceptorAttribute
    {
        public HystrixCommandAttribute(string fallBackMethod)
        {
            this.FallBackMethod = fallBackMethod;
        }

        public string FallBackMethod { get; set; }

        public override async Task Invoke(AspectContext context, AspectDelegate next)
        {
            try
            {
                await next(context);//执行被拦截的方法
            }
            catch (Exception ex)
            {
                //context.ServiceMethod被拦截的方法。context.ServiceMethod.DeclaringType被拦截方法所在的类
                //context.Implementation实际执行的对象p
                //context.Parameters方法参数值
                //如果执行失败，则执行FallBackMethod
                var fallBackMethod = context.ServiceMethod.DeclaringType.GetMethod(this.FallBackMethod);
                Object fallBackResult = fallBackMethod.Invoke(context.Implementation, context.Parameters);
                context.ReturnValue = fallBackResult;
                await Task.FromResult(0);
            }
        }
    }
}