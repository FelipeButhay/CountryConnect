import "./css/Group.css"
import InfoHover from "../components/InfoHover";

export default function Group({ divClass, name, cc, also, almost }) {
    divClass = divClass.toLowerCase();
    return (
        <div className={"group " + divClass}>
            <span className="title">{divClass == "invalid" ? "Incorrect" : name}</span>
            {
                (divClass != "default" && divClass != "missed") && (
                    <span className={"almost " + (almost ? "show" : "")}>
                        {almost ? "You are very close" : ""}
                    </span>
                )
            }
            {
                also.length > 0 && <div style={{
                        position: "absolute", 
                        height: "3rem", 
                        width: "3rem",
                        bottom: "3.5vh",
                        right: "3vh",
                }}>
                    <InfoHover>
                        {/* <span className="title-info">{name}</span> */}
                        <span> Also valid for: </span>
                        <ul>
                            {
                                also.map((title) => {
                                    return <li className="secondar-titles-info">{title}</li>
                                })
                            }
                        </ul>
                    </InfoHover>
                </div>
            }
            <div>
                {
                    cc.map((c, i) => {
                        return (<img key={i} src={`flags/${c.toLowerCase()}.svg`}/>)
                    })
                }
            </div>
        </div>
    )
}