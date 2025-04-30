using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using System.Net.Http;
using Microsoft.Net.Http.Headers;
using Microsoft.AspNetCore.Hosting;
using Newtonsoft.Json;
using stocks.Models.Display;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace stocks.Controllers
{
    [Route("api/[controller]")]
    public class CompanyController : Controller
    {


        private readonly IHostingEnvironment _hostingEnvironment;

        public CompanyController(IHostingEnvironment hostingEnvironment)
        {
            _hostingEnvironment = hostingEnvironment;
        }



        // /api/company
        [HttpGet]
        public IEnumerable<Company> GetAll()
        {
            string webRootPath = _hostingEnvironment.WebRootPath;
            string contentRootPath = _hostingEnvironment.ContentRootPath;
            string JSON = System.IO.File.ReadAllText(contentRootPath + "/companyInfo.json");
            var cc = JsonConvert.DeserializeObject<CompanyList>(JSON);
            List<Company> ccc = cc.Companies;


            return ccc;
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