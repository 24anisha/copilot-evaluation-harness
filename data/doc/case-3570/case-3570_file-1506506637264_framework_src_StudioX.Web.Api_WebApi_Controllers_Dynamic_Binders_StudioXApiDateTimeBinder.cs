﻿using System;
using System.Globalization;
using System.Web.Http.Controllers;
using System.Web.Http.ModelBinding;
using StudioX.Timing;

namespace StudioX.WebApi.Controllers.Dynamic.Binders
{
    /// <summary>
    /// Binds datetime values from api requests to model
    /// </summary>
    public class StudioXApiDateTimeBinder : IModelBinder
    {
        public bool BindModel(HttpActionContext actionContext, ModelBindingContext bindingContext)
        {
            var value = bindingContext.ValueProvider.GetValue(bindingContext.ModelName);
            DateTime? date = null;
            try
            {
                date = value?.ConvertTo(typeof(DateTime?), CultureInfo.CurrentCulture) as DateTime?;
            }
            catch { }

            if (date.HasValue)
            {
                bindingContext.Model = Clock.Normalize(date.Value);
            }

            return true;
        }
    }
}