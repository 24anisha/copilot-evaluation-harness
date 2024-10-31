using Newtonsoft.Json;
using SampleProject.Contracts.Services;
using SampleProject.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace SampleProject.Services
{
    public class GitHubService<T> : IGitHubService<T> where T : class
    {


        public async Task<T> GetUser(string username)
        {
            username = username ?? "chilas";

            HttpClient client = new HttpClient()
            {
                BaseAddress = new Uri("http://api.github.com/")
            };
            client.DefaultRequestHeaders.TryAddWithoutValidation("User-Agent", "http://developer.github.com/v3/#user-agent-required");
            T user = null;
            var response = await client.GetAsync($"users/{username}");
            user = JsonConvert.DeserializeObject<T>(await response.Content.ReadAsStringAsync());

            return user;
        }
    }
}