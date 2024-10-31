let uuid = require('node-uuid');
let fs = require('fs');
let pathModule = require('path');
import S3 = require('aws-sdk/clients/s3');

class PhotoService {

    private uploadsBucket;

    constructor() {
        this.uploadsBucket = new S3({
            signatureVersion: 'v4',
            params: {Bucket: process.env.UPLOADS_BUCKET}
        });
    }

    upload(path: string) {
        let ext = pathModule.extname(path);
        let newName = uuid.v4() + '.' + ext;
        return new Promise((resolve, reject) => {
            fs.readFile(path, (err, data) => {
                if (err) {
                    reject(err);
                }

                const base64data = new Buffer(data, 'binary');
                this.uploadsBucket.upload({
                    Key: newName,
                    Body: base64data,
                    ACL: 'public-read'
                }, (err, data) => {
                    if (err) {
                        return reject(err);
                    }
                    resolve(data.Location)
                });

            });
        });
    }

    remove(name: string) {
        return new Promise((resolve, reject) => {
            this.uploadsBucket.deleteObject({Key: name}, function(err, data) {
                if (err) {
                    reject(err)
                }
                resolve(data)
            });
        });
    }

    removeByUrl(url: string) {
        let name = pathModule.basename(url);
        return this.remove(name);
    }

}

export let photoService = new PhotoService();