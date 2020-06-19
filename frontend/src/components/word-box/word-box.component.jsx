import React from "react";
import "./word-box.styles.css";

export const WordBox = (props) => (
    <div className="WordBox-container">
        <p>{props.word}</p>
    </div>
)
