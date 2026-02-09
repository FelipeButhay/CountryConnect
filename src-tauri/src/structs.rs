use serde::{Deserialize, Serialize};


#[derive(Serialize, Deserialize, Clone)]
pub struct Group {
    pub name: String,
    pub countries: Vec<[char; 2]>,
    pub order: bool,
    pub difficulty: u8,
}

#[derive(Serialize, Deserialize)]
pub struct TempGroup {
    pub name: String,
    pub countries: Vec<String>,
    pub order: bool,
    pub difficulty: u8,
}

pub struct GroupsList {
    pub groups: Vec<Group>
}

pub struct CurrentGameState {
    pub current_groups: Vec<Group>
}

#[derive(Serialize)]
pub enum GroupStatus {
    Correct, 
    Valid, // true if it heals, false if it doesn't
    Invalid
}

#[derive(Serialize)]
pub struct GroupResponse {
    pub status: GroupStatus,
    pub titles: Vec<String>,
    pub heal: bool,
    pub almost: bool,
}