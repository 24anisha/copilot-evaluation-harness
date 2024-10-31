using System;
using System.Linq;
using Xamarin.Forms;
using TizenNet.SQLite.Sample.Interfaces;

namespace TizenNet.SQLite.Sample
{
    public class App : Application
    {
        public App()
        {
            // The root page of your application
            MainPage = new ContentPage
            {
                Content = new StackLayout
                {
                    VerticalOptions = LayoutOptions.Center,
                    Children = {
                        new Label {
                            HorizontalTextAlignment = TextAlignment.Center,
                            Text = "Welcome to Xamarin Forms!"
                        }
                    }
                }
            };
        }

        protected override void OnStart()
        {
            try
            {
                var dbPath = DependencyService.Get<IFileService>().PathCombine("myDB.sqlite3");

                using (var db = new BloggingContext(dbPath))
                {
                    var a = db.Blogs.ToList();
                }


            }
            catch (Exception ex)
            {


            }
        }
    }
}