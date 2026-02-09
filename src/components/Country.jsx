import codes from "../data/cc.json"
import "./css/Country.css"

export default function Country({cc, selected, toggleSelect}) {
    return (
        <div 
            className={"country-sq " + (selected ? "selected " : "")}
            onClick={() => toggleSelect(cc)}
        >
            <img src={`flags/${cc.toLowerCase()}.svg`}></img>
            <span>{codes[cc]}</span>
        </div>
    )
}