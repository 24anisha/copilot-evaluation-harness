import * as express from 'express'
import * as bodyParser from 'body-parser'
import * as core from "express-serve-static-core";
import * as path from 'path'
import * as csrf from 'csurf'

import { faqRouter } from "./routes/faqRoutes";

export class Server {
    app: core.Express = express();
    csrfObj = csrf({ cookie: true });
    constructor() {
        this.app.use(bodyParser.urlencoded({ extended: true }))
        this.app.use(bodyParser.json())
        this.app.use(this.csrfObj)
        // this.app.use((req, res, next) => {
        //     var csrfToken = req.csrfToken();
        //     res.locals._csrf = csrfToken;
        //     res.cookie('XSRF-TOKEN', csrfToken);
        //     console.log('XSRF-TOKEN ' + csrfToken);
        //     next();
        // });
        // this.registerStatic();
        let port: number = process.env.port || 3000;


        this.app.use('/api/faq', faqRouter);
        this.app.all('/*', (req, res) => {

            res.sendFile(path.resolve(__dirname + '/../index.html'));

            // res.render(path.join(__dirname + '/../index.html'));
        });
        // this.app.get('/', (req: core.Request, res: core.Response) => {
        //     res.send('welcome')
        // })

        this.app.listen(port, () => {
            console.log(path.join(__dirname + '/../index.html'));
            console.log(`listening on port ${port}`);
        })

    }

    private registerStatic() {
        console.log('in registerStatic');

        var staticEx = express.static(path.join(__dirname, "."), {
            maxAge: 90000,
        });

        this.app.use('/', function (req, res, next) {
            console.log("STATIC: " + req.url);

            staticEx(req, res, next);
        });
    }


}

