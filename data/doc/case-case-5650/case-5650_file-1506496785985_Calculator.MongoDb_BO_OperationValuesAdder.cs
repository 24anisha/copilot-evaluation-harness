using Calculator.Data.Repos.Model;
using Calculator.MongoDb.Repos.Interfaces;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Text;

namespace Calculator.MongoDb.Repos.BO
{

  public class OperationValuesAdder : OperationManager<bool, OperationValues>
  {
    public OperationValuesAdder() : base(MongoDbBase.OperationMongo)
    {
    }
    public OperationValuesAdder(IMongoDatabase mongoDatabase) : base(mongoDatabase)
    {
    }

    public override bool Manage(OperationValues user = null)
    {

      var filterBuilder = Builders<OperationValues>.Filter;
     // var filter = filterBuilder.Eq(cus => cus., user.Id);
      var updateOptions = new UpdateOptions { IsUpsert = true };

    //  if (string.IsNullOrWhiteSpace(user.Id))
     // {
        MongoCollection.InsertOne(user);
        return true;
     // }
      //else
      //{
      //  var replaceResult = MongoCollection.ReplaceOne(filter, user, updateOptions);
      //  return (replaceResult.ModifiedCount > 0);
      //}
    }
  }
}