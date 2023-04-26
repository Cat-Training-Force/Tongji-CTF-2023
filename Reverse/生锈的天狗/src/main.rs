use std::io;

fn main() {
    let stdin = io::stdin();
    let mut buf = String::new();
    if stdin.read_line(&mut buf).unwrap_or(0) == 39
        && buf
            .trim()
            .as_bytes()
            .into_iter()
            .zip((1u32..).map(|v| (v * 13) + 11))
            .map(|(c, v)| *c ^ v as u8)
            .zip(
                [
                    108u8, 79u8, 81u8, 75u8, 42u8, 34u8, 20u8, 6u8, 211u8, 217u8, 197u8, 232u8,
                    198u8, 158u8, 162u8, 234u8, 158u8, 184u8, 93u8, 120u8, 116u8, 96u8, 117u8,
                    11u8, 15u8, 25u8, 37u8, 40u8, 253u8, 222u8, 235u8, 244u8, 137u8, 140u8, 153u8,
                    236u8, 145u8,
                ]
                .into_iter(),
            )
            .map(|(e, v)| e - v)
            .all(|b| b == 0)
    {
        println!("Correct!");
    } else {
        println!("Wrong!");
    }
}
