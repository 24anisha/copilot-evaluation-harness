using System;
using System.Net;
using System.ServiceModel;
using System.Threading.Tasks;
using Contracts;
using Kralizek.XRayRecorder;

namespace NetFxInline
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var binding = new NetTcpBinding();
            var endpointAddress = new EndpointAddress(new Uri("net.tcp://localhost:8001"));

            var channelFactory = new ChannelFactory<IService>(binding, endpointAddress);
            channelFactory.Endpoint.EndpointBehaviors.Add(new AWSXRayBehavior());

            var client = channelFactory.CreateChannel();

            try
            {
                var items = await client.ReturnsSomethingAsync();

                (client as IClientChannel).Close();

                Console.WriteLine($"Received {items.Length} items");

                foreach (var contact in items)
                {
                    Console.WriteLine($"\t{contact.FirstName} {contact.LastName}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);

                (client as IClientChannel).Abort();
            }

            Console.WriteLine("Press <ENTER> to exit");
            Console.ReadLine();
        }
    }
}