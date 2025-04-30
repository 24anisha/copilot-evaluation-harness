using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Hosting;
using stocks.Models.Display;
using Newtonsoft.Json;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace stocks.Controllers
{
    [Route("api/[controller]")]
    public class StockController : Controller
    {
        private readonly IHostingEnvironment _hostingEnvironment;

        public StockController(IHostingEnvironment hostingEnvironment)
        {
            _hostingEnvironment = hostingEnvironment;
        }



        // /api/stock
        [HttpGet]
        public IEnumerable<Stock> GetAll()
        {
            string webRootPath = _hostingEnvironment.WebRootPath;
            string contentRootPath = _hostingEnvironment.ContentRootPath;
            string JSON2 = System.IO.File.ReadAllText(contentRootPath + "/historicalStockData.json");
            var cc = JsonConvert.DeserializeObject<List<Stock>>(JSON2);
            


            return cc;
        }


     

    // GET api/values/5
    [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
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