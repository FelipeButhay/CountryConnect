pub mod structs;
pub mod commands;
pub mod tools;

use crate::structs::*;
// use crate::tools::*;

use tauri::Manager;
use std::{fs};
use std::sync::Mutex;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()    
        .plugin(tauri_plugin_opener::init())
        .setup(|app| {
            let path = app.app_handle()
                .path()
                .resource_dir()
                .map_err(|e| format!("Error obteniendo resource dir: {:?}", e))?
                .join("data/groups.json");

            let file_content = fs::read_to_string(path)
                .map_err(|e| format!("Error leyendo archivo: {}", e))?;

            let parsed: Vec<TempGroup> = serde_json::from_str(&file_content)
                .map_err(|e| format!("Error parseando JSON: {}", e))?;
            
            let groups_list: Vec<Group> = parsed
                .iter()
                .map(|g| {
                    let g_c: Vec<[char; 2]> = g.countries
                        .iter().map(|c| {
                            let chars: Vec<char> = c.chars().collect();
                            return [chars[0], chars[1]];
                        }).collect();

                    return Group { 
                        name: g.name.clone(), 
                        countries: g_c, 
                        order: g.order, 
                        difficulty: g.difficulty 
                    };
                })
                .collect();

            app.manage(GroupsList { groups: groups_list });
            app.manage(Mutex::new(CurrentGameState { 
                current_groups: Vec::new() 
            }));

            return Ok(());
        })
        .invoke_handler(tauri::generate_handler![
            commands::create_groups,
            commands::check_group,
            commands::get_remaining_groups
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
