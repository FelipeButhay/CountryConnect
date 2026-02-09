import { useEffect, useRef, useState } from "react";

import Country from "../components/Country";
import StarCounter from "../components/StarCounter";
import Group from "../components/Group";

import "../css/Game.css"
import { invoke } from "@tauri-apps/api/core";

/*
    g = {
        name: str,
        cc: list
        also: list
    }
*/

const TOTAL_HP = 5;

export default function Game({config}) {
    const [ccList, setCCList] = useState([]);
    const [gList, setGList] = useState([]);

    const [respArchive, setRespArchive] = useState([]);
    const [indxArchive, setIndxArchive] = useState(0);

    const [ccSelected, setCCSelected] = useState({});

    const nSelected = useRef(0);

    // const [n, setN] = useState(0);
    const [hp, setHp] = useState(TOTAL_HP);

    useEffect(() => {
        getRandomCountries()

        // const interval = setInterval(() => {
        //     setN(prev => (prev + 1));
        // }, 1000);

        // return () => clearInterval(interval);
    }, []);

    async function getRandomCountries() {
        let list = (await invoke("create_groups")).map((g) => {
            g["countries"] = g["countries"].map((chars) => chars.join(""));
            return g;
        });

        console.log(list);

        Object.assign(config, {groups: list});
        
        let countrie_list = [].concat(...list.map((g) => {return g["countries"]}));
        countrie_list = shuffleList(countrie_list);
        setCCList(countrie_list);
        setCCSelected(
            Object.fromEntries(countrie_list.map((c) => [c, false]))
        );
        setGList([]);

        nSelected.current = 0;

        setIndxArchive(0);
        setRespArchive([]);

        setHp(TOTAL_HP);
    }

    async function submitGroup() {
        let arg = [];
        for (const [cc, isSelected] of Object.entries(ccSelected)) {
            if (isSelected) arg.push(cc);
        }

        if (arg.length != 4) return;

        let response = await invoke("check_group", { gc: arg });
        console.log(response);

        nSelected.current = 0;

        switch (response["status"]) {
            case "Correct": 
                let ccSet = new Set(ccList);
                let argSet = new Set(arg);

                // delete used countries 
                let newList = [...ccSet.difference(argSet).values()];

                console.log(newList);
                setCCList(newList);
                setCCSelected(
                    Object.fromEntries(newList.map((c) => [c, false]))
                );

                // save the group in the group list
                setGList((prev) => [...prev, {
                    name: response["titles"][0],
                    cc: arg,
                    also: response["titles"].slice(1),
                    type: "default"
                }]);
                break;

            case "Valid":
                break;

            case "Invalid":
                let newHp = hp - 1;
                if (newHp == 0) {
                    let remainingGroups = 
                        (await invoke("get_remaining_groups", { filter: gList.map((g) => g.name) }))
                        .map((g) => {
                            g["countries"] = g["countries"].map((chars) => chars.join(""));
                            return g;
                        });

                    console.log(remainingGroups);

                    setGList((prev) => [...prev, ...remainingGroups.map(
                            (rg) => { return {
                                name: rg["name"],
                                cc: rg["countries"],
                                also: [],
                                type: "missed"
                            }}
                        )]
                    );

                    console.log([...gList, ...remainingGroups.map(
                        (rg) => { return {
                            name: rg["name"],
                            cc: rg["countries"],
                            also: [],
                        }}
                    )]);

                    deselectAll();
                    setCCList([]);
                }

                setHp(newHp)
                break;
        }
        
        // save the response for the archive
        setIndxArchive(respArchive.length);
        setRespArchive((prev) => [...prev, {...response, cc: arg}]);
        deselectAll();
    }

    function shuffleList(list) {
        return [...list].sort(() => Math.random() - .5);
    }

    function deselectAll() {
        nSelected.current = 0;
        setCCSelected(
            Object.fromEntries(
                Object.keys(ccSelected).map(key => [key, false])
            )
        )
    }

    function toggleCC(cc) {
        nSelected.current += ccSelected[cc] ? -1 : 1;

        if (nSelected.current == 5) {
            nSelected.current = 4;
            return; 
        }

        setCCSelected(prev => ({
            ...prev,
            [cc]: !prev[cc],
        }));
    }

    // const temp = 12;
    return (
        <div className="game">
            <div className="game-buttons">
                <button className="game-new"  onClick={getRandomCountries}>
                    <svg viewBox="-50 -50 100 100">
                        <path stroke="var(--text)" fill="transparent" strokeWidth="3.5" d="
                            M -20 -30 L 0 -30 A 30 30 0 1 1 -30 0"/>
                        <path stroke="var(--text)" fill="transparent" strokeWidth="3.5" d="
                            M -10 -20 L -20 -30 L -10 -40"/>
                    </svg>
                </button>
                <button className="game-submit"  onClick={submitGroup}>
                    <svg viewBox="-50 -50 100 100">
                        <path stroke="var(--text)" strokeWidth="3.5" d="
                            M 0 10 L 0 -30 M -10 -20 L 0 -30 L 10 -20"/>
                        <path stroke="var(--text-muted)" fill="transparent" strokeWidth="3.5" d="
                            M -12 0 A 25 12 0 1 0 12 0"/>
                    </svg>
                </button>
                <button className="game-shuffle" onClick={() => setCCList(shuffleList(ccList))}>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" viewBox="-50 -50 100 100">
                        <g id="f" transform="translate(0, 32.5)"
                        style={{
                            strokeWidth: 3.5,
                            fill: "transparent",
                        }}>
                            <path d="M -40 -45 L -20 -45 C -5 -45 -5 -20 10 -20 L 40 -20"/>
                            <path d="M 32 -28 L 40 -20 L 32 -12"/>
                        </g>
                        <use stroke="var(--text-muted)" href="#f" transform="scale(1, -1)"/>
                        <use stroke="var(--text)" href="#f" transform="scale(1, 1)"/>
                    </svg>
                </button>
                <button className="game-shuffle" onClick={deselectAll}>
                    <svg viewBox="-50 -50 100 100">
                        <path id="l" stroke="var(--text)" strokeWidth="3.5" d="M 0 0 L -25 -25"/>
                        <path id="l" stroke="var(--text)" strokeWidth="3.5" d="M 0 0 L -25 +25"/>
                        <path id="l" stroke="var(--text)" strokeWidth="3.5" d="M 0 0 L +25 -25"/>
                        <path id="l" stroke="var(--text)" strokeWidth="3.5" d="M 0 0 L +25 +25"/>
                    </svg>

                </button>
            </div>
            <div className="game-grid">
                {
                    gList.map((g, i) => {
                        return <Group
                            key={i}

                            divClass={g.type}
                            almost={false}
                            name={g.name}
                            cc={g.cc}
                            also={g.also}
                        />
                    })
                }
                {
                    ccList.map((cc, i) => {
                        return <Country 
                            key={i} 
                            selected={ccSelected[cc]}
                            toggleSelect={toggleCC}
                            cc={cc}
                        />
                    })
                }
            </div>

            <div style={{
                display: "flex",
                alignItems: "center",
                flex: 1,
                flexDirection: "column",
                height: "100%",
                position: "relative",
                justifyContent: "space-between",
            }}>
                <div className="game-hp">
                    <StarCounter total={TOTAL_HP} n={hp}/>
                    <span>{`${hp} / ${TOTAL_HP} HP`}</span>
                </div>
                <div className="game-archive">
                    <button className="left-button" onClick={() => setIndxArchive((prev) => prev - 1)}>
                        <svg viewBox="-50 -50 100 100">
                            <path strokeWidth={3.5} stroke="var(--text)" fill="transparent" transform="scale(-1)"
                                d="M -15 20 L 15 0 L -15 -20"/>
                        </svg>
                    </button>

                    <div className="archive">
                        {
                            respArchive.length != 0 ? (
                                <Group
                                    divClass={respArchive[indxArchive % respArchive.length].status}
                                    name    ={respArchive[indxArchive % respArchive.length].titles[0]}
                                    cc      ={respArchive[indxArchive % respArchive.length].cc}
                                    also    ={respArchive[indxArchive % respArchive.length].titles.slice(1)}
                                    almost  ={respArchive[indxArchive % respArchive.length].almost}
                                />
                            ) : (
                                <span className="empty-archive">You haven't played yet</span>
                            )
                        }
                    </div>
                        
                    <button className="right-button" onClick={() => setIndxArchive((prev) => prev + 1)}>
                        <svg viewBox="-50 -50 100 100">
                            <path strokeWidth={3.5} fill="transparent" stroke="var(--text)"
                                d="M -15 20 L 15 0 L -15 -20"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    )
}