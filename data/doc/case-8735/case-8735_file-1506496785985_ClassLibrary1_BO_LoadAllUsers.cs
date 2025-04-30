using Calculator.CommonSettings;
using Calculator.Data.Repos.BO;
using Calculator.UserManager.DTO;
using Calculator.UserManager.Interfaces;
using Microsoft.Extensions.Options;
using System;
using System.Collections.Generic;
using System.Linq;


namespace Calculator.UserManager.BO
{
  public class LoadAllUsers : IUserManager<List<User>, User>
  {
    private IOptions<Configurations> conf;
    public LoadAllUsers(  IOptions<Configurations> conf)
    {
      this.conf = conf;
    }

    public List<User> Manage(User value)
    {

      try
      {
        using (var db = new UnitOfWorkForCalculatorDb(null, conf))
        {
          List<User> users = db.UserRepository.GetAll().Select(a => new User
          {

            Password = a.Password,
            IsValid = a.IsValid,
            UserID = a.UserID,
            UserName = a.UserName


          }).ToList();

          return users;
        }
      }
      catch (Exception e)
      {

        throw;
      }
    }
  }
}