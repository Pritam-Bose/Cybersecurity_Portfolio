const crypto = require("crypto");

const key = crypto.randomBytes(32); // 256-bit key

function encrypt(text) {
    const iv = crypto.randomBytes(12);

    const cipher = crypto.createCipheriv(
        "aes-256-gcm",
        key,
        iv
    );

    let encrypted = cipher.update(text, "utf8", "hex");
    encrypted += cipher.final("hex");

    const authTag = cipher.getAuthTag();

    return {
        iv: iv.toString("hex"),
        encrypted,
        authTag: authTag.toString("hex")
    };
}

function decrypt(data) {
    const decipher = crypto.createDecipheriv(
        "aes-256-gcm",
        key,
        Buffer.from(data.iv, "hex")
    );

    decipher.setAuthTag(
        Buffer.from(data.authTag, "hex")
    );

    let decrypted = decipher.update(
        data.encrypted,
        "hex",
        "utf8"
    );

    decrypted += decipher.final("utf8");

    return decrypted;
}

const encrypted = encrypt("Hello RabTech Academy");

console.log("Encrypted:", encrypted);

console.log(
    "Decrypted:",
    decrypt(encrypted)
);