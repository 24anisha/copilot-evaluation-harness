var moment = require('moment');
var execSync = require('child_process').execSync;
var exec = require('child_process').exec;
var argv = require('yargs').argv; // eslint-disable-line
var logFile = '/tmp/crashdump';
var lastCrashDescription = '/tmp/lastcrash';
var description = 'Unknown';
var fs = require('fs-extra');

if (process.argv[2] !== undefined) {
  description = "'" + process.argv[2] + "'";
}

var sinceTime = moment().subtract(1, 'minutes').format('YYYY-MM-DD HH:mm');
var minuteDump = execSync('/usr/bin/sudo /bin/journalctl --since="' + sinceTime + '" > /tmp/crashdump', {uid: 1000, gid: 1000}); // eslint-disable-line
var releaseDump = execSync('cat /etc/os-release >> /tmp/crashdump', {uid: 1000, gid: 1000}); // eslint-disable-line
var variant = getVariant();

try {
  var lastReport = fs.readJSONSync(lastCrashDescription, {uid: 1000, gid: 1000}).description;
} catch (e) {
  lastReport = 'last';
}

if (lastReport !== description) {
  sendCrashReport();
}

function sendCrashReport () {
  var command = "/usr/bin/curl -X POST -H 'Content-Type: multipart/form-data'" +
        " -F 'logFile=@" + logFile + "'" +
        ' -F desc=' + description +
        " -F 'variant=" + variant + "'" +
        " 'http://logs.volumio.org:7171/report/v1'";

  exec(command, {uid: 1000, gid: 1000, encoding: 'utf8'}, function (error, stdout, stderr) {
    if (error !== null) {
      console.log('Cannot send Crash Dump report: ' + error);
    } else {
      console.log('CRASH DUMP SENT: ' + stdout);
      fs.writeJSONSync(lastCrashDescription, {'description': description}, {uid: 1000, gid: 1000});
    }
  });
}

function getVariant () {
  var file = fs.readFileSync('/etc/os-release').toString().split('\n');

  var nLines = file.length;
  var str;
  for (var l = 0; l < nLines; l++) {
    if (file[l].match(/VOLUMIO_VARIANT/i)) {
      str = file[l].split('=');
      var variantRet = str[1].replace(/\"/gi, ''); // eslint-disable-line
      return variantRet;
    }
  }
}
