use std::{collections::HashSet};
use crate::structs::*;
use crate::tools::*;
use std::sync::Mutex;

#[tauri::command]
pub fn create_groups(
        s_group_list: tauri::State<GroupsList>, 
        s_current_game: tauri::State<Mutex<CurrentGameState>>
    ) -> Result<Vec<Group>, String> {

    let mut used_c: HashSet<[char; 2]> = HashSet::new();
    let mut chosen_g: Vec<Group> = Vec::new();

    let mut all_g = get_all_groups(&s_group_list).clone();

    let mut attempts = 0;
    'w_loop: while attempts < 100 {
        shuffle(&mut all_g);
        attempts += 1;

        'g_loop: for g in all_g.iter_mut() {
            let selection: Vec<[char; 2]>;

            if g.countries.len() < 4 {
                continue;
            }

            if !g.order {
                shuffle(&mut g.countries);
            } 
            
            selection = g.countries[0..4].to_vec();

            for s in selection.iter() {
                if !used_c.insert(*s) { continue 'g_loop }
            }

            chosen_g.push(Group { countries: selection, ..g.clone() });
            if chosen_g.len() == 4 { break 'w_loop }
        }

        chosen_g.clear();
        used_c.clear();
    }

    s_current_game.lock().unwrap().current_groups = chosen_g.clone();

    return Ok(chosen_g);
}

#[tauri::command]
pub fn check_group(
        gc: Vec<String>,
        s_group_list: tauri::State<GroupsList>, 
        s_current_game: tauri::State<Mutex<CurrentGameState>>
    ) -> Result<GroupResponse, String> {
        
    let g_vec: Vec<[char; 2]> = gc.iter()
        .map(|c| {
            let chars: Vec<char> = c.chars().collect();
            return [chars[0], chars[1]];
        }).collect();

    let mut is_almost: bool = false;
    let is_correct: bool = with_current_state(&s_current_game, 
        |cs| {
            for g in cs.current_groups.iter() {
                let mut valid_coutner = 4;

                for c in g_vec.iter() {
                    if !g.countries.contains(c) { valid_coutner -= 1 }
                }

                if valid_coutner == 4 { return true; } 
                if valid_coutner == 3 {
                    is_almost = true;
                    return false;
                }
            }

            return false;
        }
    );

    let all_groups = get_all_groups(&s_group_list);
    
    let mut v_titles: Vec<String> = Vec::new();
    for g in all_groups {
        let mut temp_valid = true;
        for c in g_vec.iter() {
            if !g.countries.contains(c) {
                temp_valid = false;
                break;
            }
        }

        if temp_valid {
            v_titles.push(g.name.clone());
        }
    }

    return if is_correct { 
        Ok(GroupResponse {
            status: GroupStatus::Correct,
            titles: v_titles,
            heal: false,
            almost: false,
        }) 
    } else if v_titles.len() > 0 {
        Ok(GroupResponse {
            status: GroupStatus::Valid,
            titles: v_titles,
            heal: false,
            almost: is_almost,
        }) 
    } else {
        Ok(GroupResponse {
            status: GroupStatus::Invalid,
            titles: Vec::new(),
            heal: false,
            almost: is_almost,
        }) 
    };
}

#[tauri::command]
pub fn get_remaining_groups(
        filter: Vec<String>,
        s_current_game: tauri::State<Mutex<CurrentGameState>>
    ) -> Result<Vec<Group>, String> {
    
    let current_groups: Vec<Group> = with_current_state(&s_current_game, 
        |cs| { 
            return cs.current_groups.clone()
                .into_iter()
                .filter(|g| {
                    return !filter.contains(&g.name);
                })
                .collect()
        }
    );
    
    return Ok(current_groups);
}