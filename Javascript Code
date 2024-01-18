function calculation(a, b, c, wrap) {
    let max_dis = 0;
    let cart_value = 20 * a + 40 * b + 50 * c; // cart_value calculation
    let total_p = a + b + c;
    let dis_name = "";

    // discount calculation
    if (cart_value > 200) { // discount for cart value greater than 200
        if (10 > max_dis) {
            max_dis = 10;
            dis_name = "flat_10_discount";
        }
    }

    if (a > 10 || b > 10 || c > 10) { // discount for any product quantity greater than 10
        let value = 0;
        if (a > 10) {
            value = 20 * a * 0.05;
        } else if (b > 10) {
            value = 40 * b * 0.05;
        } else if (c > 10) {
            value = 50 * c * 0.05;
        }

        if (value > max_dis) {
            max_dis = value;
            dis_name = "bulk_5_discount";
        }
    }

    if (total_p > 20) { // discount for total no. of products greater than 20
        if (cart_value * 0.1 > max_dis) {
            max_dis = value;
            dis_name = "bulk_10_discount";
        }
    }

    if (total_p > 30 && (a > 15 || b > 15 || c > 15)) { // discount if total quantity is greater than 20 and any single product > 15
        let value = 0;

        if (a > 15) {
            value = 20 * (a - 15) * 0.5;
        } else if (b > 15) {
            value = 40 * (b - 15) * 0.5;
        } else if (c > 15) {
            value = 50 * (c - 15) * 0.5;
        }

        if (value > max_dis) {
            dis_name = "tiered_50_discount";
        }
    }

    // gift wrap
    let wrap_cost = 0;
    if (wrap === 1) {
        wrap_cost += total_p;
    }

    // shipping fee
    let half_filled = total_p % 10 !== 0 ? 1 : 0;
    let ful_filled = Math.floor(total_p / 10);
    let shipping_fee = (half_filled + ful_filled) * 5;

    // output
    console.log("Product A, quantity: ", a, "Amount: ", a * 20);
    console.log("Product B, quantity: ", b, "Amount: ", b * 40);
    console.log("Product C, quantity: ", c, "Amount: ", c * 50);
    console.log("Subtotal, without discount: ", cart_value);
    console.log("Discount name: '", dis_name, "' Discount Amount: ", max_dis);
    console.log("Shipping Fee: ", shipping_fee, "Gift Wrap Fee: ", wrap_cost);
    console.log("Grand Total: ", cart_value - max_dis + shipping_fee + wrap_cost);
}

// This is where the program is instantiated...
const a = parseInt(prompt("Enter number of products(Type A): "));
const b = parseInt(prompt("Enter number of products(Type B): "));
const c = parseInt(prompt("Enter number of products(Type C): "));
const wrap = parseInt(prompt("Enter 1 if Gift wrapper needed else enter 0: "));
console.log("\n\n");
calculation(a, b, c, wrap); // a, b, c are the quantities of products A, B, C respectively.
