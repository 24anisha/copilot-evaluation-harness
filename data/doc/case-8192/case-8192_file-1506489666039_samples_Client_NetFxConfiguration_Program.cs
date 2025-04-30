using System;
using System.ServiceModel;
using System.Threading.Tasks;
using Contracts;

namespace NetFxConfiguration
{
    class Program
    {
        static async Task Main(string[] args)
        {
            IService client = null;

            try
            {
                var channelFactory = new ChannelFactory<IService>("MyTest");

                client = channelFactory.CreateChannel();

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