using MQTTnet;
using MQTTnet.Server;
using System;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace MQTTserver
{
    public class Util
    {
        public static int TestMeIAddNumbers(int A, int B)
        {
            return A + B;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Server Started!");
            Task.Run(async () => await StartServer()).Wait();
        }

        private static async Task StartServer()
        {
            var optionsBuilder = new MqttServerOptionsBuilder()
                .WithConnectionBacklog(100)
                .WithDefaultEndpointPort(1883);

            var mqttServer = new MqttFactory().CreateMqttServer();
            await mqttServer.StartAsync(optionsBuilder.Build());
			var ct = new CancellationTokenSource();
            var heartbeatTask = Task.Run(async () => await ServerHeartbeat(ct.Token, mqttServer)); 
			
            Console.WriteLine("Type 'quit' to exit");

            while (true)
            {
				string input = Console.ReadLine(); 
				
                if (input != null && input.Contains("quit"))
                    break; 
            }
            ct.Cancel();
            await heartbeatTask; 
            await mqttServer.StopAsync();
        }

        private static async Task ServerHeartbeat(CancellationToken token, IMqttServer server)
        {
            long heartbeat =0;
            while (token.IsCancellationRequested == false)
            {
                var message = new MqttApplicationMessageBuilder()
                    .WithTopic("heartbeat")
                    .WithPayload($"I am alive for {heartbeat} seconds")
                    .WithAtMostOnceQoS()
                    .WithRetainFlag(false)
                    .Build();
                await server.PublishAsync(message);
                await Task.Delay(1000);
                heartbeat++;
            }
        }
    }
}