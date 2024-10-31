using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using CodingMilitia.Grpc.Client;
using CodingMilitia.Grpc.HelloWorld.Client;
using CodingMilitia.Grpc.HelloWorld.Service;
using CodingMilitia.Grpc.Serializers;
using CodingMilitia.Grpc.Server;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace CodingMilitia.Grpc.HelloWorld
{
    class Program
    {
        public static async Task Main(string[] args)
        {
            var serverHostBuilder = new HostBuilder()
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddGrpcServer<ISampleService, SampleService>(new GrpcServerOptions { Url = "127.0.0.1", Port = 5000 });
                });

            var cts = new CancellationTokenSource();
            
            var t = Task.Run(async () =>
            {
                try
                {
                    await Task.Delay(1000);
                    var clientServices = new ServiceCollection()
                        .AddGrpcClient<ISampleService>(new GrpcClientOptions { Url = "127.0.0.1", Port = 5000 })
                        .BuildServiceProvider();
                    var client = clientServices.GetRequiredService<ISampleService>();
                    var request = new SampleRequest { Value = 1 };
                    var response = await client.SendAsync(request, CancellationToken.None);
                    Console.WriteLine("{0} -> {1}", request.Value, response.Value);
                    cts.Cancel();
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                }
            });

            await serverHostBuilder.RunConsoleAsync(cts.Token);
            await t;
        }
    }
}