using System;
using EntityFrameworkCore.DbContext;
using EntityFrameworkCore.Model;
using Microsoft.EntityFrameworkCore;

namespace EntityFrameworkCore
{
    class Program
    {
		static void Main()
		{
			PlutoContext context = new PlutoContext(new DbContextOptions<PlutoContext>());
			context.Courses.Add(new Course("Math", "Basic Math", CourseLevel.Beginner, 150, new Author()));

			context.SaveChanges();
            Console.WriteLine("Hello World!");

			var course = context.Courses.Find(1);

			Console.ReadKey();
		}
    }
}