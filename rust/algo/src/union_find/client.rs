use std::io;

pub fn client() {
    
    println!("Please input number of objects:");

    let mut object_count = String::new();
    io::stdin().read_line(&mut object_count).ok().unwrap();
    let object_count: u32 = object_count.trim().parse().unwrap();

    println!("Please input pairs of objects to union.");
    println!("Each object must be less than ({}).", &object_count);
    println!("To move on, input an empty string");

    loop  {

        println!("Please enter the first number to union:");

        let mut first = String::new();
        io::stdin().read_line(&mut first).ok().unwrap();

        // check if first is empty, if so, break the loop

        let first: u32 = first.trim().parse().unwrap();

        println!("Please enter the second number to union:");

        let mut second = String::new();

        // check if second is empty, if so, break the loop

        io::stdin().read_line(&mut second).ok().unwrap();
        let second: u32 = second.trim().parse().unwrap();

        if !connected(&first, &second) {
            union(&first, &second);
        } else {
            println!("{} and {} are already connected.", first, second);
        }

    }

    // perhaps some benchmarking after the loop has ended. it may make more
    // sense to do the benchmarking inside of that above loop somehow


}

// will later be implemented elsewhere
fn connected(first: &u32, second: &u32) -> bool {
    return false;
}

// will later be implemented elsewhere
fn union(first: &u32, second: &u32) {
    println!("union applied to {} and {}.", first, second);
}

