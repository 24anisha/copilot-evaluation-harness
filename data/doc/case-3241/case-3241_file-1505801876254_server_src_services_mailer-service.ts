import {Router, Request, Response, NextFunction} from 'express';
var nodemailer = require('nodemailer');


export class MailerService {

    public constructor() {}

    public sendEmail(res:any, requestDetails) : any {
        // Not the movie transporter!
        var transporter = nodemailer.createTransport({
            service: 'Gmail',
            auth: {
                user: 'fieldbookingsystem@gmail.com', // Your email id
                pass: 'startbooking' // Your password
            }
        });
        var text = 'Hello ' + requestDetails.user.firstName + ' ' + requestDetails.user.lastName + ',\n\n' + 'Your field booking request has been submitted with Request ID: ' + requestDetails.requestId + '. You will receive an email within the next 48 hours from ' + requestDetails.field.admin.organization + ' for payment arrangements. Thank you!';
        var mailOptions = {
            from: 'fieldbookingsystem@gmail.com', // sender address
            to: requestDetails.user.userEmail, // list of receivers
            subject: 'Field Booking Request', // Subject line
            text: text //, // plaintext body
            // html: '<b>Hello world ✔</b>' // You can choose to send an HTML body instead
        };

        transporter.sendMail(mailOptions, function(error, info){
            if(error){
                console.log(error);
                res.json({yo: 'error'});
            }else{
                console.log('Message sent: ' + info.response);
                res.json({yo: info.response});
            };
        });
    }
}
module.exports = new MailerService();