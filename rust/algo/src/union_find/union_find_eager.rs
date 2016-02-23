
struct Union_Eager {
    space: Vec<u32>,
}

trait CanConnect {
    fn connected(&self, first: &u32, second: &u32) -> bool;
}

impl CanConnect for Union_Eager {
    fn connected(first: &u32, second:&u32) -> bool {

    }
}

trait CanUnion {
    fn union(&self, first: &u32, second: &u32)
}

impl CanUnion for Union_Eager {
    fn union() {

    }
}

