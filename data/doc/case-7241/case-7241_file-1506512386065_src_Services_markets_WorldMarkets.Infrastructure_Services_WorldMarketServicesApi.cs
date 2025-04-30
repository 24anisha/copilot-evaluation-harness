using Services.markets.WorldMarkets.Domain;
using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using WorldMarkets.Domain.Interfaces;

namespace Services.markets.WorldMarkets.Infrastructure
{
    public class WorldMarketServicesApi : IWorldMarketServicesApi
    {
        private HttpClient _httpClient;

        public async Task<string> GetPageWorldMarkets()
        {
            try
            {
                _httpClient = new HttpClient();
                var response = await _httpClient.GetAsync("http://exame.advfn.com/");
                if (response.StatusCode == HttpStatusCode.OK)
                {
                    return response.Content.ReadAsStringAsync().Result;
                }
            }
            catch (Exception ex)
            {
                return "";
            }
            return "";
        }
    }
}