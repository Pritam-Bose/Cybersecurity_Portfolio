const bcrypt = require("bcrypt");

async function main() {
    const password = "MyStrongPassword123!";

    const saltRounds = 12;

    const hash = await bcrypt.hash(
        password,
        saltRounds
    );

    console.log("Password hash:");
    console.log(hash);

    const valid = await bcrypt.compare(
        password,
        hash
    );

    console.log("Password verified:", valid);
}

main();