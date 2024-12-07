const fs = require('fs');

const [, , sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;

const content1 = fs.readFileSync(sourceFilePath1, 'utf8');
const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

const concatenatedContent = `${content1.trim()}\n${content2.trim()}`;

fs.writeFileSync(destinationFilePath, concatenatedContent);
