using Calculator.CommonSettings;
using Calculator.Data.Repos.BO;
using Calculator.UserManager.DTO;
using Calculator.UserManager.Interfaces;
using Microsoft.Extensions.Options;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Calculator.UserManager.BO
{
  public class GetUser : IUserManager<User, User>
  {
    private IOptions<Configurations> conf;
    public GetUser(  IOptions<Configurations> conf)
    {
      this.conf = conf;
    }
    public User Manage(User value)
    {

      try
      {
        using (var db = new UnitOfWorkForCalculatorDb(null, conf))
        {
          var users = db.UserRepository.GetAll().Where(x => x.Password == value.Password && x.UserName == value.UserName).Select(a => new User
          {

            Password = a.Password,
            IsValid = a.IsValid,
            UserID = a.UserID,
            UserName = a.UserName


          }).FirstOrDefault();

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