using Core.Interfaces;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace Web.ActionFilters
{
    public class ModelHasCorrectIdAttribute : ActionFilterAttribute
    {
        public override void OnActionExecuting(ActionExecutingContext context)
        {
            var id = (int)context.ActionArguments["id"];
            var entity = context.ActionArguments["entity"] as IHasId;

            if (id != entity.Id)
            {
                context.Result = new BadRequestObjectResult("Entity Id does not match.");
            }
        }
    }
}