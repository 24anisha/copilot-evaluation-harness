using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using Tasko.Model;
using Tasko.Repository;
using Tasko.Services;

namespace Tasko.NotificationService
{
    public partial class NotificationService : ServiceBase
    {
        public NotificationService()
        {
            
        }

        public void OnNotificationTimerReached(object sender, System.Timers.ElapsedEventArgs args)
        {
            List<OrderSummary> pendingOrders = VendorData.GetOfflineOrdersWithNoRatings();
            VendorAppService service = new VendorAppService();

            foreach (OrderSummary orderSummary in pendingOrders)
            {
                service.SendNotification(orderSummary);
            }
        }

        protected override void OnStart(string[] args)
        {
            System.Timers.Timer notificationTimer = new System.Timers.Timer();
            notificationTimer.Interval = 50000;
            notificationTimer.Elapsed += new System.Timers.ElapsedEventHandler(this.OnNotificationTimerReached);
            notificationTimer.Start();
        }

        protected override void OnStop()
        {
        }
    }
}