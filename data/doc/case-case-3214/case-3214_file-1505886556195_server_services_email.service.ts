import * as nodemailer from 'nodemailer';
import {XOAuth2GeneratorOptions, Generator, createXOAuth2Generator} from "xoauth2";
import {SendMailOptions} from "nodemailer";
import settings from "../settings";

export class EmailService {
    private transporter: nodemailer.Transporter;

    constructor(generatorOptions, service?) {
        service = service || 'gmail';

        if(typeof generatorOptions === 'object'){
            this.transporter = nodemailer.createTransport({
                service: service,
                auth: {
                    xoauth2: createXOAuth2Generator(generatorOptions)
                }
            });
        } else {
            this.transporter = nodemailer.createTransport(generatorOptions);
        }
    }

    send(options: SendMailOptions) {
        const {from, to, subject, html} = options;
        return this.transporter.sendMail({from, to, subject, html})
            .then(({response}) => response)
    }
}

export const adminEmailService = new EmailService({
    user: settings.email.admin.user,
    clientId: settings.email.admin.clientId,
    clientSecret: settings.email.admin.clientSecret,
    refreshToken: settings.email.admin.refreshToken,
});