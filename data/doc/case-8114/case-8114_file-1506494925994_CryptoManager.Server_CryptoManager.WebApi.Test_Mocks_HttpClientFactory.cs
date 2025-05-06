using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace CryptoManager.WebApi.Test.Mocks
{
    public class HttpClientFactory
    {
        private HttpClient _client;
        public HttpClientFactory(HttpClient client)
        {
            _client = client;
            _client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
            _client.BaseAddress = new Uri(Constants.AplicationTestBaseUri);
        }

        public void AddHeader(string name, string value)
        {
            _client.DefaultRequestHeaders.Add(name, value);
        }
        
        public async Task<HttpResponseMessage> GetAsync(string path)
        {
            return await _client.GetAsync(path);
        }

        public async Task<HttpResponseMessage> PostAsync(string path, object viewModel = null)
        {
            var json = JsonConvert.SerializeObject(viewModel);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            return await _client.PostAsync(path, content);
        }

        public async Task<HttpResponseMessage> PutAsync(string path, object viewModel)
        {
            var json = JsonConvert.SerializeObject(viewModel);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            return await _client.PutAsync(path, content);
        }

        public async Task<HttpResponseMessage> DeleteAsync(string path)
        {
            return await _client.DeleteAsync(path);
        }

        public async Task AddAuthorizationAsync()
        {
            if (!_client.DefaultRequestHeaders.Contains("Authorization"))
            {
                var token = await MockAuthorization.GetValidTokenAsync();
                AddHeader("Authorization", $"Bearer {token}");
            }
        }
    }
}