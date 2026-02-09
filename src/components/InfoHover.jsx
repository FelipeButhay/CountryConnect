import { useState } from "react"
import "./css/InfoHover.css"

export default function InfoHover({ children }) {
    const [hover, setHover] = useState(false);
    return (
        <div className="infohover-container" 
            onMouseEnter={() => setHover(false)}
            onMouseLeave={() => setHover(true)}
        >
            <svg viewBox="-50 -50 100 100"
                style={{
                    stroke: `var(${hover ? "--text" : "--text-muted"})`,
                    strokeWidth: "6",
                    fill: "transparent"
                }}
            >
                <circle r="30"/>
                <path d="
                    M 12 12 L 0 12 L -12 12
                    M 0 12 L 0 -5 L -8 -5
                "/>
                <circle r="1.5" cy="-14"/>
            </svg>
            <div className="info">{children}</div>
        </div>
    );
}