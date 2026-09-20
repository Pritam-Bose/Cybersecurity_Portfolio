const crypto = require("crypto");

const { publicKey, privateKey } =
    crypto.generateKeyPairSync("rsa", {
        modulusLength: 2048,
        publicKeyEncoding: {
            type: "spki",
            format: "pem"
        },
        privateKeyEncoding: {
            type: "pkcs8",
            format: "pem"
        }
    });

const message = "RabTech Academy Task 5";

const sign = crypto.createSign("SHA256");
sign.update(message);
sign.end();

const signature = sign.sign(privateKey, "base64");

console.log("RSA-2048 key pair generated.");
console.log("Signature:", signature);

const verify = crypto.createVerify("SHA256");
verify.update(message);
verify.end();

console.log(
    "Signature valid:",
    verify.verify(publicKey, signature, "base64")
);