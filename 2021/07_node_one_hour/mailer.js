const nodemailer = require('nodemailer');

const email = {
    host: 'smtp.mailtrap.io',
    port: 2525,
    auth: {
        user: "18697805754359",
        pass: "3473a89556e7c6"
    }
};

const send = async (data) => {
    nodemailer.createTransport(email).sendMail(data, (error, info) => {
        if (error) {
            console.log(error);
        } else {
            console.log(info);
            return info.response;
        }
    });
};

const mail_data = {
    from: "daewon.yoon@gmail.com",
    to: "daewon.yoon@gmail.com",
    subject: "테스트메일 입니다.",
    text: "node.js 한시간만에 끝내기"
};

send(mail_data);