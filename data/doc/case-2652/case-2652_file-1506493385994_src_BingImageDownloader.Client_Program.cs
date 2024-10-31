using BingImageDownloader.Model;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Net.Http;
using System.Threading.Tasks;

namespace BingImageDownloader
{
    class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine("Downloading Bing Images...");
            var destinationDirectory = "BingImages";
            if(args.Length == 1)
            {
                destinationDirectory = args[0];
            }
            var destination = Directory.CreateDirectory(destinationDirectory);

            Task.WaitAll(Run(destination));
        }

        public static async Task Run(DirectoryInfo destination)
        {
            var client = new HttpClient() { BaseAddress = new Uri("https://www.bing.com") };

            var locale = "en-US";
            var getCurrentImages = $"/HPImageArchive.aspx?format=js&idx=9&n=8&mkt={locale}";

            var bingResultRaw = await client.GetStringAsync(getCurrentImages);
            var bingResult = JsonConvert.DeserializeObject<BingResult>(bingResultRaw);

            foreach (var image in bingResult.Images)
            {
                using (var result = await client.GetAsync(image.Url))
                {
                    if (result.IsSuccessStatusCode)
                    {
                        var filename = Path.GetFileName(image.Url);
                        Console.WriteLine($"Downloading {filename}...");
                        var destinationPath = Path.Combine(destination.FullName, filename);
                        await result.Content.LoadIntoBufferAsync();
                        using (FileStream fs = new FileStream(destinationPath, FileMode.Create))
                        {
                            await result.Content.CopyToAsync(fs);                            
                        }
                    }
                }

            }
        }
    }
}