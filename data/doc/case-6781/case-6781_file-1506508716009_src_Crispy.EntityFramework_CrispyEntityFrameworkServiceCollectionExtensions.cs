namespace Microsoft.Extensions.DependencyInjection
{
    using Crispy.Abstractions;
    using Crispy.EntityFramework;
    using JetBrains.Annotations;
    using Microsoft.EntityFrameworkCore;
    using System;
    using System.Collections.Generic;
    using System.Text;

    public static class CrispyEntityFrameworkServiceCollectionExtensions
    {
        public static IServiceCollection AddCrispyEntityFrameworkAuto(
            this IServiceCollection services,
            [NotNull]string connectionString,
            [NotNull]string migrationAssemblyName)
        {
            var connInfo = connectionString.Split(':');
            services
                .AddDbContextPool<CrispyDbContext>(builder =>
                    {
                        var providerType = connInfo[0];
                        var conn = connInfo[1];

                        if (connInfo[0] == "mysql")
                        {
                            builder.UseMySql(conn, options =>
                                options.MigrationsAssembly(migrationAssemblyName));
                        }
                        else if (connInfo[0] == "mssql")
                        {
                            builder.UseSqlServer(conn, options => 
                                options.MigrationsAssembly(migrationAssemblyName));
                        }
                        else
                        {
                            builder.UseInMemoryDatabase(databaseName: "cripsy_memory_database");
                        }
                    })
                .AddScoped<ICrispyStore, CrispyDbContext>();

            return services;
        }

    }
}