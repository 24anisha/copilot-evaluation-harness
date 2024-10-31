import * as bodyParser from 'body-parser';
import * as cookieParser from 'cookie-parser';
import * as errorhandler from 'errorhandler';
import { Express } from 'express';
import * as session from 'express-session';
import config from '../utils/conf';
import log from './log';
import apiRouter from './api';

export default async function InjectionMiddlewares(app: Express) {
    app.use(log);
    app.use(cookieParser());
    app.use(bodyParser());
    app.use(session({ secret: config.get('session:secret') }));
    app.use(errorhandler());
    app.use('/api', apiRouter);
}