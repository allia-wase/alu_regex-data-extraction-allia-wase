function extractEmails(text) {
    const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
    return text.match(emailRegex) || [];
}

function extractUrls(text) {
    const urlRegex = /https?:\/\/[^\s/$.?#].[^\s]*/g;
    return text.match(urlRegex) || [];
}

function extractPhoneNumbers(text) {
    const phoneRegex = /\(?\b\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/g;
    return text.match(phoneRegex) || [];
}

function extractTimes(text) {
    const timeRegex = /\b(?:\d{1,2}:\d{2}(?:\s?[APap][Mm])?|\d{1,2}:\d{2})\b/g;
    return text.match(timeRegex) || [];
}

const fs = require('fs');

fs.readFile('sampleData.txt', 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading the file:", err);
        return;
    }

    console.log("Extracted Emails:", extractEmails(data));
    console.log("Extracted URLs:", extractUrls(data));
    console.log("Extracted Phone Numbers:", extractPhoneNumbers(data));
    console.log("Extracted Times:", extractTimes(data));
});
