// file:    api/auth.api.ts
// author:  sjosephs
// date:    20/03/17

import { Router, Response, Request, NextFunction } from 'express';
import { AUTH_EXPIRY, AUTH_SECRET } from '../config';
import { UserModel, UserDocument } from '../models/user.model';
import { EmployerModel, EmployerDocument } from '../models/employer.model';
import { IUser } from 'supplyworks';
import * as jwt from 'jsonwebtoken';
import * as bpasr from 'body-parser';

export class AuthAPI {
  public router = Router();

  constructor() { this.buildRouter(); }

  buildRouter(): void {
    this.router.post('/', bpasr.json(), (req, res) => {
      var body = <IUser>req.body;
      UserModel.findOne({'email': body.email}, (err, user: UserDocument) => {
        if( err ) this.errorHandler(err);
        if( !user ) {
          this.incorrectUserPassword(res);
        } else {
          EmployerModel.findOne({'employeeId': user._id}, (empErr, emp) => {
            if(empErr) this.errorHandler(empErr);
            if(emp) user.employerId = emp._id;
            user.comparePassword(body.password, (isMatch) => {
              if(!isMatch) this.incorrectUserPassword(res);
              else {
                var token = jwt.sign( {'email': user.email, 'isAdmin': user.isAdmin, 'id': user._id, 'employerId': user.employerId}, 
                  AUTH_SECRET, { expiresIn: AUTH_EXPIRY} );
                user.password = '';
                res.status(200).json( {'success': true, 'data': {'token': token, 'user': <IUser>user}} );
              }
            });
          });
        }
      });
    });
  }

  private incorrectUserPassword(res: Response){
    res.status(200).json({'success': false, 'data': 'Incorrect username or password.'});
  }

  private errorHandler(error: any, response?: Response){ 
    console.error( 'Error in auth.api.ts - ' + (error.message || error) );
    response.status( 500 ).send('Error in auth.api.ts - ' + (error.message || error));
  }
}