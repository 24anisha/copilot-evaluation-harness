using Calculator.CommonSettings;
using Calculator.Data.Repos.BO;
using Calculator.Data.Repos.Model;
using Calculator.OperationsManager.Interfaces;
using Microsoft.Extensions.Options;
using System;

namespace Calculator.OperationsManager.BO
{
  public class InsertOperations : IOperationDb<bool, OperationValues>
  {
    private IOptions<Configurations> conf;
    public InsertOperations(IOptions<Configurations> conf)
    {
      this.conf = conf;
    }
    public bool Manage(OperationValues values )
    {

      try
      {
        using (var db = new UnitOfWorkForCalculatorDb(null, conf))
        {
          db.OperationsRepository.Add(values);

          return db.OperationsRepository.Commit() > 0;
         
        }
      }
      catch (Exception e)
      {

        return false;
      }

    }

  }
}