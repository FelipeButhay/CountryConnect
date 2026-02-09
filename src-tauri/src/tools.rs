use rand::{self, Rng};
use std::sync::Mutex;

use crate::structs::*;

pub fn shuffle<T>(v: &mut Vec<T>) {
    let n = v.len();
    for i in 0..n {
        let m = rand::thread_rng().gen_range(i..n);
        v.swap(i, m);
    }
}

pub fn get_all_groups<'a>(state: &'a tauri::State<'a, GroupsList>) -> &'a Vec<Group> {
    return &state.groups;
}

pub fn with_current_state<T>(
        state: & tauri::State<Mutex<CurrentGameState>>,
        f: impl FnOnce(&CurrentGameState) -> T
    ) -> T {

    let guard = state.lock().unwrap();
    return f(&guard);
}