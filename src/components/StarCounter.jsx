import { useState, useEffect } from "react";

import "./css/StarCounter.css"

export default function StarCounter({total, n}) {
    const [svg, setSvg] = useState("");

    useEffect(() => {
        fetch(`hps/${total}.svg`)
        .then(res => res.text())
        .then(setSvg)
        .catch(() => console.log("momento gebauer"));
    }, [total]);
    
    // <g id="star-counter">
    const dynamicStyle = `
        <style>
            g#star-counter use:nth-child(n + ${n+1}) {
                fill: #aaa;
            }
        </style>
    `
    
    return (
        <div className="star-counter-frame">
            <div className="star-counter" dangerouslySetInnerHTML={{ __html: dynamicStyle + svg}} />
        </div>
    );
}