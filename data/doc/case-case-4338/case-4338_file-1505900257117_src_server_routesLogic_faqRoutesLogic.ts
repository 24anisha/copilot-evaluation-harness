import * as express from 'express'
import * as bodyParser from 'body-parser'
import * as core from "express-serve-static-core";
import { SupportIssue } from "../../models";




export class FaqRoutesHandler {
    public delHandler(req: core.Request, faqs: Array<SupportIssue>) {
        faqs.splice(faqs.indexOf(req['faq']), 1);
    }

    public putHandler(req: core.Request) {
        req['faq'].prb = req.body.prb;
        req['faq'].sln = req.body.sln;
    }

    public patchHandler(req: core.Request) {
        for (let entry in req.body) {
            let newVal = req.body[entry];
            console.log(newVal);
            req['faq'][entry] = newVal;
        }
    }

    public getAllHandler(faqs: Array<SupportIssue>, linkedFaqs: Array<SupportIssue>, req: core.Request) {
        faqs.forEach(i => {
            let linkedFaq = Object.assign({}, i);
            linkedFaq['links'] = {};
            linkedFaq['links']['self'] = `http://${req.headers.host}/api/faq/${i.id}`
            linkedFaqs.push(linkedFaq);
        })
    }

    public getOneHandler(faq: SupportIssue, linkedFaq: SupportIssue, req: core.Request) {
        linkedFaq = Object.assign(linkedFaq, faq);

        linkedFaq['links'] = {};
        let path = `http://${req.headers.host}/api/faq/?sln=${faq.sln}`;
        path = path.replace(' ', '%20');
        linkedFaq['links']['filterBySln'] = path;


    }
}
