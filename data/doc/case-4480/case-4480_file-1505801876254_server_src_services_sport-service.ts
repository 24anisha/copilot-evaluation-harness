import {Router, Request, Response, NextFunction} from 'express';
import SportModel from '../models/SportModel';
import DataAccess from '../data-access';

export class SportService {

    private SportModel: SportModel;
    public idGenerator:number;
    
    public constructor() {
        this.SportModel = new SportModel();
        this.idGenerator = 100;
    }

    public retrieveAllSports(response:any): any {
        // logic to retrieve available Sports (mongo code)
        var query = this.SportModel.model.find({});
        query.exec( (err, itemArray) => {
            response.json(itemArray) ;
        });
    }
}
module.exports = new SportService();