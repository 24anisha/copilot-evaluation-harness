using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Carupano.Runtime
{
    using Messaging;
    using Persistence;
    public class ProjectionManager
    {
        IInboundMessageBus Bus;
        IEventStore Store;
        IEnumerable<Model.ProjectionInstance> Projections;

        public ProjectionManager(IEventStore store, IInboundMessageBus bus, IEnumerable<Model.ProjectionInstance> projections)
        {
            Store = store;
            Bus = bus;
            Projections = projections;
        }

        public void Start()
        {
            foreach(var proj in Projections)
            {
                foreach(var msg in Store.Load(proj.GetState()))
                {
                    var evt = new Model.PublishedEvent(msg.Event, msg.SequenceNo);
                    if(proj.Handles(evt))
                    {
                        proj.Handle(evt);
                    }
                }
                //TODO: events might come while it's reading, so we need to set teh event handler
                //first and accumulate while building projection.
                Bus.MessageReceived += (msg) =>
                {
                    if (msg is EventMessage)
                    {
                        var inbound = msg as EventMessage;
                        var evt = new Model.PublishedEvent(inbound.Payload, inbound.SequenceNo);
                        if (proj.Handles(evt))
                        {
                            proj.Handle(evt);
                            proj.SetState(inbound.SequenceNo);
                        }
                    }
                };
                
            }
        }
    }
}