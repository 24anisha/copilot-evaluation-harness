using Consul;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System;

namespace OcelotServer01.Api
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc();
        }

        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseMvc();

            //String ip = Configuration["ip"];
            string ip = "127.0.0.1";
            //部署到不同服务器的时候不能写成127.0.0.1或者0.0.0.0，因为这是让服务消费者调用的地址
            int port = int.Parse(Configuration["port"]);
            var client = new ConsulClient(config => { config.Address = new Uri("http://127.0.0.1:8500"); config.Datacenter = "dc1"; });
            var result = client.Agent.ServiceRegister(new AgentServiceRegistration()
            {
                ID = "duanxin2" + Guid.NewGuid(),//服务编号，不能重复，用Guid最简单
                Name = "duanxin2",//服务的名字
                Address = ip,//我的ip地址(可以被其他应用访问的地址，本地测试可以用127.0.0.1，机房环境中一定要写自己的内网ip地址)
                Port = port,//我的端口
                Check = new AgentServiceCheck
                {
                    DeregisterCriticalServiceAfter = TimeSpan.FromSeconds(5),//服务停止多久后反注册
                    Interval = TimeSpan.FromSeconds(10),//健康检查时间间隔，或者称为心跳间隔
                    HTTP = $"http://{ip}:{port}/api/health",//健康检查地址
                    Timeout = TimeSpan.FromSeconds(5)
                }
            });
        }
    }
}