using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;

namespace budjit.core.data.SQLite
{
    public class DesignTimeDbContextFactory : IDesignTimeDbContextFactory<BudjitContext>
    {
        public BudjitContext CreateDbContext(string[] args)
        {
            string path = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            var builder = new DbContextOptionsBuilder<BudjitContext>().UseSqlite($"DataSource=budjit.db");
            return new BudjitContext(builder.Options);
        }
    }
}