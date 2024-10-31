using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Core2WebApi.Common;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Core2WebApi.Controllers
{
    [Route("api/[controller]")]
    public class ValuesController : ControllerBase
    {
        private readonly ILogger _logger;
        public ValuesController(ILogger<ValuesController> logger)
        {
            _logger = logger;
        }
        // GET api/values
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            _logger.LogInformation(Constants.LoggingEvents.ListItems, "Getting list items");
            var res = $"value{id}";
            res = null;
            if (res == null)
            {
                _logger.LogWarning(Constants.LoggingEvents.GetItemNotFound, "GetById({ID}) NOT FOUND", id);
                return NotFound();
            }
            return Content(res);
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}