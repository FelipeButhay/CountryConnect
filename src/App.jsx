import { useState } from "react";
import { invoke } from "@tauri-apps/api/core";

import Game from "./screens/ScreenGame.jsx"
import Nav from "./NavBar.jsx";

import "./css/common.css"
import "./css/variables.css"

export default function App() {
	const [screen, setScreen] = useState(0);
	const [config, setConfig] = useState({
		totalHp: 5,
		currentHp: 3,
	});

	return <>
		<Nav/>
		{screen == 0 && (<Game config={config}/>)}
	</>
} 