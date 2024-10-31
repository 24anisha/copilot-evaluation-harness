import {Router, Request, Response, NextFunction} from 'express';
import FieldTypeModel from '../models/FieldTypeModel';
import DataAccess from '../data-access';

export class FieldTypeService {

    private FieldTypeModel: FieldTypeModel;
    public idGenerator:number;
    
    public constructor() {
        this.FieldTypeModel = new FieldTypeModel();
        this.idGenerator = 100;
    }

    public retrieveAllFieldTypes(response:any): any {
        // logic to retrieve available FieldTypes (mongo code)
        var query = this.FieldTypeModel.model.find({});
        query.exec( (err, itemArray) => {
            response.json(itemArray) ;
        });
    }
}

module.exports = new FieldTypeService();